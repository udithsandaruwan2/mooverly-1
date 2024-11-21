from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url="login")
def productsPage(request):
    user = "all"
    search_query = request.GET.get('search', '')
    products = Product.objects.all()
    products = products.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query)) 
    context = {'user':user, 'products':products, 'search_query':search_query}
    return render(request, 'products/products-page.html', context)

from django.db.models import Q

@login_required(login_url="login")
def userProductsPage(request):
    user = "current"
    user = request.user  # Use the current user object
    profile = user.profile
    search_query = request.GET.get('search', '')
    products = Product.objects.filter(owner=profile)
    products_searched = products.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    context = {'user': user, 'products': products_searched, 'search_query':search_query}  # Return only the searched products
    return render(request, 'products/products-page.html', context)

@login_required(login_url="login")
def singleProduct(request, pk):
    product = Product.objects.get(id=pk)
    profile = request.user.profile
    staff_code = profile.staff_code.code if profile.staff_code else None
    context = {'product':product, 'staff_code':staff_code}
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
    product = profile.product_set.get(uuid=pk)
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
    product = Product.objects.get(uuid=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('user-products-page')

    
    context = {'product':product}
    return render(request, 'products/delete-product.html', context)