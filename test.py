with open("/home/fmk/Downloads/data/audios.txt", "r") as f:
		
		for line in f:
			from pydub import AudioSegment
			llist = line.split("|")
			audio_path = llist[3].replace('\n','')
			song = AudioSegment.from_file(audio_path,"flac")
			length = song.duration_seconds
			print(length)
			break
'''
i = 0
books = Book.objects.all()
for x in r2:
	minutes = x[2]
	seconds = int(minutes.split('.')[0])*60 + int(minutes.split('.')[1]) #convert minutes to seconds
	record = Chapter(id = int(x[0]), length = seconds, book_id = books[i], title = x[3])
	record.save()
	i = i + 1

j = 0
chapters = Chapter.objects.all()
for x in r3:
	record = Audio(id = int(x[6]),chapter_order = int(x[0]), chapter_id = chapters[j], name = x[2], audiofiles = x[3].rstrip(), length = int(x[4]), text = x[7].rstrip())
	record.save()
	j = j + 1
'''
