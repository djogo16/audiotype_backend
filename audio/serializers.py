# audio/serializers.py
from rest_framework import serializers
from .models import Audio, Book, Audio_twenty, Audio_forty, Audio_sixty


class AudioTwentySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
      	    'audio',
	    'text',
            'segments',
        )
        model = Audio_twenty

class AudioFortySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
	    'audio',
	    'text',
            'segments',
        )
        model = Audio_forty
class AudioSixtySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
	    'audio',
	    'text',
            'segments',
        )
        model = Audio_sixty

class BookSerializer(serializers.ModelSerializer):
	chapters = serializers.StringRelatedField(many=True)
	class Meta:
		fields = (
		    'id',
		    'title',
		    'chapters',
		)
		model = Book
