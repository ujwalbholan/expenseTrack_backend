from django.urls import path
from . import views 

urlpatterns = [
    path('updateProfile/', views.update_profile_view, name='update_profile_view'),
    path('changePassword/', views.change_password_view, name='change_password_view'),
]