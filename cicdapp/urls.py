# cicd/urls.py
from django.urls import path
from .views import cicd_home,render_example,get_result


urlpatterns = [
    path('', cicd_home, name='cicd_home'),
    path('render_example/', render_example, name='render_example'),
    path('api/get_result', get_result, name='get_result'),
    # path('example/', example, name='example'),
    # Add more URL patterns as needed
]
