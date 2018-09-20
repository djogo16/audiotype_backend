from audio.models import Audio, Chapter, Audio_twenty, Audio_forty, Audio_sixty
from pydub import AudioSegment
import os
import shutil
from os.path import expanduser
from django.core.files import File

	
def concatenate_audio(chapter_id, length_audio):
	queryset = Audio.objects.filter(chapter_id = chapter_id)
	audios_to_concatenate = []
	segments_delimitators = []
	audio_lists = []
	audios = []
	audio_limits = []
	length = 0
	i = 0
	j = 0
	c = False
	cumulative_length = 0
	text_lists = []
	texts = []
	for q in queryset:
		cumulative_length = cumulative_length + q.length
		audio_limits.append(cumulative_length)
		audios.append(q)
		texts.append(q.text)
		if(cumulative_length > length_audio):
			audio_lists.append((audios,audio_limits))
			text_lists.append(texts)
			audio_limits = []
			audios = []
			cumulative_length = 0
	for i in range(len(audio_lists)):
		audios_to_concatenate.append(audio_lists[i][0])
		segments_delimitators.append(audio_lists[i][1])
	



	#Concatinate audios to have audios of approximately length = length_audio
	i = 1
	home = expanduser('~')
	dirctory_name_audios = home +"/audio-type/django-backend/media/There" + str(chapter_id) + str(length_audio)
	directory_name_texts = home +"/audio-type/django-backend/media/Here" + str(chapter_id) + str(length_audio)
	os.makedirs(dirctory_name_audios)
	#os.makedirs("There")
	for audio_list in audios_to_concatenate:
		audio_sum = AudioSegment.from_file(str(audio_list[0].audio_file), "flac")
		for audio in range(1,len(audio_list)):
			#if (audio==0):
			#audio_sum = AudioSegment.from_file(str(audio_list[0].audio_file), "flac")
			audio_sum = audio_sum + AudioSegment.from_file(str(audio_list[audio].audio_file), "flac")
		
		audio_sum.export(dirctory_name_audios + "/" + str(chapter_id) + "-" + str(i) +".mp3", "mp3")
		i = i+ 1

	os.makedirs(directory_name_texts)
	with open(directory_name_texts + "/" + str(chapter_id) + "-concatenate.txt","w") as f:
		for audio_list in audios_to_concatenate:
			for audio in audio_list:
				f.write(audio.text + " ")
			f.write("*")
	
	return segments_delimitators
def populate_audio_models(Model,audio_length):

	home = expanduser('~')
		
	queryset = Chapter.objects.all()
	for q in queryset:
		segments_delimitators = concatenate_audio(q.id,audio_length)
		dirctory_name_audios = home +"/audio-type/django-backend/media/There" + str(q.id) + str(audio_length)
		directory_name_texts = home +"/audio-type/django-backend/media/Here" + str(q.id) + str(audio_length)
		
		with open(directory_name_texts + "/" + str(q.id) + "-concatenate.txt","r") as f:
			texts = f.read()
			texts_list = texts.split("*")
			audios_list = os.listdir(dirctory_name_audios)
			audios_list = ["/home/fmk/audio-type/django-backend/media/There" +str(q.id) +str(audio_length) +"/"+ x for x in audios_list]
			audios_list = sorted(audios_list,key=os.path.getctime)
			print(audios_list)
			print(texts_list)
		
			for i in range(len(audios_list)):
				segments = [str(x) for x in segments_delimitators[i]]
				#f2 = open(dirctory_name_audios + "/" + audios_list[i],"rb")
				f2 = open(audios_list[i],"rb")
				audio_file = File(f2)
				record = Model(chapter_id = q.id,audio = audio_file, text = texts_list[i], segments = ' '.join(segments))
				record.save()
		

def main():
	#populate_audio_models(Audio_twenty,20)
	populate_audio_models(Audio_forty,40)
	populate_audio_models(Audio_sixty,60)


		
#if __name__ == main:
#	main()			
			


		

