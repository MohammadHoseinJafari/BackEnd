from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('product/<int:id>/',views.product,name='product'),
    path('blog/',views.blog,name='blog'),
    path('category/',views.category,name='cate'),
    path('blank/',views.blank,name='blank'),
    path('notfind/',views.notfind,name='notfind'),
    path('clients/',views.clients,name='clients'),
    path('supplier/',views.supplier,name='supplier'),
    path('persenel/',views.persenel,name='persenel'),
    path('sgup/', views.signup, name='signup'),
]