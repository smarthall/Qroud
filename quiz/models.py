from django.db import models
from django.forms import ModelForm

# Create your models here.
class Question(models.Model):

    question = models.TextField()
    answer = models.CharField(max_length=250)
    user = models.CharField(max_length=30)
    added = models.DateField('date added', auto_now_add=True)
    used = models.DateField('date last used', null=True, blank=True)

    def __unicode__(self):
        return self.question

class NewQuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['used',]



