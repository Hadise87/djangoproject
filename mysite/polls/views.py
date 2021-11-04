
from django.http import Http404
from django.shortcuts import render

# Create your views here.

# part3:
from django.http import HttpResponse
from django.template import loader
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
from django.shortcuts import get_object_or_404, render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    # template = loader.get_template('polls/index.html')
    return render(request, 'polls/index.html', context)
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def index(request):
    return HttpResponse("Hello, world. You're at the polls index now.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html' , {'question' : question})
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html' , {'question' : question})
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttoResponse(response % question_id)

def vote(request, question_id):
    return HttpPesponse("You're voting on question %s." % question_id)



