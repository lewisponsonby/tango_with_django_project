import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views':'62',
         'likes':'31'},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views':'18',
         'likes':'9'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views':'40',
         'likes':'20'} ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': '48',
         'likes':'24'},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views':'18',
         'likes':'9'},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views':'16',
         'likes':'8'} ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views':'12',
         'likes':'6'},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views':'14',
         'likes':'7'} ]

    cats = {'Python': {'pages': python_pages},
            'Django': {'pages': django_pages},
            'Other Frameworks': {'pages': other_pages} }

    initialn=128
    for cat, cat_data in cats.items():
        c = add_cat(cat, initialn, initialn/2)
        initialn=initialn/2
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],p['views'],p['likes'])

def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title, views=views, likes=likes)[0]
    p.url=url
    p.views=views
    p.likes=likes
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
