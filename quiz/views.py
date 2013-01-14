from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.db.models import Q
from quiz.models import Question, NewQuestionForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('quiz_index.html', {})

@login_required()
def doquiz(request):
    lastmonth = date.today() - timedelta(days=30)
    try:
        # This doesn't offer the best performance, tune later
        question = Question.objects.filter(Q(used__lte=lastmonth) | Q(used__isnull=True)).order_by('?')[0]
    except IndexError as e:
        return render_to_response('quiz_noquestions.html', {})
    return render_to_response('quiz_details.html',
                             {'question': question, 'showanswer': False})

def newquestion(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = NewQuestionForm()

    return render(request, 'quiz_newquestion.html', {'form': form})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.used = date.today()
    question.save()
    return render_to_response('quiz_details.html',
                             {'question': question, 'showanswer': True})

