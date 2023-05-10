import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

product_names = []
product_prices = []
product_rates = []
product_links = []

search_input = input('What product do you search for? ')
for i in range(1,3):       
    url = f'https://www.amazon.ae/s?k=amazon+uae+{search_input}&page={i}&crid=B658EMFNLJMZ&qid=1683745577&sprefix=amazon+uae+laptop%2Caps%2C716&ref=sr_pg_2'
    result = requests.get(url)
    #print(result)

    src = result.text
    soup = BeautifulSoup(src,'lxml') 
    box = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")
    #print(box)
    products = box.find_all('div',class_="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")


    def get_product_info():
        for product in products:
            try:
                product_name = product.find('h2',class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4").text
                product_names.append(product_name)
                product_price = product.find('span',class_="a-price-whole").text
                product_prices.append(product_price)
                product_rate = product.find('span',class_="a-icon-alt").text.strip()
                product_rates.append(product_rate)
                product_link = product.find('a',class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").get('href')
                product_link = "https://www.amazon.ae" + str(product_link)
                product_links.append(product_link)
            except:
                pass  
            

    def create_csv_file():
        
        list_file = [product_names,product_prices,product_rates,product_links]
        exported = zip_longest(*list_file)
        with open("items_found.csv", "w",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Names","Product Prices","Product Rates","Product links"])
            writer.writerows(exported)
         
        print("CSV File created!")    
        
    
if __name__ == '__main__':
    get_product_info()
    create_csv_file()
    