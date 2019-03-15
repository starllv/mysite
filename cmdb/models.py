import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	question_text.short_description = "问题"
	pub_date.short_description = "发布时间"
	
	def was_published_recently(self):
		now = timezone.now()
		return now-datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = '最近发布了吗？'

	def __str__(self):
		return self.question_text
	
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text
