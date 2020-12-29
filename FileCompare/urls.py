from django.urls import path

from FileCompare import views

app_name = 'FileCompare'

urlpatterns = [
    path('add_photo', views.add_photo, name='add_photo'),
    path('add_photo', views.add_photo, name='add_photo'),
    path('edit_photo/<int:pk>', views.edit_photo, name='edit_photo'),
    path('delete_photo/<int:pk>', views.delete_photo, name='delete_photo'),
    path('manage_photo', views.manage_photo, name='manage_photo'),
    path('', views.home, name='home'),
    path('image_match_static', views.image_match_static, name='image_match_static'),
    path('image_match_dynamic', views.image_match_dynamic, name='image_match_dynamic'),

]