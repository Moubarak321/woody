from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, Category
# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    # if request.method == 'POST':
    #     name = request.method.POST.get('Grannulés de bois')
        # if name:
        #     return redirect (request, 'store/gran.html', context={"categories": categories})
        # elif request.method.POST.get('Bois compressé'):
        #     render(request, 'store/compress.html', context={"categories": categories})
        # elif request.method.POST.get('Bois de chauffage'):
        #     render (request, 'store/chauff.html', context={"categories": categories})
        # else:
        #     render (request, '/')

    return render(request, 'store/index.html' , {
        "products":products,
        "categories": categories
    })






def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product":product})

# def category_view(request, category):
#     product_category = get_object_or_404(Product, category= category)
#     if product_category.category == "Bois compressé":
#         return render(request , 'store/compress.html', {"product_category": product_category})
#     elif product_category == "Granulés de bois":
#         return render(request, 'store/gran.html', {"product_category": product_category})
#     elif product_category == "Bois de chauffage":
#         return render(request, 'store/chauff.html', {"product_category": product_category})
#     else:
#         return render(request, '/')

def gran(request):
    # product_category = Category.objects.get(name= cat)
    product_category = Category.objects.all()

    print(product_category)
    products_fetched = Product.objects.filter(product_category)
    print(products_fetched)
    return render(request, 'store/gran.html', context={"products_fetched": products_fetched})

# def voir_articles(slug_cat) :
#     ma_categorie = Category.object.get(slug=slug_cat)
#     mes_articles = Article.objects.filter(category=ma_categorie)

#    #retourne le templates avec les articles en paramètres

def categorie(request, category=None):
    produits = Product.objects.all()
    categories = Category.objects.all()
    if category: 
        category= get_object_or_404(Category, slug=category)
        produits=  produits.filter(category=category)
        return render(request , 'store/chauff.html', context={
            "produits":produits,
            "categories":categories,
        })

        # if request.method.POST.get('Grannulés de bois'):
        #     produits=  Category.objects.raw('SELECT * Grannulés de bois')

        #     print(produits)
        #     return render(redirect('store/gran.html', context={"produits":produits}))
        #     # return redirect (request, 'store/gran.html', context={"produitsCat": produitsCat})
        # elif request.method.POST.get('Bois compressé'):
        #     render(request, 'store/compress.html', context={"produits":produits})
        # elif request.method.POST.get('Bois de chauffage'):
        #     render (request, 'store/chauff.html', context={"produits":produits})
        # else:
        #     render (request, '/')

    return render(request, 'store/index.html' , {
        "products":produits,
        "categories": categories
    })