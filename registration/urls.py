from django.urls import path
from .views import SignUpView, ProfileUpadte, EmailUpadte

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpadte.as_view(), name='profile'),
    path('profile/email/', EmailUpadte.as_view(), name='profile_email')
]
