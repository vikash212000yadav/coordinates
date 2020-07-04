from django.urls import path

from location.views import LookupView

urlpatterns = [
    path('', LookupView.as_view(), name='lookup'),
]