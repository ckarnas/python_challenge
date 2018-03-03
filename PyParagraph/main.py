#The program to run PyParagraph
#Colleen Karnas-Haines
#3/2/2018


#
#
# I did an extra challenge which involved comparing multiple .txt files and making
# a summary/comparison analysis. It is listed as main_bonus.py
# Check it out!
#
#

import os

data_file = os.path.join('data_bootcamp_ad.txt')
text_to_analyze = open(data_file,"r") 
paragraph= (text_to_analyze.read()) 

#Find word count
words = paragraph.split()
word_count = len(words)


#Find sentence count

total_sentences = paragraph.count(".") + paragraph.count("?")

#Find Avg length of sentences
avg_length_sent = round(word_count / total_sentences, 1)


#Find Avg length of words
nonletters = sum(map(paragraph.count, [".", " ","?",",","-","!",";",":", "+", "=", "-", "<", ">"]))
total_chars = len(paragraph) - nonletters
avg_word_length = round(total_chars/word_count, 1)

#Output
fancy_line = "-----------------"
print("Paragraph analysis")
print(fancy_line)
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(total_sentences))
print("Average Letters per Word: " + str(avg_word_length))
print("Average Sentence Length: " + str(avg_length_sent))
print(fancy_line)
