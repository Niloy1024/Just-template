from django.urls import path
from .views import MyModelListCreateView,MyModel2ListCreateView

urlpatterns = [
    path('book/',MyModelListCreateView.as_view()),
    path('album/',MyModel2ListCreateView.as_view()),
       
]