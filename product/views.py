from django.shortcuts import render, redirect
from product.models import Category

def categories(request):
    data = Category.objects.all()
    context = {'categories': data}
    return render(request, 'administrator/product/categories.html', context)

def create_category(request):
    if request.method == "POST":
        Category.objects.create(
            name=request.POST.get('category'),
            created_by=request.user
        )
        return redirect('categories')

    return render(request, 'administrator/product/cat-create.html')