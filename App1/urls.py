from django.urls import path
from . import views

urlpatterns = [
    path('test',views.TestFn,name='test'),
    path('test1',views.TestFn1,name='test1')

]
