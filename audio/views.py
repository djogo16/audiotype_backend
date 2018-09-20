# audio/views.py
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import re
from random import randint
from serve_correct import compareText
from .models import Audio, Book, Chapter, Audio_twenty, Audio_forty, Audio_sixty
from .serializers import AudioTwentySerializer, BookSerializer


class ListAudio(generics.ListCreateAPIView):
	#serializer_class = AudioSerializer
	length = 0
	def get_queryset(self):
		chapter_id = int(self.request.query_params.get('chapter_id', None))
		length = int(self.request.query_params.get('length', None))
		chapter = Chapter.objects.get(pk = chapter_id)
		if(length == 20):	
			queryset = Audio_twenty.objects.filter(chapter_id = chapter.id)
			serializer_class = AudioTwentySerializer
		elif (length == 40):
			queryset = Audio_forty.objects.filter(chapter_id = chapter.id)
		else:
			queryset = Audio_sixty.objects.filter(chapter_id = chapter.id)
		return queryset
	def get_serializer_class(self):
		length = int(self.request.query_params.get('length', None))
		if(length == 20):	
			serializer_class = AudioTwentySerializer
		elif (length == 40):
			serializer_class = AudioFortySerializer
		else:
			serializer_class = AudioSixtySerializer
		return serializer_class
class RandomAudio(APIView):
	renderer_classes = (JSONRenderer, )
	
	def get(self,request, format = None):
		length = int(request.GET.get('length', 20))
		if(length == 20):
			queryset = Audio_twenty.objects.all()
		elif (length ==40):
			queryset = Audio_forty.objects.all()
		else:
			queryset = Audio_sixty.objects.all()
		index = randint(0,len(queryset)-1)
		return Response({"audio" :[str(queryset[index].audio)], "segments" :queryset[index].segments})
	
class SelectedBook(generics.ListCreateAPIView):
	serializer_class = BookSerializer
	def get_queryset(self):
		path = self.request.build_absolute_uri()
		book_title = self.request.query_params.get('title', None)
		if(";" not in path):
			queryset = Book.objects.filter(title = book_title)
		else:
			queryset = Book.objects.filter(title__contains = book_title)
		
		print(path)
		return queryset
class ListBooks(generics.ListCreateAPIView):
	renderer_classes = (JSONRenderer, )
	def get(self,request,format = None):
		return Response(Book.objects.values('title'))
class ServeResult(APIView):
	renderer_classes = (JSONRenderer, )
	
	def get(self,request,format = None):
		text = request.GET.get('text', '')
		path = request.GET.get('path', '')
		audio = re.search(r'audio_file.*', path).group()
		queryset = Audio_twenty.objects.filter(audio = audio)
		result_tuple = compareText(text, queryset[0].text)
		result = {
			"user_answer":result_tuple[1], 
			"correct_answer": result_tuple[0], 
			"misspelled_words_count" : result_tuple[2],
			"missed_words_count" : result_tuple[3],
			"correct_words_count" : result_tuple[4]
			}
		
		return Response(result)
