from difflib import Differ
from pprint import pprint
import re

#def findLastIndex(word):
#	next(dropwhile(lambda x: l[x] != 'p', reversed(range(len(l)))))

def compareText(user_answer, correct_answer):
	
	diff = Differ()
	#text1 = re.sub(r'([^\s\w]|_)+', '', correct_answer)
	user_answer = user_answer.upper()
	text2 = re.sub(r"((?!['])[^\s\w]|_)+", '', user_answer)
	text2 = re.sub(r'\t', '', text2)
	user_answer_list = text2.split(" ")
	correct_answer_list = correct_answer.split(" ")
	result = (diff.compare(correct_answer_list,user_answer_list ))
	result = list(result)
	user_current_index = 0
	correct_current_index = 0
	misspelled_words_count = 0
	correct_words_count = 0
	missed_words_count = 0
	del result[-1]
	for word in result:
		#print(word[0])
		#print(word)
		if(word[0] == "+"):
			
			if(len(word[0]) == 2):
				continue
			word_list = word.split(" ")
			index = user_answer_list.index(word_list[1],user_current_index)
			user_current_index = index
			user_answer_list.insert(index,"<span>")
			user_answer_list.insert(index + 2,"</span>")
			misspelled_words_count = misspelled_words_count +1
		elif (word[0] == "-"):
			word_list = word.split(" ")
			index = correct_answer_list.index(word_list[1],correct_current_index)
			correct_current_index = index
			correct_answer_list.insert(index,"<section>")
			correct_answer_list.insert(index + 2,"</section>")
			missed_words_count = missed_words_count +1
		elif (word[0] == " "):
			correct_words_count = correct_words_count + 1
		else:
			pass
	return (" ".join(correct_answer_list), " ".join(user_answer_list),misspelled_words_count, missed_words_count, correct_words_count)
	
			
					
