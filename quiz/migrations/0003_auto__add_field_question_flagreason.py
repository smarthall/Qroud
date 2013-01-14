# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.flagreason'
        db.add_column('quiz_question', 'flagreason',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.flagreason'
        db.delete_column('quiz_question', 'flagreason')


    models = {
        'quiz.question': {
            'Meta': {'object_name': 'Question'},
            'added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'flagged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flagreason': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'used': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['quiz']