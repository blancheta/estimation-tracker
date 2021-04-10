from django.urls import path
from tracker.views import *

urlpatterns = [
    path('', TaskView.as_view(), name='home'),
]
