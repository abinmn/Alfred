from django.urls import path, include
import api.views.registration as registration
import api.views.events as events
import api.views.participants as participants
import api.helper_functions.pdf_generator as pdf_generator

urlpatterns = [
    path('colleges/', registration.CollegeList.as_view()),
    path('colleges/<int:pk>', registration.CollegeDetails.as_view()),
    path('excel_id/', registration.ExcelIdDetails.as_view()),
    path('excel_id/events', participants.ExcelIDEventsView.as_view()),
    path('excel_id/events/<int:id>', participants.SpecificEventsExcelIDView.as_view()),

    path('events/', events.AllEventsList.as_view()),
    path('events/paid', events.PaidEventsList.as_view()),
    path('events/<int:id>', events.EventDetails.as_view()),
    path('events/<slug:id>/rules', events.EventRules.as_view()),
    path('events/<slug:id>/status', events.EventStatus.as_view()),

    path('events/<slug:id>/participants', participants.ParticipantsDetailsView.as_view()),
    path('events/<slug:id>/shortlist', participants.ShortListView.as_view()),
    path('events/<slug:id>/winners', participants.WinnersView.as_view()),
    
    path('events/<slug:id>/teams', participants.TeamDetailsViews.as_view()),
]