from django.http import HttpResponse
from django.shortcuts import render

# def home_page(request):
#     return HttpResponse('<h1>eCommerce</h1>')

def home_page(request):
    context = {
        'title':'home page',
        'content':'Welcome to python & Django eCommerce'
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title':'about page',
        'content':'about eCommerce'
    }
    return render(request, 'home_page.html', context)

def contact_page(request):
    context = {
        'title':'contact page',
        'content':'contact eCommerce'
    }
    if request.method=='POST':
        #print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))

    return render(request, 'contact/view.html', context)