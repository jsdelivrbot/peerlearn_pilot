from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Learner(models.Model):
    mturkid = models.CharField(max_length=20, primary_key = True)
    feedback_clarity = models.TextField(max_length=500)
    feedback_logic = models.TextField(max_length=500)
    feedback_accuracy = models.TextField(max_length=500)

    def __unicode__(self):
        return self.mturkid+" "+self.username


