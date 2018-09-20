#Populate database with LIbrispeech ASR data(http://www.openslr.org/12/)
import pickle
import get_fields
from audio.models import Book, Chapter, Audio

#r1 = get_fields.book_fields()
#r2 = get_fields.chapter_fields()

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

with open("/home/fmk/Downloads/data/text_data1.txt","rb") as f3:
	r3 = pickle.load(f3)
	i = 0
	for x in r3:
		try:

			chapter = Chapter.objects.get(id =int(x[1]))
			record = Audio(id = int(x[6]),chapter_order = int(x[0]), chapter_id = chapter, name = x[2], audio_file = x[3].rstrip(), length = int(x[4]), text = x[7].rstrip())
			record.save()
			print("in populate2.py {} record saved {}".format(i,x))
		except Chapter.DoesNotExist:
			continue
	

