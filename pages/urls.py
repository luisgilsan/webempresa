
from django.urls import path
from . import views as views

urlpatterns = [
    path('<int:page_id>/', views.page,name='page'),
]