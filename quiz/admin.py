from quiz.models import Question, QuestionAdmin
from django.contrib import admin

admin.site.register(Question, QuestionAdmin)
