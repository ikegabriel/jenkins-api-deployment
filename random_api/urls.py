from django.urls import path
from .views import *

urlpatterns = [
    path('talent/', GetTalent.as_view(), name="talent"),
]
