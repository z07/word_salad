import random
import MeCab

f = open("test.txt","r")
text_lines = f.readlines()
text = reduce(lambda x, y: x+y, text_lines)

m = MeCab.Tagger("-Owakati")
words = m.parse(text)
word_list = m.parse(text).split(' ')
tuple_list = []
for i in range(len(word_list)-2):
    tuple_list.append((word_list[i],word_list[i+1],word_list[i+2]))

first_init = tuple_list[0][0]
second_init = tuple_list[0][1]
first_key = first_init
second_key = second_init
new_text = [first_key,second_key]
for i in range(200):
    next_list = []
    for i in range(len(tuple_list)):
        if tuple_list[i][0] == first_key and tuple_list[i][1] == second_key:
            next_list.append(tuple_list[i][2])
    next_word = next_list[random.randint(0,len(next_list)-1)]
    new_text.append(next_word)
    first_key = second_key
    second_key = next_word

new_text.reverse()
last = new_text.index('\xe3\x80\x82')
len_text = len(new_text)
new_text.reverse()
new_text = new_text[:len(new_text)-last]
new_text = reduce(lambda x, y: x+y, new_text)
print new_text
