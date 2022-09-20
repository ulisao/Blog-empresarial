from django.urls import path
from .views import Newsletter_SignUp, Newsletter_Unsubscribe

app_name = 'newsletter'
urlpatterns = [
    path('subscribe/', Newsletter_SignUp, name='subscribe'),
    path('unsubscribe', Newsletter_Unsubscribe, name='unsubscribe'),
]
