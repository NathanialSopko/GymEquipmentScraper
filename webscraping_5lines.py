import csv
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def export_data(data):
    with open("web_scraping_toc.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'link'])
        writer.writeheader()
        writer.writerows(data)


session = HTMLSession()
r = session.get('https://titan.fitness/collections/racks')
r.html.render(sleep=2)
productList = []
#r.html.render()
loop = True
while (loop == True):
    if r.status_code == 200:
        soup = BeautifulSoup(r.html.raw_html, "html.parser")
        notLastPage = soup.find("li", class_="paginate__itemlast")
        if(notLastPage is None):
            loop = False
        
        results = soup.find("div", id="ss__content--search")
        products = results.find_all("a", class_="full-unstyled-link c-b1")
        
        for i in range(len(products)):
            product_name = products[i].text.strip()
            product_link = 'https://titan.fitness' + products[i].get("href") #.find("a")
            productList.append({
                'name': product_name,
                'link': product_link,
            })
        
        if(loop == True):
            nextPageToLoad = 'https://titan.fitness' + notLastPage.find("a", class_="pagination__item").get("href")
            r = session.get(nextPageToLoad)
            r.html.render(sleep=2)
    else:
        print(f"Request failed with status code: {r.status_code}")
        loop = False

export_data(productList)