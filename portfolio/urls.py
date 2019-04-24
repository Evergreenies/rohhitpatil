from django.urls import path
from portfolio.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
