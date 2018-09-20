from audio.models import Audio
from django.core.files import File 

objects = Audio.objects.all()

for o in objects:
	path = "/home/fmk/Downloads/" + o.path[o.path.index('L'):]
	f = open(path,'rb')
	o.path = path
	o.save()
	o.audio.save(o.name, File(f))
	#print(o.path[o.path.index('L'):])




