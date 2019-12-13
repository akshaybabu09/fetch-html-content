from django.contrib import admin
from django.urls import path, include

from fetch_html.views import FetchHTMLContentAPI

urlpatterns = [
    path('', FetchHTMLContentAPI.as_view(), name='fetch-html')
]
