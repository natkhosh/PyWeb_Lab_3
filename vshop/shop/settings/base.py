from django.conf.global_settings import *

from vshop import settings

if settings.LANG == 'ru':
    LANG_RU = settings.LANG


PHONE_NUMBER = '+7 (812) 555-55-55'

E_MAIL = 'veganbestfood@gmail.com'

TITLE = 'Veganbestfood'

WEBSITE = "veganbestfood.com"

if settings.LANG == 'ru':
    ABOUT = 'Веганство - это практика воздержания от использования продуктов животного происхождения и ' \
            'связанная с этим философия, которая отвергает товарный статус животных.'

    DAILY_OFFER = '!!! Бесплатная доставка !!!'

    ADDRESS = '191025 Санкт-Петербург Невский пр. 122'
    CONTACTS = 'Контакты'
else:
    ABOUT = 'Veganism is the practice of abstaining from the use of animal products and an associated philosophy ' \
            'that rejects the commodity status of animals.'

    DAILY_OFFER = '!!! Free delivery !!!'

    ADDRESS = '191025 Saint-Petersburg Nevsky pr. 122'

    CONTACTS = 'Contacts'
