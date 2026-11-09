from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Store, Product  
from .forms import newstoreform, newproductform, newcontactform
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html") 


def info(request):
    nombre = "Efrain"
    return render(request, "info.html", {"name": nombre})


def stores_view(request):
    s = Store.objects.all()  
    return render(request, "stores.html", {"stores": s})


def products_view(request):
    p = Product.objects.all()  
    return render(request, "products.html", {"products": p})


def create_stores(request):
    if request.method == 'GET':
        return render(request, "create_store.html", {'forms': newstoreform()})
    else:
        form = newstoreform(request.POST)
        if not form.is_valid():
            return render(request, "create_store.html", {'forms': form})
        Store.objects.create(  
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description']
        )
        return redirect('stores')


def create_product(request):
    if request.method == 'GET':
        return render(request, "create_product.html", {'forms': newproductform()})
    else:
        form = newproductform(request.POST)
        if not form.is_valid():
            return render(request, "create_product.html", {'forms': form})
        Product.objects.create(  
            title=form.cleaned_data['title'],
            price=form.cleaned_data['price'],
            store=form.cleaned_data['store']
        )
        return redirect('products')


def details(request, id):
    s = get_object_or_404(Store, id=id)  
    p = Product.objects.filter(store_id=id)  
    return render(request, 'details.html', {'store': s, 'products': p})


def contact(request):
    if request.method == 'GET':
        return render(request, 'extras/contact.html', {'form': newcontactform()})
    else:
        form = newcontactform(request.POST)
        if form.is_valid():
            try:
                destinatario = form.cleaned_data['email']
                asunto = "Contacto - Villa Navideña Efrain 🎄"
                mensaje = "🎄 ¡Hola! Gracias por contactar a Villa Navideña Efrain. 🎁\n\nHemos recibido tu solicitud con éxito.\n"
                
                # Simulación veloz integrada
                send_mail(asunto, mensaje, None, [destinatario], fail_silently=False)

                return redirect('home')
            except Exception as e:
                return render(request, 'extras/contact.html', {'form': form, 'error': f'Error: {str(e)}'})
        else:
            return render(request, 'extras/contact.html', {'form': form})


def despedirse(request, nombre, edad):
    return HttpResponse(f"<h1>Adiós, Mundo! Me llamo {nombre} y tengo {edad} años.</h1>")
