import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

product_names = []
product_prices = []
product_rates = []
product_links = []

search_input = input('What product do you search for? ')
url = f'https://www.amazon.ae/s?k=amazon+uae+{search_input}&crid=20TRJ2648LYRO&sprefix=amazon+uaela%2Caps%2C296&ref=nb_sb_ss_ts-doa-p_1_12'
result = requests.get(url)

src = result.content
soup = BeautifulSoup(src,'lxml')


products = soup.find_all('div',class_="sg-col-inner")

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
            """print(f"Product Name: {product_name}")
                print(f"Product Price: {product_price}")
                print(f"Product Rate: {product_rate}")
                print(f"Product Link: {product_link}")
                print('_____________________')
            """    
        except:
            pass  

def create_csv_file():
    list_file = [product_names,product_prices,product_rates,product_links]
    exported = zip_longest(*list_file)
    with open("items_found.csv", "w",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["product name","product price","Rates","product link"])
        writer.writerows(exported)
    print("CSV File created!")    
    
    
if __name__ == '__main__':
    get_product_info()
    create_csv_file()