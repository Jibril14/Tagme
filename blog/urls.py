
from django.urls import path

from .views import home, create

app_name = 'blogs'

urlpatterns = [
  path('', home, name='home'),
  path('tag/<str:pk>', home, name="blogs_tag"),
  path('create', create, name="create" )
]
