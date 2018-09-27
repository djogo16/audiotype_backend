from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Book(models.Model):

	"""Model representing books from LibriSpeech"""

	id = models.IntegerField(primary_key = True)
	author = models.CharField(max_length = 250)
	title = models.CharField(max_length = 500)
	
	def __str__(self):
		return self.title
class Chapter(models.Model):

	"""Model representing the chapters of books from LibriSpeech"""

	id = models.IntegerField(primary_key = True)
	length = models.IntegerField()
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE,related_name = 'chapters')
	title = models.CharField(max_length = 250)
	
	#class Meta:
	#	unique_together = ('book_id', 'title')
	
	def __str__(self):
		return (self.title + "|" + str(self.id))

	def __unicode__(self):
        	return '%s' % (self.title)
	

class Audio_twenty(models.Model):
	
	"""model representing audios"""
	
	id = models.AutoField(primary_key = True)
	chapter_id = models.IntegerField()
	audio = models.FileField(upload_to = 'audio_file_twenty')
	text = models.TextField()
	segments = models.CharField(max_length = 250)
	

class Scores(models.Model):
	id = models.AutoField(primary_key = True)
	correct_count = models.IntegerField()
	missed_count = models.IntegerField()
	misspelled_count = models.IntegerField()
	correct_answer = models.TextField()
	user_answer = models.TextField()
	user = models.ForeignKey(User, related_name="scores", on_delete=models.CASCADE, null=True)
	stars = models.IntegerField(default = 0)
	book_title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(default=datetime.now, blank=True)

	

