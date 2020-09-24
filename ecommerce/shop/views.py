from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    products=Product.objects.all()
    prod_len=len(products)
    print(prod_len)
    nslide=[]
    if prod_len % 4==0:
        nslides=prod_len/4
        print ("hello1",nslides)

    else:
        nslides=prod_len//4 + 1
        print("hello2", nslides)
        nslide.append(nslides)
        print("nslide",nslide)
    nSlide=nslide[0]
    print ("hello--",nSlide)
    print ("----",type(nSlide))


    allprodss=[]
    catprodss=Product.objects.values('category','id')

    cats={item['category'] for item in catprodss}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        allprodss.append([prod,range(1,nSlide),nSlide])
    for i in allprodss:
        print(i)

    context={'all_prods':allprodss}

    return render(request,"home.html",context)

def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        obj=Contact(name=name,email=email,phone=phone,desc=desc)
        obj.save()
        msg="your message has been sent"
        return render(request, 'contact.html', {'msg': msg})

    return render(request,'contact.html')
def tracker(request):
    return render(request,'tracker.html')
def productview(request,myid):
    product=Product.objects.get(id=myid)
    print(product)
    return render(request,'productView.html',{'product':product})
def search(request):
    return render(request,'search.html')