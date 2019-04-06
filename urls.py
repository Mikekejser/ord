from django.urls import path
from . import views

app_name='ord'

urlpatterns = [
    path('', views.main, name='main'),
    path('kategorier', views.kategorier, name='kategorier'),
    path('kategori/<name>/<level>', views.kategori, name='kategori'),
   	path('alle_ord', views.alle_ord, name='alle_ord'),
    path('top_200', views.top_200, name='top_200'),
    path('fraser/<level>', views.fraser, name='fraser'),
    path('udtryk', views.udtryk, name='udtryk'),
   	path('ordsprog', views.ordsprog, name='ordsprog'),
]
