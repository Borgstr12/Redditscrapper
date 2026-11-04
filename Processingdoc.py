from bs4 import BeautifulSoup as bfs
import NOTTHEAPI
with open("scrappingsform.html") as BS:
 walloftext = bfs(BS,'html.parser');

tag = walloftext.body
print(tag.attrs)
firstchild = tag.find(id = "page")
secondchild = firstchild.find(id ="hockey")
thirdchild = secondchild.find(class_ = "container")
fourthchild = thirdchild.find(class_ = "table")

list = fourthchild.find_all(class_="year",string = True)
k = 0
text = ""
for i in list:
    k+=1
    text = i.get_text(strip = True)
    NOTTHEAPI.wordprinter(k,text)

   
   
        