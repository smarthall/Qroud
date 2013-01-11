from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from quiz.models import Question

def doquiz(request):
    lastmonth = date.today() - timedelta(days=30)
    try:
        question = Question.objects.filter(Q(used__lte=lastmonth) | Q(used__isnull=True)).order_by('?')[0]
    except IndexError as e:
        return render_to_response('quiz_noquestions.html', {})
    return render_to_response('quiz_doquiz.html', {'question': question})

def newquestion(request):
    return HttpResponse("Hello, world. You want to enter a question")

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.used = date.today()
    question.save()
    return render_to_response('quiz_answer.html', {'question': question})

