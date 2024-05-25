from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, StaffcodeForm
from products.forms import SizeForm, CategoryForm
from .models import Profile, StaffCode
from products.models import Product
from .utils import local
from django.db.models import Q

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User login successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'users/login-page.html')


@login_required(login_url="login")
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerPage(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            staff_code = form.cleaned_data.get('staff_code')
            try:
                staff_code_obj = StaffCode.objects.get(code=staff_code)
                local.staff_code = staff_code_obj  # Store the staff_code in thread-local storage
                
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                # Create user profile
                
                
                messages.success(request, 'User account was created!')
                login(request, user)
                return redirect('update-profile')
            except StaffCode.DoesNotExist:
                messages.error(request, 'Invalid staff code!')
        else:
            messages.error(request, 'An error has occurred during registration!')

    context = {'form': form}
    return render(request, 'users/register-page.html', context)


@login_required(login_url="login")
def dashboardPage(request):
    profile = request.user.profile
    staff_code = profile.staff_code.code if profile.staff_code else None
    search_query = request.GET.get('search', '')
    
    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | Q(user__username__icontains=search_query)
    ).exclude(user=profile.user)
    
    context = {'profiles': profiles, 'staff_code': staff_code, 'search_query': search_query}
    return render(request, 'users/dashboard-page.html', context)


@login_required(login_url="login")
def userProducts(request, pk):
    products = Product.objects.filter(owner_id=pk)
    context = {'products': products}
    return render(request, 'users/user-products.html', context)


@login_required(login_url="login")
def updateProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'users/update-profile.html', context)

@login_required(login_url="login")
def createStaffcode(request):
    profile = request.user.profile
    form = StaffcodeForm()

    if request.method == 'POST':
        form = StaffcodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Code added successfully!')
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'users/create-staffcode.html', context)

@login_required(login_url="login")
def addSize(request):
    profile = request.user.profile
    tag = 'size'
    form_size = SizeForm()
    if request.method == 'POST':
        form_size = SizeForm(request.POST)
        if form_size.is_valid():
            form_size.save()
            messages.success(request, 'Size added successfully!')
            return redirect('dashboard')

    context = {'form_size':form_size, 'tag':tag}
    return render(request, 'users/add-size-category.html', context)

@login_required(login_url="login")
def addCategory(request):
    profile = request.user.profile
    tag = 'category'
    form_category = CategoryForm()
    if request.method == 'POST':
        form_category = CategoryForm(request.POST)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('dashboard')

    context = {'form_category':form_category, 'tag':tag}
    return render(request, 'users/add-size-category.html', context)
