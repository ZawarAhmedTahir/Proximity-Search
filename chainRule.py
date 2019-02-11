
import matplotlib.pyplot as plt
from colorGenerator import colors_
import random
new_dict = {}

def chainRule(words):
    temp=words
    queryList = words.split(" /s ")
    words = [x.lower() for x in queryList]
    for word in words:
        word = word.lower()

        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1

    total_words = sum(new_dict.values())

    keys=[]
    probs=[]
    for key, value in sorted(new_dict.items(),reverse=True):
        probability = value / total_words
        keys.append(key)
        probs.append(probability)
        #print(key + ": " + str(probability))

    labels = keys
    sizes = probs
    colors = colors_(len(labels))

    plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(temp)
    plt.axis('equal')
    plt.show()






