from django.urls import path

from .views import masailview

app_name = 'masail'
urlpatterns = [
    path('list/', masailview, name='masailList'),
]
