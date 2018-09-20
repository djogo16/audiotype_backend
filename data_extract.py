#File that extracts audio fragments from the LibriSpeecch Directory.

import os
import re

def create_file_audio():
	readerIDs = os.listdir("/home/fmk/Downloads/data/LibriSpeech/train-clean-360/")
	chapters = []
	audios = []
	for ID in readerIDs:
		chapterIDs = os.listdir("/home/fmk/Downloads/data/LibriSpeech/train-clean-360/" + str(ID))
		chapters += chapterIDs
		for chapID in chapterIDs:
			audios += sorted(os.listdir("/home/fmk/Downloads/data/LibriSpeech/train-clean-360/" + str(ID) + "/" +str(chapID)))
	audioIDs = []
	for x in audios:
		stri = "".join([number for number in re.findall(r'\d+',x) if number.startswith('0') and number!='']) + "\n"
		if(stri != "\n"):
			audioIDs.append(int(stri.strip()))
		
	with  open("/home/fmk/Downloads/data/audios.txt","w") as f1, open ("/home/fmk/Downloads/data/texts.txt","w") as f2 , open("/home/fmk/Downloads/data/text_fragments.txt","w") as f3:
		i = 0
		for a in audios:
			ID = re.search("-(.*?)[-\.]", a)
			readerID = a[0:a.find("-")]
			path = "/home/fmk/Downloads/data/LibriSpeech/train-clean-360/" + str(readerID) +"/" + ID.group(1) +"/"
			if(a.endswith(".txt")):
				f2.write(ID.group(1) +"|" + a+ "\n")
				f = open(path + a , "r")
				fragments = f.read()
				for fragment in fragments:
					f3.write(fragment)
				continue					
			f1.write(str(audioIDs[i]) + "|" + ID.group(1) + "|" + a + "|" + path + a +"\n")
			i = i+1

def create_file_chapters():
	data =[]
	with open("/home/fmk/Downloads/data/LibriSpeech/CHAPTERS.TXT", "r") as f:
		d = f.read()
		data = d.split("\n")
	with open("/home/fmk/Downloads/data/chapters_data.txt", "w") as f:
		for datum in data:
			datum_list = datum.split("|")
			if(len(datum_list)>1 and datum_list[3].strip() == "train-clean-360"):
				f.write(datum_list[0].strip() + "|" +datum_list[1].strip() + "|" + datum_list[2].strip() + "|" + datum_list[5].strip()+ "|" +datum_list[6].strip() + "|" + datum_list[7].strip() + "\n")

create_file_audio()
create_file_chapters()
				
		
		
