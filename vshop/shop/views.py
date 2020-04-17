from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *
from vshop import settings


lang_ = settings.LANG




# Create your views here.


class IndexView(View):

    def get(self, request):

        # for k, v in request.COOKIES.items():
        #     print(k, v)

        return render(request, 'shop/index.html', {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS})


class ShopView(View):

    def get(self, request, page_id=1):


        # products_list = [{'name': 'Bell Pepper',
        #              'image': 'shop/images/product-1.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Strawberry',
        #              'image': 'shop/images/product-2.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Green Beans',
        #              'image': 'shop/images/product-3.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Purple Cabbage',
        #              'image': 'shop/images/product-4.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Tomatoe',
        #              'image': 'shop/images/product-5.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Brocolli',
        #              'image': 'shop/images/product-6.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Carrots',
        #              'image': 'shop/images/product-7.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Fruit Juice',
        #              'image': 'shop/images/product-8.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Onion',
        #              'image': 'shop/images/product-9.jpg',
        #              'price': '$120.00',
        #              'discount': '30%',
        #              'price_sale': '$80.00'},
        #             {'name': 'Apple',
        #              'image': 'shop/images/product-10.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Garlic',
        #              'image': 'shop/images/product-11.jpg',
        #              'price': '$120.00'},
        #             {'name': 'Chilli',
        #              'image': 'shop/images/product-12.jpg',
        #              'price': '$120.00'}]

        products_list = Product.objects.all()

        paginator = Paginator(products_list, 4)

        try:
            products = paginator.page(page_id)
            products.num_pages_tuple = tuple(range(paginator.num_pages))
        except:
            return redirect(reverse('shop'))
        return render(request, 'shop/shop.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'products': products, 'lang_': lang_})


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


class BlogView(View):

    def get(self, request):

        a_bloge = [{'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_1.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'},
                  {'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_2.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'},
                  {'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_3.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'},
                  {'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_4.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'},
                  {'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_5.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'},
                  {'date': 'July 20, 2019',
                  'image': '/static/shop/images/image_6.jpg',
                  'author': 'Admin',
                  'comment_number': '3',
                  'header': 'Even the all-powerful Pointing has no control about the blind texts',
                  'details': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,'
                             ' there live the blind texts.'}
                  ]

        return render(request, 'shop/blog.html',  {'phone_number': PHONE_NUMBER, 'e_mail': E_MAIL,
                                                   'daily_offer': DAILY_OFFER, 'title': TITLE, 'about': ABOUT,
                                                   'contacts': CONTACTS, 'address': ADDRESS, 'a_bloge': a_bloge})