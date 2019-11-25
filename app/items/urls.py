from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from items import views

app_name = 'items'

urlpatterns = [
    url(r'^$', views.api_root),
    path('racks/', views.RackView.as_view(), name='racks-list'),
    path('racks/<int:pk>/', views.rack_detail, name='racks-detail'),
    path('pdu/', views.PduListCreateSearchView.as_view(), name='pdu-list'),
    path('pdu/<int:pk>/', views.PduRetrieveUpdateView.as_view(), name='pdu-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)