from django.http import HttpResponse
from django.template import loader

def cart(request):
    main = "Cart"
    nodes = {"main":main}
    cart_view = loader.get_template("cart.html")
    cart_main = cart_view.render(nodes)
    return HttpResponse(cart_main)

def categories(request):
    main = "Categories"
    nodes = {"main": main}
    categorie_view = loader.get_template("categories.html")
    categorie_main = categorie_view.render(nodes)
    return HttpResponse(categorie_main)

def checkout(request):
    main = "Checkout"
    nodes = {"main": main}
    checkout_view = loader.get_template("checkout.html")
    checkout_main = checkout_view.render(nodes)
    return HttpResponse(checkout_main)

def contacts(request):
    main = "Contacts"
    nodes = {"main": main}
    contacts_view = loader.get_template("contacts.html")
    contacts_main = contacts_view.render(nodes)
    return HttpResponse(contacts_main)

def error404(request):
    main = "Checkout"
    nodes = {"main": main}
    error404_view = loader.get_template("error404.html")
    error404_main = error404_view.render(nodes)
    return HttpResponse(error404_main)

def faqs(request):
    main = "Checkout"
    nodes = {"main": main}
    checkout_view = loader.get_template("checkout.html")
    checkout_main = checkout_view.render(nodes)
    return HttpResponse(checkout_main)

def home(request):
    main = "home"
    nodes = {"main": main}
    home_view = loader.get_template("home.html")
    home_main = home_view.render(nodes)
    return HttpResponse(home_main)

def itemdetail(request):
    main = "Itemdetail"
    nodes = {"main": main}
    itemdetail_view = loader.get_template("itemdetail).html")
    itemdetail_main = itemdetail_view.render(nodes)
    return HttpResponse(itemdetail_main)

def login(request):
    main = "Login"
    nodes = {"main": main}
    login_view = loader.get_template("login.html")
    login_main = login_view.render(nodes)
    return HttpResponse(login_main)

def orderdetail(request):
    main = "Orderdetail"
    nodes = {"main": main}
    orderdetail_view = loader.get_template("orderdetail.html")
    orderdetail_main = orderdetail_view.render(nodes)
    return HttpResponse(orderdetail_main)

def orders(request):
    main = "Orders"
    nodes = {"main": main}
    orders_view = loader.get_template("orders.html")
    orders_main = orders_view.render(nodes)
    return HttpResponse(orders_main)

def shop(request):
    main = "Shop"
    nodes = {"main": main}
    shop_view = loader.get_template("shop.html")
    shop_main = shop_view.render(nodes)
    return HttpResponse(shop_main)

def signup(request):
    main = "Signup"
    nodes = {"main": main}
    signup_view = loader.get_template("signup.html")
    signup_main = signup_view.render(nodes)
    return HttpResponse(signup_main)

def whishlist(request):
    main = "Whishlist"
    nodes = {"main": main}
    whishlist_view = loader.get_template("whishlist.html")
    whishlist_main = whishlist_view.render(nodes)
    return HttpResponse(whishlist_main)