from django.urls import path
from .views import (
    BlogView,
    BlogDetailView
)

urlpatterns = [
    path('blogs/', BlogView.as_view(), name="news"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="new_detail"),
]
