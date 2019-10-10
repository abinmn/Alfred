from django.urls import path
import api.views.registration as views

urlpatterns = [
    path('colleges/', views.CollegeList.as_view()),
]