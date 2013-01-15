from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from quiz.models import Question, NewQuestionForm, DisputeForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'quiz_index.html', {})

@login_required()
def doquiz(request):
    lastmonth = date.today() - timedelta(days=30)
    try:
        # This doesn't offer the best performance, tune later
        question = Question.objects.filter(flagged=False).filter(Q(used__lte=lastmonth) | Q(used__isnull=True)).order_by('?')[0]
    except IndexError as e:
        return render(request, 'quiz_noquestions.html', {})
    return render(request, 'quiz_details.html',
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

def dispute(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = DisputeForm(request.POST)
        if form.is_valid():
            question.flagged = True
            question.flagreason = form.cleaned_data['flagreason']
            question.save()
            return HttpResponseRedirect('/')
    else:
        form = DisputeForm()

    return render(request, 'quiz_dispute.html',
                          {'form': form,
                           'question': question})

def answer(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    question.used = date.today()
    question.save()
    return render(request, 'quiz_details.html',
                             {'question': question, 'showanswer': True})

