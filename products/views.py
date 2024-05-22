from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def productsPage(request):
    user = "all"
    products = Product.objects.all()
    context = {'user':user, 'products':products}
    return render(request, 'products/products-page.html', context)

@login_required(login_url="login")
def userProductsPage(request):
    user = "current"
    profile = request.user.profile
    products = Product.objects.filter(owner=profile)
    context = {'user':user, 'products':products}
    return render(request, 'products/products-page.html', context)

@login_required(login_url="login")
def singleProduct(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'products/single-product.html', context)

@login_required(login_url="login")
def addProduct(request):
    profile = request.user.profile
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = profile
            product.save()
            return redirect('user-products-page')

    context = {'form':form}
    return render(request, 'products/add-product.html', context)

@login_required(login_url="login")
def updateProduct(request, pk):
    profile = request.user.profile
    product = profile.product_set.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('user-products-page')
    
    context = {'form':form}
    return render(request, 'products/add-product.html', context)

@login_required(login_url="login")
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('user-products-page')

    
    context = {'product':product}
    return render(request, 'products/delete-product.html', context)