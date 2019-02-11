import colorGenerator
from colorGenerator import colors_
import matplotlib.pyplot as plt
def plotPie(ord):
    # colors_(5)
    labels=[]
    sizes=[]
    for tm in ord:
        labels.append(tm)
        sizes.append(ord[tm][0])
        print(tm, ord[tm][0])
    colors = colors_(len(labels))

    # Plot
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

def plotPieWithLegend(ord,string):
    # colors_(5)
    labels = []
    sizes = []
    for tm in ord:
        labels.append(tm)
        sizes.append(ord[tm][0])
        print(tm, ord[tm][0])
    colors = colors_(len(labels))

    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()

    plt.show()

def plotPieBar(ord,string):
    import numpy as np
    import matplotlib.pyplot as plt
    labels = []
    sizes = []
    for tm in ord:
        labels.append(tm.replace("-parscit.130908.xml",""))
        sizes.append(ord[tm][0])
        #print(tm, int(round((ord[tm][0])*100)))
    colors = colors_(len(labels))

    y_pos = np.arange(len(labels))
    plt.bar(y_pos, sizes, color=list(colorGenerator.colors_(len(labels))))
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.xticks(y_pos, labels)
    plt.title(string)
    plt.show()


