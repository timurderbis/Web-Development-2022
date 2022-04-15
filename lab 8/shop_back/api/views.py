from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product as ProductModel, Category as CategoryModel
from django.http import Http404

# Create your views here.
def category_list(request):
  categories = CategoryModel.objects.all()
  json_categories = [c.to_json() for c in categories]
  return JsonResponse(json_categories, safe=False)

def category_detail(request, id):
  try:
    category = CategoryModel.objects.get(id=id)
  except CategoryModel.DoesNotExist as e:
    raise Http404
  return JsonResponse(category.to_json())

def category_product(request, id):
  try:
    category = CategoryModel.object.get(id=id)
  except CategoryModel.DoesNotExist as e:
    raise Http404
  products = category.product_set.all()
  json_product = [p.to_json() for p in products]
  return JsonResponse(json_product, safe=False)

def product_list(request):
  c1 = CategoryModel(name='Phones')
  c1.save()
  ProductModel.objects.create(name='Iphone',
                              price=599.9,
                              description='Best Phone',
                              count=1,
                              is_active=True,
                              category=c1)
  products = ProductModel.objects.all()
  products_json = [product.to_json() for product in products]
  return JsonResponse(products_json, safe=False)

def product_detail(request, id):
  try:
    product = ProductModel.objects.get(id=id)
  except ProductModel.DoesNotExist as e:
    raise Http404
  return JsonResponse(product.to_json())
