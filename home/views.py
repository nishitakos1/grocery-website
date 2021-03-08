from django.shortcuts import render
from .models import GroceryItem, Orders, Orderupdate
from math import ceil
import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def home(request):
    products = GroceryItem.objects.all()
    allProds = []
    catprods = GroceryItem.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = GroceryItem.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'home.html', params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.description.lower() or query in item.title.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = GroceryItem.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = GroceryItem.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = messages.error(
            request, "Please make sure to enter relevant search query")
    return render(request, 'search.html', params)


def about(request):
    return render(request, 'about.html')


def productview(request, myid):
    product = GroceryItem.objects.filter(id=myid)
    return render(request, 'productview.html', {'product': product[0]})


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['unameInput']
        email = request.POST['emailInput']
        fname = request.POST['fnameInput']
        lname = request.POST['lnameInput']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if len(username) > 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method == "POST":
        loginuname = request.POST['loginuname']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginuname, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def Checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email,
                       address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')


def Tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try :
            order = Orders.objects.filter(order_id = orderId, email=email)
            if len(order)>0:
                update = Orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')

