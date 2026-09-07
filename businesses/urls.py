from django.urls import path

from . import views

urlpatterns = [
    path(
        "dashboard/<int:business_id>/",
        views.dashboard,
        name="dashboard"
    ),
]
