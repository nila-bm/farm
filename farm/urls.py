from django.urls import path
from .views import FarmListView,FarmHome,FarmDetailView

app_name = 'farm'

urlpatterns = [
    path("",FarmHome.as_view(),name="home"),
    path("list/",FarmListView.as_view(),name="farmlist"),
    path("<int:pk>/",FarmDetailView.as_view(), name="farmdetail"),
]
