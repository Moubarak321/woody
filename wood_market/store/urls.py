from django.urls import path
from . import views

urlpatterns = [
    path('detail/<str:slug>', views.detail, name="detail"),
    # path('category_view/<str:category>', views.category_view, name="category_view"),
    path('categorie/<slug:category>/', views.categorie, name="categorie"),

]