from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def product_list(request):
    # 등록된 상품의 리스트를 볼 수 있는 view
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)

@login_required
def product_create(request):
    # 상품 등록 view
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/product_create.html', context)