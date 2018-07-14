from django.db import models

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.qtext
	qtext=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')

class Choice(models.Model):
	def __str__(self):
		return self.ctext
	ques=models.ForeignKey(Question, on_delete=models.CASCADE)
	ctext=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

class User(models.Model):
	def __str__(self):
		return self.username
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=200)