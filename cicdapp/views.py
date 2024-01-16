# cicd/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time


def cicd_home(request):
    return HttpResponse(" app! ")

def render_example(request):
    context = {'message': 'Hello from the render example!'}
    return render(request, 'cicd/render_example.html', context)


# def example(request):
#     return HttpResponse("Welcome to the CICD app!")
    # context = {'message': 'Hello from the render example!'}
    # return render(request, 'cicd/render_examples.html', context)

from django.http import JsonResponse
import time

def perform_computation():
    # Simulate a long computation (10 seconds delay)
    time.sleep(10)
    return {"result": "Big Time Result!"}

def get_result(request):
    result = perform_computation()
    return JsonResponse(result)
