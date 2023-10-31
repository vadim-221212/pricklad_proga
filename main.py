from bs4 import  BeautifulSoup
import re


with open('html_doc.html','r',encoding='utf-8') as file:
    html_content=file.read()

soup=BeautifulSoup(html_content,'html.parser')

pattern=r'\S+@\S+'
emails=re.findall(pattern,soup.getText())


for email in emails:
    print(email)
