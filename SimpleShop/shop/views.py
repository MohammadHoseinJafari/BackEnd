from django.shortcuts import render , HttpResponse , get_object_or_404
from .models import *
# Create your views here.

def home(request):
    Tsh = Product.objects.filter(category=2)
    all = Product.objects.all()
    hat = Product.objects.filter(category=4)
    return render(request, 'shop/index.html', {'all': all , 'tsh': Tsh , 'hat':hat})


def product(request,id):
    product = get_object_or_404(Product, id=id)
    color = Color.objects.filter(product=id)
    size = Size.objects.filter(product=id)
    cat = Category.objects.filter(product=id)
    all = Product.objects.all()
    context = {'product': product , 'all':all , 'color': color,'size':size,'cat':cat}
    return render(request, 'shop/single.html', context)

def category(request):
    return render(request,'shop/category.html')

def blog(request):
    post = Post.objects.all()
    return render(request, 'shop/blog.html', {'post': post})

def blank(request):
    return render(request,'shop/blankpage.html')

def notfind(request):
    return render(request,'shop/404.html')

def clients(request):
    cl = Client.objects.all()
    return render(request, 'shop/clients.html', {'client': cl})

def supplier(request):
    supp = Supplier.objects.all()
    return render(request,'shop/supplier.html',{'supp':supp})

def persenel(request):
    stuuf = Stuff.objects.all()
    return render(request,'shop/persenel.html',{'stuff':stuuf})

def signup(request):
    return render(request,'shop/404.html')
