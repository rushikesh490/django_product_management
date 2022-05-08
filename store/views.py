
from django.shortcuts import redirect, render
from django.views import View
from .models import Order, Product ,Register_table
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # products = Product.objects.all()
    TWMS = Product.objects.filter(type='Men')
    TWWS = Product.objects.filter(type='Women')
    mobiles = Product.objects.filter(category='4')

    print('you are: ',request.session.get('username'))

    return render(request, 'store/home.html',{'TWMS':TWMS,'TWWS':TWWS,'mobiles':mobiles}) 


def clothes(request,data=None):
    if data == None:
        products = Product.objects.all()
    elif data == 'MensTop':
        products = Product.objects.filter(category='1')
    elif data == 'WomensTop':
        products = Product.objects.filter(category='2')
    elif data == 'MensBottom':
        products = Product.objects.filter(category='5')
    elif data == 'WomensBottom':
        products = Product.objects.filter(category='6')

    print('you are: ',request.session.get('username'))

    if request.method == 'POST':
        product = request.POST['product']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            
        request.session['cart'] = cart
        print(request.session['cart'])

    return render (request, 'store/clothes.html',{'products':products})



def mobiles(request,data=None):
    if data == None:
        products = Product.objects.filter(category='4')
    elif data == 'Redmi' or data == 'Samsung' or data == 'iphone':
        products = Product.objects.filter(category='4').filter(type=data)

    if request.method == 'POST':
        product = request.POST['product']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            
        request.session['cart'] = cart
        print(request.session['cart'])

    return render (request, 'store/mobiles.html',{'products':products})

def vegetable(request):
    products = Product.objects.filter(category='7')
    if request.method == 'POST':
        product = request.POST['product']
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            
        request.session['cart'] = cart
        print(request.session['cart'])

    return render(request,'store/vegetable.html',{'products':products})

class check_out(View):
    def post(self,request):
        address = request.POST['address']
        phone = request.POST['phone']
        user = request.session.get('username')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys())) 
        print(address,phone,user,cart,products)

        for product in products:
            order = Order(user=User(id=request.user.id),
            product=product,
            price=product.price,
            quantity=cart.get(str(product.id)),
            address=address,phone_num=phone)
            request.session['cart']={}
            order.place_order()
        return redirect('cart')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        contact_num = request.POST['contact_num']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if len(username)< 3:
            messages.error(request,'Username to small')
            return redirect('signup')
        if password1 != password2:
            messages.error(request,'Passwords does not match')
            return redirect('signup')
        elif User.objects.filter(email=email):
            messages.error(request,'Email already exists')
            return redirect('signup')
        elif User.objects.filter(username=username):
            messages.error(request,'Username already exists')
            return redirect('signup')
        else:

    

            user = User.objects.create_user(username=username,email=email,password=password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            data = Register_table(user=user,contact_num=contact_num)
            data.save()
            messages.success(request,'User created successfully')
            return render(request,'store/signup.html')
        

    return render(request,'store/signup.html')

class signin(View):
    def get(self, request):
        return render(request,'store/signin.html')

    def post(self,request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                request.session['username']=user.username
                
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect('/')
            else:
                messages.error(request,"Credientials Invalid")
        return render(request,'store/signin.html')

def product_detail(request,id):
    product = Product.objects.get(pk=id)
    return render(request,'store/product_detail.html',{'product':product})

def signout(request):
    logout(request)
    return redirect('/')

def cart(request):
    if request.session.get('cart'):
        ids = list(request.session.get('cart').keys())
        products = Product.objects.filter(id__in=ids)
        return render(request, 'store/cart.html',{'products':products})
    return render(request, 'store/cart.html')
