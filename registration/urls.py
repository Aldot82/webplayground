from django.urls import path
from .views import SignUpView, ProfileUpadte

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpadte.as_view(), name='profile')
]