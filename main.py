from bs4 import BeautifulSoup
import re


file_name = input("Введите название файла: ")

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        pattern = r'\S+@\S+'
        emails = re.findall(pattern, soup.getText())


        for email in emails:
            print(email)

except FileNotFoundError:
    print(f"Файл '{file_name}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
