from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from colordar import views

app_name='colordar'

urlpatterns=[
    
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
