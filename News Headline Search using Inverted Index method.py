import requests as req
from bs4 import BeautifulSoup

#words list
list_words = [];
#documents related to words
list_word_doc = [];
#original documents
list_docs = [];

def parse(text):
    docNumber = len(list_docs);
    list_docs.append(text)
    list_word_doc.append([])
    allwords = text.lower().split(' ');
    for item in allwords:
        if item != '':
            if item not in list_words:
                list_words.append(item)
                list_word_doc.append([])
                index  = list_words.index(item)
            index  = list_words.index(item)
            if docNumber not in list_word_doc[index]:
                list_word_doc[index].append(docNumber)
def search(text, orand):
    texts = text.lower().split()
    tempList=[]
    for t in texts:
        if t != '':
            if t in list_words:
                index  = list_words.index(t)
                tempList.append(list_word_doc[index])


    if len(tempList) ==0:
        return [];
    if orand == 'and':
        founded = set(tempList[0]);
        for s in tempList[1:]:
            founded.intersection_update(s)


    if orand == 'or':
        founded = set([]);
        for s in tempList:
            founded.update(s)

    return list(founded)
def printdocs(li):
    print('tedad yaft shode: ' + str(len(li)) )
    for i in li:
        print("news number#" +str(i+1) +': ' + list_docs[i])

url = 'https://www.enet.ie/news.html'
r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
mydivs = soup.select(".NewsSummaryLink")
for item in mydivs:
    h3 = item.select('h3');
    atag = h3[0].select('a');
    parse(atag[0].text)
    
 

while True:
    print("\n\n")
    print("#1)serach with 'or'")
    print("#2)serach with 'and'")
    print("#0)exit")
    s = input()
    if s == '1':
        text = input('\n\rsearch text:')
        f = search(text, 'or')
        printdocs(f)
    if s == '2':
        text = input('\n\rsearch text:')
        f = search(text, 'and')
        printdocs(f)
    if s == '0':
        break;
