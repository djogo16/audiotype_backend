#Populate database with LIbrispeech ASR data(http://www.openslr.org/12/)

import get_fields
from audio.models import Book, Chapter, Audio

#r1 = get_fields.book_fields()
#r2 = get_fields.chapter_fields()
r3 = get_fields.audio_fields()

#for x in r1:
#	record = Book(id = int(x[0]), title = x[1].rstrip(), author = x[2].rstrip())
#	record.save()


#for x in r2:
#	try:
#		book = Book.objects.get(id=int(x[3]))
#		minutes = x[2]
#		seconds = int(minutes.split('.')[0])*60 + int(minutes.split('.')[1]) #convert minutes to seconds
#		record = Chapter(id = int(x[0]), length = seconds, book_id = book, title = x[4])
#		record.save()
#	except Book.DoesNotExist:
#		continue


for x in r3:
	
	try:
		chapter = Chapter.objects.get(pk =int(x[1]))
		record = Audio(id = int(x[5]),chapter_order = int(x[0]), chapter_id = chapter, name = x[2], audio_file = x[3].rstrip(), length = int(x[4]), text = x[6].rstrip())
		record.save()
		print("record saved")
	except Chapter.DoesNotExist:
		print("chapter ID : {}.".format(x[1]))
		print("in populate.py {}".format(x))
		
	

