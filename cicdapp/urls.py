# cicd/urls.py
from django.urls import path
from .views import cicd_home,render_example

urlpatterns = [
    path('', cicd_home, name='cicd_home'),
    path('render_example/', render_example, name='render_example'),
    # path('example/', example, name='example'),
    # Add more URL patterns as needed
]
