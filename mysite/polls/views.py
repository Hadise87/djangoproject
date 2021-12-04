
from django.http import  HttpResponseRedirect
# from django.template import loader
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone

# As we had in generic definition generic views abstract common patterns to the point where you don’t even need to write Python code to write an app. so we changed add def to class

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

#  In question.object .... ye queryset barmigardune ke dakhele an Questions haii hast ke pub_date anha zudtar az timezone alane.
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

#  In question.object .... ye queryset barmigardune ke dakhele an Questions haii hast ke pub_date anha zudtar az timezone alane.

class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date_lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


                # we dont need these two def also:

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html' , {'question' : question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

                    # This def for vote as before
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST va request.POST['choice'] hamishe outpiteshun string hast
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html' , {
            'question': question,
            'error_message' : "you didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

             # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
             
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpPesponse("You're voting on question %s." % question_id)



