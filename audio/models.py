from django.db import models


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
	

class Audio(models.Model):	

	"""model representing audios"""

	id = models.BigIntegerField(primary_key = True)
	chapter_order = models.IntegerField()
	chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	name = models.CharField(max_length = 250)
	length = models.IntegerField()
	audio_file = models.FileField(upload_to = 'audiofiles')
	text = models.TextField()

	def __str__(self):
		return self.name

class Audio_twenty(models.Model):
	id = models.AutoField(primary_key = True)
	chapter_id = models.IntegerField()
	audio = models.FileField(upload_to = 'audio_file_twenty')
	text = models.TextField()
	segments = models.CharField(max_length = 250)
	

class Audio_forty(models.Model):
	id = models.AutoField(primary_key = True)
	chapter_id = models.IntegerField()
	audio = models.FileField(upload_to = 'audio_file_forty')
	text = models.TextField()
	segments = models.CharField(max_length = 250)

class Audio_sixty(models.Model):
	id = models.AutoField(primary_key = True)
	chapter_id = models.IntegerField()
	audio = models.FileField(upload_to = 'audio_file_sixty')
	text = models.TextField()
	segments = models.CharField(max_length = 250)

