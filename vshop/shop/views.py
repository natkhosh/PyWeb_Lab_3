from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *

# Create your views here.


class IndexView(View):

    def get(self, request):
        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS})


class ShopView(View):

    def get(self, request):
        return render(request, 'shop/shop.html')