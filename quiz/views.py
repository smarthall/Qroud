from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from quiz.models import Question

def doquiz(request):
    question = Question.objects.order_by('?')[0]
    return render_to_response('quiz_doquiz.html', {'question': question})

def newquestion(request):
    return HttpResponse("Hello, world. You want to enter a question")

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('quiz_answer.html', {'question': question})



