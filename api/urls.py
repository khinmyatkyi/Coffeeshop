import imp
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', view=views.get_categories, name="get_json_category"),
]
