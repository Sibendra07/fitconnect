from django.urls import include, path, re_path
from rest_framework import routers

from scraper.views import ScrapeView

urlpatterns = [
    path("scrape/", ScrapeView.as_view(), name="Scrape"),
]
