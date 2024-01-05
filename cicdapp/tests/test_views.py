# tests/test_views.py
from django.test import Client
import pytest

def test_home_view():
    client = Client()
    response = client.get('/')
    assert response.status_code == 200





@pytest.mark.django_db
def test_render_example_view():
    client = Client()
    response = client.get('/render_example/')
    
    assert response.status_code == 200
    assert b'Hello from the render example!' in response.content



@pytest.mark.django_db
def test_render_example_view():
    client = Client()
    response = client.get('/examples/')
    
    assert response.status_code == 200
    assert b'Hello from the render example!' in response.content



    