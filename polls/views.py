from django.shortcuts import render, Http404, get_object_or_404
from .models import Question,Choice


# Get Question and Display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)


# Details of a Single Poll Question
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist.")
    return render(request, 'polls/detail.html', {'question':question})


# Result of a single Poll Question
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question':question})
