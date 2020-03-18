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
try:
    purchased = opinion.find("div", "product-review-pz").string
except IndexError:
    purchased = None
dates = opinion.find("span", "review-time").find_all("time")
review_date = dates.pop(0)["datetime"]
try:
    purchase_date = dates.pop(0)["datetime"]
except IndexError:
    purchase_date = None
useful = opinion.find("button", "vote-yes").find("span").string
useless = opinion.find("button", "vote-no").find("span").string
content = opinion.find("p", "product-review-body").get_text()
try:
    pros = opinion.find("div", "pros-cell").find("ul").get_text()
except IndexError:
    pros = None
try:
    cons = opinion.find("div", "cons-cell").find("ul").get_text()
except IndexError:
    cons = None

print(opinion_id, recomendation, stars, author, pros, cons, useful, useless, purchased, purchase_date, review_date)


