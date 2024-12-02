from django.urls import path
from .views import show_offers

app_name = "mortgages"

urlpatterns = [path("offers/", show_offers, name="offers")]
