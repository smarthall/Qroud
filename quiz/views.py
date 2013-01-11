from django.http import HttpResponse

def doquiz(request):
    return HttpResponse("Hello, world. You want to do a quiz")

def newquestion(request):
    return HttpResponse("Hello, world. You want to enter a question")

def detail(request, question_id):
    return HttpResponse("Hello, world. You want to do question %s" % question_id)



