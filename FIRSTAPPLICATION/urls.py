from FIRSTAPPLICATION import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("AddPerson", views.showForm, name="ap"),
    path("ShowData", views.showdata, name="sd"),
]