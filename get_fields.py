#Module that return models fields for audioType database
from pydub import AudioSegment
import pickle

#Each of the three functions below extract fields for the Chapter, Audio and Book models
def chapter_fields():
	
	with open ("/home/fmk/Downloads/data/chapters_data.txt", "r") as f:
		fields = []		
		for line in f:
			fields.append((line.split("|")))
		return fields	

def audio_fields():
	#return_fields = []	
	fields = []
	with open("/home/fmk/Downloads/data/audios.txt", "r") as f1, open("/home/fmk/Downloads/data/text_fragments.txt","r") as f2, open("/home/fmk/Downloads/data/text_data1.txt","wb") as f3:
		fragments = f2.readlines()
		lines = f1.readlines()		
		
		for i in range(0,104014) :
			llist = lines[i].split("|")
			llist[3] = llist[3].replace('\n','')
			song = AudioSegment.from_file(llist[3],"flac")
			length = song.duration_seconds
			llist.append(length)
			
			#extract text and audio id:
			fragmentlist = fragments[i].split(' ',1)
			audio_id = fragmentlist[0].split('-',1)[1].replace('-','')			
			text = fragmentlist[1]
			llist.extend((audio_id, text))
			fields.append(llist)
			#return_fields.append(fields)
			#i = i + 1
			print("in get_fields.txt line {} {:0.2f}%\n-------------------------------------------".format(i,i/104014*100))
			print(lines[i])
			#print(fragments[i])
			#print(return_fields)
			print('\n\n')
			
	print(fields)	#pickle.dump(fields,f3)
	return fields
'''			
	with open("/home/fmk/Downloads/data/text_fragments.txt","r") as f2:
		i = 0
		#lines = f2.readlines()
		for line in f2:
			llist = line.split(' ',1)
			audio_id = llist[0].split('-',1)[1].replace('-','')
			text = llist[1]
			fields[i].extend((audio_id, text))
			i = i + 1
			print("in fragments.txt line {} {:0.2f}\n----------------------------------------".format(i,(50 + i/104014)*100))
			print(line)
'''
	
			
			
	
def book_fields():
	
	with open("/home/fmk/Downloads/data/books.txt", "r") as f:
		fields = []
		lines = f.readlines()
		for line in lines:
			fields.append((line.split("|")))
		return fields	

