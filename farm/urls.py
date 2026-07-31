from django.urls import path
from .views import FarmListView

app_name = 'farm'

urlpatterns = [
    path("list/",FarmListView.as_view(),name="farmlist")
]
