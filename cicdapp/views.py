# cicd/views.py
from django.shortcuts import render
from django.http import HttpResponse

def cicd_home(request):
    return HttpResponse(" app! ")

def render_example(request):
    context = {'message': 'Hello from the render example!'}
    return render(request, 'cicd/render_example.html', context)


# def example(request):
#     return HttpResponse("Welcome to the CICD app!")
    # context = {'message': 'Hello from the render example!'}
    # return render(request, 'cicd/render_examples.html', context)
