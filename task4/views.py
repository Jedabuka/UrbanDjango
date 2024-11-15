from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Task4(TemplateView):

    def main_page(request):
        return render(request, 'main_page.html')

    def shop_page(request):
        title_shop = 'Фрукты'
        fruit = ['Манго', 'Ананас', 'Гранат']
        buy = 'Купить'
        context = {'title': title_shop,
                   'fruit': fruit,
                   'buy': buy}

        return render(request, 'shop_page.html', context)

    def basket_page(request):
        title_basket = 'Корзина'
        string1 = 'Пока не робит, приходите завтра!'
        string2 = 'Что ж вы всё время сегодня приходите :)'
        context = {'title': title_basket,
                   'message1': string1,
                   'message2': string2}

        return render(request, 'basket_page.html', context)

# python manage.py startapp
# django-admin startproject
# python manage.py runserver
