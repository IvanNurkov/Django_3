from django.shortcuts import render
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    sort_page = request.GET.get('sort')
    phones_objects = Phone.objects.all()

    if sort_page == 'max_price':
        phones_objects = phones_objects.order_by('price').revers()
    elif sort_page == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sort_page == 'name':
        phones_objects = phones_objects.order_by('name')

    context = {'phone': phones_objects, }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
