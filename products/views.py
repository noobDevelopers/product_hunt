from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    product = Product.objects
    return render(request,'products/home.html',{'products':product})
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title=request.POST['title']
            product.pub_date=timezone.datetime.now()
            product.body=request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://'+request.POST['url']
            product.image=request.FILES['image']
            product.icon=request.FILES['icon']
            product.hunter=request.user
            product.save()
            return redirect('/product/'+str(product.id))

        else:
            return render(request,'products/create.html',{'error':'One or More Field Missing'})

    else:        
        return render(request,'products/create.html')
def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})
@login_required(login_url="/account/signup")
def upvote(request,product_id):
   
    product=get_object_or_404(Product,pk=product_id)
    product.votes_total+=1
    product.save()
    return redirect('/product/'+str(product.id))
    


