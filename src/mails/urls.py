from django.urls import path

from mails.views import subscribe


app_name = "mails"

urlpatterns = [path("subscribe", subscribe, name="subscribe")]
