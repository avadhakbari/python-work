from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProductMst, ProductSubCat

def product_sub_category_details(request):
    products = ProductMst.objects.all()
    return render(request, 'product_sub_category_details.html', {'products': products})

def add_product_sub_category(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_model = request.POST.get('product_model')
        product_ram = request.POST.get('product_ram')

        product_sub_category = ProductSubCat(
            product_id=ProductMst.objects.get(product_id=product_id),
            product_price=product_price,
            product_image=product_image,
            product_model=product_model,
            product_ram=product_ram
        )
        product_sub_category.save()
        return redirect('product_sub_category_details')
    else:
        products = ProductMst.objects.all()
        return render(request, 'add_product_sub_category.html', {'products': products})

def view_product_sub_category(request, pk):
    product_sub_category = ProductSubCat.objects.get(pk=pk)
    return render(request, 'view_product_sub_category.html', {'product_sub_category': product_sub_category})

def update_product_sub_category(request, pk):
    product_sub_category = ProductSubCat.objects.get(pk=pk)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_price = request.POST.get('product_price')
        product_image = request.FILES.get('product_image')
        product_model = request.POST.get('product_model')
        product_ram = request.POST.get('product_ram')

        product_sub_category.product_id = ProductMst.objects.get(product_id=product_id)
        product_sub_category.product_price = product_price
        product_sub_category.product_image = product_image
        product_sub_category.product_model = product_model
        product_sub_category.product_ram = product_ram
        product_sub_category.save()
        return redirect('product_sub_category_details')
    else:
        products = ProductMst.objects.all()
        return render(request, 'update_product_sub_category.html', {'product_sub_category': product_sub_category, 'products': products})

def delete_product_sub_category(request, pk):
    product_sub_category = ProductSubCat.objects.get(pk=pk)
    if request.method == 'POST': 
        product_sub_category.delete()
        return redirect('product_sub_category_details')
    return render(request, 'delete_product_sub_category.html', {'product_sub_category': product_sub_category})

def search_product(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        products = ProductMst.objects.filter(product_name__icontains=search_query)
        return render(request, 'search_product.html', {'products': products})
    return render(request, 'search_product.html')