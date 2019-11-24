from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from items import views

app_name = 'items'

urlpatterns = [
    path('racks/', views.RackView.as_view()),
    path('racks/<int:pk>/', views.rack_detail),
    path('pdu/', views.PduListCreateSearchView.as_view()),
    path('pdu/<int:pk>/', views.PduRetrieveUpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)