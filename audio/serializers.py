# audio/serializers.py
from rest_framework import serializers
from .models import Audio, Book, Audio_twenty, Audio_forty, Audio_sixty, Scores
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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


class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
	model = Scores
	fields = ('id', 'correct_count', 'missed_count', 'misspelled_count', 'book_title' ,'correct_answer','user_answer','created_at','stars')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
