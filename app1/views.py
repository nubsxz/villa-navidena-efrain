from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Store, Product  
from .forms import newstoreform, newproductform, newcontactform
from email.message import EmailMessage
import smtplib
import os

def home(request):
    # CORREGIDO: Buscaba en extras/ pero está afuera
    return render(request, "home.html") 


def info(request):
    nombre = "Efrain"
    # CORREGIDO: Buscaba en extras/ pero está afuera
    return render(request, "info.html", {
        "name": nombre})


def stores_view(request):
    s = Store.objects.all()  
    # CORREGIDO: Buscaba en extras/ pero está afuera
    return render(request, "stores.html", {
        "stores": s
    })


def products_view(request):
    p = Product.objects.all()  
    # CORREGIDO: Buscaba en extras/ pero está afuera
    return render(request, "products.html", {
        "products": p
    })


def create_stores(request):
    if request.method == 'GET':
        # CORREGIDO: Buscaba en extras/ pero está afuera
        return render(request, "create_store.html", {
            'forms': newstoreform()
        })
    else:
        form = newstoreform(request.POST)
        if not form.is_valid():
            # CORREGIDO: Buscaba en extras/ pero está afuera
            return render(request, "create_store.html", {'forms': form})
        Store.objects.create(  
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description']
        )
        return redirect('stores')


def create_product(request):
    if request.method == 'GET':
        # CORREGIDO: Buscaba en extras/ pero está afuera
        return render(request, "create_product.html", {
            'forms': newproductform()
        })
    else:
        form = newproductform(request.POST)
        if not form.is_valid():
            # CORREGIDO: Buscaba en extras/ pero está afuera
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
    # CORREGIDO: Buscaba en extras/ pero está afuera
    return render(request, 'details.html', {
        'store': s,
        'products': p
    })


def contact(request):
    if request.method == 'GET':
        # MANTENIDO: navegacion.html y contact.html sí se ven dentro de la carpeta extras
        return render(request, 'extras/contact.html', {'form': newcontactform()})
    else:
        try:
            remitente = "efrainmoncru10@gmail.com"
            destinatario = request.POST['email']
            password_app = "xerv vugh cffm rmcx"  

            mensaje = """Saludos, gracias por contactarnos
              Nuestros productos son los siguientes:
        """

            for i in Product.objects.all():  
                mensaje = mensaje + str(i) + ' - $' + str(i.price) + '\n'

            email = EmailMessage()
            email["From"] = remitente
            email["To"] = destinatario
            email["Subject"] = "Contacto tienda - Nuestros Productos Maricarmen"
            email.set_content(mensaje)  

            smtp = smtplib.SMTP("smtp.gmail.com", 587)
            smtp.starttls()
            smtp.login(remitente, password_app)
            smtp.sendmail(remitente, destinatario, email.as_string())
            smtp.quit()

            return redirect('home')

        except Exception as e:
            # MANTENIDO: navegacion.html y contact.html sí se ven dentro de la carpeta extras
            return render(request, 'extras/contact.html', {
                'form': newcontactform(),
                'error': f'Error: {str(e)}'
            })


def despedirse(request, nombre, edad):
    return HttpResponse(f"<h1>Adiós, Mundo! Me llamo {nombre} y tengo {edad} años.</h1>")
