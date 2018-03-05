#The program to run PyParagraph
#Colleen Karnas-Haines
#3/2/2018

import os


data_file = os.path.join('data_bootcamp_ad.txt')
text_to_analyze = open(data_file,"r") 
para= (text_to_analyze.read()) 
data_file2 = os.path.join('coding_bootcamp_ad.txt')
text_to_analyze2 = open(data_file2,"r") 
para2= (text_to_analyze2.read()) 

count = 0
stats = {}
comparing_for_fun = [para, para2]
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
    
    #I added the EOL marker because the coding website has many periods that do not indicate a sentence, like Node.js
    total_sentences = paragraph.count(". ") + paragraph.count("?") + paragraph.count(".\n")
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


