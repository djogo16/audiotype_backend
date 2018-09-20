import os

directory1 = "/home/fmk/Downloads/data-books/LibriSpeech/books/ascii/"
directory = "/home/fmk/Downloads/data-books/LibriSpeech/books/utf-8/"

books_id = os.listdir("/home/fmk/Downloads/data-books/LibriSpeech/books/ascii/")
with open("/home/fmk/Downloads/books.txt","w") as f:
	for ID in books_id:
		book_path = directory1 + ''.join(os.listdir(directory1 + "/"+ str(ID)))
		f.write(str(ID) +'|'+ book_path +'\n')

