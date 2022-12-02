# TODO настройте здесь urls для заданий get_car и search_car)
from django.urls import path

from cars import views

urlpatterns = [
    path("", views.cars, name="cars_list"),
    path("<int:pk>/", views.get_car, name="car"),
    path("search/", views.search, name="car_search")
]
