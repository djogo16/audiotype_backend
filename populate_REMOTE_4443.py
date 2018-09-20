#Populate database with LIbrispeech ASR data(http://www.openslr.org/12/)

import get_fields
from audio.models import Chapter, Transcription

#r1 = get_fields.audio_fields()
r2 = get_fields.chapter_fields()
#r3 =  get_fields.transcription_fields()

#for x in r1:
#	record = Audio(chapter_order = int(x[0]), chapter_id = int(x[1]), name = x[2], length = int(x[4]), path = x[5])
#	record.save()


for x in r2:
	record = Chapter(id = int(x[0]), minutes = int(x[2]), title = x[3], book_title = x[4])
	record.save()
#for x in r3:
#	record = Transcription(chapter_id = int(x[0]), name = x[1])
#	record.save()


