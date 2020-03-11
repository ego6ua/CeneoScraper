#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL przykladowej strony z opiniami
url = 'https://www.ceneo.pl/78803054#tab=reviews'

#poranie kodu html strony z podanego URL
page_respons = requests.get(url)
page_tree = BeautifulSoup(page_respons.text, 'html.parser')

#wydobycie z kodu HTML strony fragmentow odpowiadajacych poszczegolnym opiniom
opinions = page_tree.find_all("li", "js_product-review")


#wydobycie skladowych dla pojedynczej opinii
opinion = opinions.pop()


opinion_id = opinion['data-entry-id']
author = opinion.find("div", "reviewer-name-line").string
recomendation = opinion.find("div", "product-review-summary").find("em").string
stars = opinion.find("span", "review-score-count").string
purchased = opinion.find("div", "product-review-pz").string
#- opinia: li.review-box
#- identyfikator: li.review-box['data-entry-id']
#- autor: div.reviewer-name-line
#- rekomendacja: div.product-review-summary > em
#- gwiazdki: span.review-score-count
#- potwierdzona zakupem: div.product-review-pz



#- data wystawienia: span.review-time > time['datetime'] - pierwszy element listy
#- data zakupu: span.review-time > time['datetime'] - drugi element listy
useful = opinion.find("button", "vote-yes").find("span").string
useless = opinion.find("button", "vote-no").find("span").string
content = opinion.find("p", "product-review-body").get_text()
print(opinion_id, author, recomendation, useful, useless, content, stars)
#- przydatna: span[id=^votes-yes]
#             button.vote-yes['data-total-vote']
#             button.vote-yes > span
#- nieprzydatna: span[id=^votes-no]
#                button.vote-no['data-total-vote']
#                button.vote-no > span
#- treść: p.product-review-body
#- wady: div.cons-cell > ul
#- zalety: div.pros-cell > ul


