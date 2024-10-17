from django.urls import path

from .views import meetings_list_view ,meeting_detail_view,meeting_create_view,room_list_view,room_detail_view,room_create_view ,delete_meeting

#domain.com/website/...
urlpatterns=[
path('all/',meetings_list_view, name='all'),
path('allrooms/',room_list_view, name='allrooms'),
 path('one/<int:meeting_id>/', meeting_detail_view, name='one'), 
 path('oneroom/<int:room_id>/', room_detail_view, name='oneroom'), 
  path('create/', meeting_create_view, name='create'), 
path('meetings/<int:id>/delete/', delete_meeting, name='delete_meeting_view'),
  path('createroom/', room_create_view, name='createroom'), 
  path('deleteroom/', room_create_view, name='deleteroom'), 

]