from django.conf.urls.static import static
from django.urls import path

from config import settings
from index import views

urlpatterns = [
    path('',views.index,name='index'),
]