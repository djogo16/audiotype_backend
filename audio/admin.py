from django.contrib import admin
from .models import Book, Chapter, Audio_twenty



# Register your models here.

class AudioTwentyAdmin(admin.ModelAdmin):
	list_display = ('id', 'chapter_id', 'audio', 'text','segments')
	list_filter = ('id', 'text')


admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Audio_twenty, AudioTwentyAdmin)




