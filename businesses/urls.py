from django.urls import path

from . import views
# It creates the url which links to the path of the dashboard along with the business id of the business 
urlpatterns = [
    path(
        "dashboard/<int:business_id>/",
        views.dashboard,
        name="dashboard"
    ),
]
