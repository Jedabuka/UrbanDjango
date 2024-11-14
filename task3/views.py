from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Task3(TemplateView):

    def main_page(request):
        title_main = 'Главная страница'
        link_main = "Главная"
        link_shop = 'Магазин'
        link_basket = 'Корзина'
        context = {'title': title_main,
                   'main': link_main,
                   'shop': link_shop,
                   'basket': link_basket}

        return render(request, 'main_page.html', context)

    def shop_page(request):
        title_shop = 'Фрукты'
        mango = 'Манго'
        ananas = 'Ананас'
        granat = 'Гранат'
        buy = 'Купить'
        back_shop = 'Вернуться обратно'
        context = {'title': title_shop,
                   'mango': mango,
                   'ananas': ananas,
                   'granat': granat,
                   'buy': buy,
                   'back': back_shop}

        return render(request, 'shop_page.html', context)

    def basket_page(request):
        string1 = 'Пока не робит, приходите завтра!'
        string2 = 'Что ж вы всё время сегодня приходите :)'
        back_basket = 'Вернуться обратно'
        context = {'message1': string1,
                   'message2': string2,
                   'back': back_basket}
        return render(request, 'basket_page.html', context)


# python manage.py startapp
# django-admin startproject
# python manage.py runserver
