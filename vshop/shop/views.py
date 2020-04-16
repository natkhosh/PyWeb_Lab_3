from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *


# Create your views here.


class IndexView(View):

    def get(self, request):

        # for k, v in request.COOKIES.items():
        #     print(k, v)

        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS})


class ShopView(View):

    def get(self, request):
        products = [{'name': 'Bell Pepper',
                     'image': 'shop/images/product-1.jpg',
                     'price': '$120.00',
                     'discount': '30%',
                     'price_sale': '$80.00'},
                    {'name': 'Strawberry',
                     'image': 'shop/images/product-2.jpg',
                     'price': '$120.00'},
                    {'name': 'Green Beans',
                     'image': 'shop/images/product-3.jpg',
                     'price': '$120.00'},
                    {'name': 'Purple Cabbage',
                     'image': 'shop/images/product-4.jpg',
                     'price': '$120.00'},
                    {'name': 'Tomatoe',
                     'image': 'shop/images/product-5.jpg',
                     'price': '$120.00',
                     'discount': '30%',
                     'price_sale': '$80.00'},
                    {'name': 'Brocolli',
                     'image': 'shop/images/product-6.jpg',
                     'price': '$120.00'},
                    {'name': 'Carrots',
                     'image': 'shop/images/product-7.jpg',
                     'price': '$120.00'},
                    {'name': 'Fruit Juice',
                     'image': 'shop/images/product-8.jpg',
                     'price': '$120.00'},
                    {'name': 'Onion',
                     'image': 'shop/images/product-9.jpg',
                     'price': '$120.00',
                     'discount': '30%',
                     'price_sale': '$80.00'},
                    {'name': 'Apple',
                     'image': 'shop/images/product-10.jpg',
                     'price': '$120.00'},
                    {'name': 'Garlic',
                     'image': 'shop/images/product-11.jpg',
                     'price': '$120.00'},
                    {'name': 'Chilli',
                     'image': 'shop/images/product-12.jpg',
                     'price': '$120.00'}]

        return render(request, 'shop/shop.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'products': products})


class WishlistView(View):

    def get(self, request):
        return render(request, 'shop/wishlist.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS})


class CartView(View):

    def get(self, request):
        return render(request, 'shop/cart.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS})


class ContactView(View):

    def get(self, request):
        return render(request, 'shop/contact.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'website': WEBSITE})