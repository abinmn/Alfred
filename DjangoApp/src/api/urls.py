from django.urls import path
import api.views.registration as registration

urlpatterns = [
    path('colleges/', registration.CollegeList.as_view()),
    path('colleges/<int:pk>', registration.CollegeDetails.as_view()),

]