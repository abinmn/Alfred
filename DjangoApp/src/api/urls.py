from django.urls import path
import api.views.registration as registration
import api.views.events as events

urlpatterns = [
    path('colleges/', registration.CollegeList.as_view()),
    path('colleges/<int:pk>', registration.CollegeDetails.as_view()),
    path('excel_id/', registration.ExcelIdDetails.as_view()),
    path('events/', events.AllEventsList.as_view()),
    path('events/<slug:id>', events.EventDetails.as_view()),
    path('events/<slug:id>/rules', events.EventRules.as_view()),

]