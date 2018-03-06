#The program to run PyParagraph
#Colleen Karnas-Haines
#3/2/2018
#I did some extra comparisons in this program

import os
import sys

#I made this a dynamic data entry
more_data = True
comparing_for_fun = []
while more_data:
    print("Your data should be available from the raw_data folder. If you have not placed it in there,")
    print("please do so before continuing.")
    file_name = input("What is your file name?")
    next_path = os.path.join("raw_data", file_name)
    if os.path.isfile(next_path)  ==False:
        print("I'm sorry. That file does not exist. Please confirm your file name and retry later.")
        sys.exit("Doh!")
    text_to_analyze = open(next_path,"r") 
    comparing_for_fun.append(text_to_analyze.read()) 
    continue_ques = input("Do you have any more data sets to add to this run? y/n: ")
    if (continue_ques.upper() == "N") | (continue_ques.upper() =="NO"):
        more_data = False
        
count = 0
stats = {}
for paragraph in comparing_for_fun:
    count = count+1
    words = paragraph.split()
    word_count = len(words)
    stats[count] = {}
    stats[count]["Word Count"] = word_count
    #word_count
    total_sentences = 0
    #I found 2 ways to find the sentence. I'll keep the second one because it has less code
    #for x in words:
    #    if ("." in x) | ("?" in x):
    #        total_sentences = total_sentences + 1
    
    #I added the EOL marker because I tested a coding website has many periods that did not indicate a sentence, like Node.js 
    #total_sentences = paragraph.count(". ") + paragraph.count("?") + paragraph.count(".\n")

    total_sentences = paragraph.count(".") + paragraph.count("?")
    stats[count]["Sentence Count"] = total_sentences
    print(total_sentences)
    avg_length_sent = round(word_count / total_sentences, 1)
    
    stats[count]["Avg Sentence Length"] = avg_length_sent

    #I also found two ways here. I want to remember both for future reference
    #nonletters = paragraph.count(" ") + paragraph.count(".") + paragraph.count("?") + paragraph.count(",") + paragraph.count("-")
    nonletters = sum(map(paragraph.count, [".", " ","?",",","-","!",";",":", "+", "=", "-", "<", ">"]))
    total_chars = len(paragraph) - nonletters
    avg_word_length = round(total_chars/word_count, 1)
    stats[count]["Avg Word Length"] = avg_word_length
    
    #Output
    fancy_line = "-----------------"
    print("Paragraph analysis of file #" + str(count) )
    print(fancy_line)
    print("Approximate Word Count: " + str(word_count))
    print("Approximate Sentence Count: " + str(total_sentences))
    print("Average Letters per Word: " + str(avg_word_length))
    print("Average Sentence Length: " + str(avg_length_sent))
    print(fancy_line)
    
#Final Summary Analysis
print(fancy_line)
print("Let's look at some summary analysis.")
print(fancy_line)
max_word_art = max(stats, key=lambda v: stats[v]['Word Count'])
max_word = stats[max(stats, key=lambda v: stats[v]['Word Count'])]["Word Count"]

print("*Article #" + str(max_word_art) + " has the most words with " + str(max_word) + " words.")
max_sent_length_art = max(stats, key =lambda v: stats[v]["Avg Sentence Length"])
max_sent_length = stats[max(stats, key=lambda v: stats[v]["Avg Sentence Length"])]["Avg Sentence Length"]
print("*The authors of article #" + str(max_sent_length_art) + " think their audience is super sophisticated. They created sentences that are, on average, " + str(max_sent_length) + " words long!")


