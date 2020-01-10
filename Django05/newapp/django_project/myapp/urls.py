from django.urls import path
from .views import AnimalList, AnimalDetail, AnimalCreate

app_name = 'zoo'

urlpatterns = [
    path('', AnimalList.as_view(), name='animal-list'),
    path('animal/<int:pk>', AnimalDetail.as_view(), name='animal-detail'),
    path('new-animal/', AnimalCreate.as_view(), name='animal-create'),
    # path('new-animal/', create_animal, name='animal-create'),
]