<img src="https://github.com/tankalxat34/tankalxat34/raw/main/readme_content/icon_googlebooks.png"/>

# PyGoogleBooks
Python package for convenient work with Google Books service

**Author: tankalxat34**

# How to use?
Create new python-file and paste here this code:
```py
import PyGoogleBooks

gb = PyGoogleBooks.GoogleBook("buc0AAAAMAAJ", w=1280)
print(gb.name)
print(gb.authors)
print(gb.description)
print(gb.url)
print(gb.cover_link)
print(gb.get_link_to_page(page_number=5))
print(gb.get_pages(last_page_number=20, ignore_errors=True))
```

On your console you will see something like this:

```
Adventures of Sherlock Holmes
['Sir Arthur Conan Doyle']
Presenting 12 tales starring the legendary British detective Sherlock Holmes, this 1892 book is Arthur Conan Doyle&#39;s first short-story collection. The mystery compilation includes some of Holmes&#39;s finest cases with his dutiful sidekick, Doctor Watson, most notably &quot;A Scandal in Bohemia,&quot; in which Holmes matches wits with the crafty former lover of a European king. Also featured is &quot;The Adventure of the Red-Headed League,&quot; a study in misdirection that unfolds to become a much larger scheme. The stories, initially published in the Strand Magazine, are essential reading for Holmes fans.
https://books.google.ru/books?id=buc0AAAAMAAJ
https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP1&img=1&zoom=3&sig=ACfU3U2f3KG48wGY0dIFmWduClK503ONtw&w=1280
https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP5&img=1&zoom=3&sig=ACfU3U3Q2Ps0b6zInwuZwbABbYEz3b3LeA&w=1280
['https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP1&img=1&zoom=3&sig=ACfU3U2f3KG48wGY0dIFmWduClK503ONtw&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP1&img=1&zoom=3&sig=ACfU3U2f3KG48wGY0dIFmWduClK503ONtw&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP2&img=1&zoom=3&sig=ACfU3U01RzV-6aIu0MGrrEzHZAQrozv8Rw&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP3&img=1&zoom=3&sig=ACfU3U06HM0NZV1SQMNoTrUWcPLrRQc8VA&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP4&img=1&zoom=3&sig=ACfU3U1g6vMWtZuD9l9hkSMKyiYlH_UJ4A&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP5&img=1&zoom=3&sig=ACfU3U3Q2Ps0b6zInwuZwbABbYEz3b3LeA&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP6&img=1&zoom=3&sig=ACfU3U3mmAwNiygsD_C2JuC51Kq3Iwyw5g&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP7&img=1&zoom=3&sig=ACfU3U1RAlruEwGA58GirNGbrMLA2qc-dg&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP8&img=1&zoom=3&sig=ACfU3U2JFIBVBEuS9FKoP0eC9btV3pv8FQ&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP9&img=1&zoom=3&sig=ACfU3U2atbA03pfB5XJmGelBhjFrT27AUw&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP10&img=1&zoom=3&sig=ACfU3U1-TbSar4RZsKlXOvfIVbt0lBUrVQ&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP11&img=1&zoom=3&sig=ACfU3U2j_AAamXcyIyUqD4Vv4KXwvvfIdA&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP12&img=1&zoom=3&sig=ACfU3U0r-eSk6WOQ7tYNxboBVfPGD1mDrg&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP13&img=1&zoom=3&sig=ACfU3U3RcALH5OiLk-toTwXluli3fe9XRw&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP14&img=1&zoom=3&sig=ACfU3U3q65-L5vRMitbQiUaVcmhqZNWKIg&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP15&img=1&zoom=3&sig=ACfU3U33A2PJvWbTDDtY_5NCSQHZPmV09w&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP16&img=1&zoom=3&sig=ACfU3U0jO8UXw4XIcUH0pje3BvhJ6lFSxQ&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP17&img=1&zoom=3&sig=ACfU3U2PEW_I7pt66RaVY3yoNGdDIgYJJg&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP18&img=1&zoom=3&sig=ACfU3U05hN0R4D-8Sl2n3O1Br-gcWdxUbQ&w=1280', 'https://books.google.ru/books/content?id=buc0AAAAMAAJ&hl=ru&pg=PP19&img=1&zoom=3&sig=ACfU3U3GSDXF0TG1C0HehN69WK2alsBcDw&w=1280']
```
