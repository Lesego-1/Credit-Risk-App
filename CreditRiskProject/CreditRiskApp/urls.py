from django.urls import path
from . import views

urlpatterns = [
    path("", views.form, name="form"),
    path("api/", views.CreditRiskListCreate.as_view(), name="api"),
    path("api/<int:pk>/", views.CreditRiskRetrieveUpdateDestroy.as_view(), name="update_api"),
]