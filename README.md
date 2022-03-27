<img src="https://github.com/tankalxat34/tankalxat34/raw/main/readme_content/icon_googlebooks.png"/>

# PyGoogleBooks
Python package for convenient work with Google Books service

**Author: tankalxat34**

# How to use?
Create new python-file and paste here this code:
```py
import PyGoogleBooks

gb = PyGoogleBooks.GoogleBook("G1YUEAAAQBAJ", w=1280)
print(gb.name)
print(gb.authors)
print(gb.description)
print(gb.url)
print(gb.cover_link)
print(gb.get_link_to_page(page_number=5))
```

On your console you will see something like this:

```
Театр Теней Рэя Брэдбери
['Нил Гейман', 'Харлан Эллисон', 'Одри Ниффенеггер', 'Элис Хоффман', 'Джо Хилл', 'Дэйв Эггерс', 'Чарльз Ю', 'Сэм Уэллер', 'Морт Касл']
«Театр Теней Рэя Брэдбери» не просто собрание историй известных писателей – это их признание в любви, дань уважения единственному и неповторимому художнику слова Рэю Брэдбери, который подарил миру такие великие произведения, как «451 градус по Фаренгейту», «Марсианские хроники», «Вино из одуванчиков». История Нила Геймана рассказывает нам о человеке, который забыл великого мастера пера. В невероятном рассказе Джо Хилла, адаптированном Джейсоном Чарамеллой и Чарльзом Полом Уилсоном III, два подростка – Гейл и Джоэл – обнаруживают диковинное существо, и это событие, случившееся одним туманным днём у серебристых вод озера Шамплейн, навсегда изменит их жизнь. Галерею мистических событий продолжает биограф Брэдбери Сэм Уэллер в «Живи вечно!». Молодой репортёр Сэм встречается со своим кумиром и узнаёт страшную тайну...
https://books.google.ru/books?id=G1YUEAAAQBAJ
https://books.google.ru/books/publisher/content?id=G1YUEAAAQBAJ&hl=ru&pg=PP1&img=1&zoom=3&sig=ACfU3U0pF5lw0XFz8ifIXviRLY7TUPb9IA&w=1280
https://books.google.ru/books/publisher/content?id=G1YUEAAAQBAJ&hl=ru&pg=PA5&img=1&zoom=3&sig=ACfU3U1AweAPUzHHAfwFc178DohqUDQZwg&w=1280
```
