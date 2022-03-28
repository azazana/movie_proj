from csv import excel

from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)
# admin.site.register(DressingRoom)
admin.site.register(Actor)


class RatingFilret(admin.SimpleListFilter):
    title = 'фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>80', 'Топ'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        else:
            return queryset.filter(rating__gte=80)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['budget']
    prepopulated_fields = {'slug': ('name',)}

    list_display = ['name', 'rating', 'year', 'budget', "rating_status", 'director', ]
    list_editable = ['rating', 'budget', 'director']
    # ordering = ['-rating','name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = [
        'name__istartswith', 'rating'
    ]
    list_filter = ['name', 'currency', RatingFilret]
    filter_horizontal = ['actors']

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return "Не очень"
        elif movie.rating < 70:
            return "Разок можно глянуть"
        elif movie.rating <= 84:
            return "Зачет"
        else:
            return "Топчик"

    @admin.action(description='Установить валюту доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту евро')
    def set_euro(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Было обновлено {count} записей', level=messages.ERROR)
