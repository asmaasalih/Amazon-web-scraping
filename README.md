# Amazon_web_scrapping
This project is a Python script that scrapes product data from Amazon using the BeautifulSoup library. The scraped data is stored in a CSV file.

![image of csv file of results](img.png)
## Installation
To use this script, you will need to have Python 3 installed on your machine. You can install it from the Python website.

You will also need to install the following Python libraries:

BeautifulSoup4
requests
pandas
You can install these libraries by running the following command:

Copy code
`pip install beautifulsoup4 requests pandas`
## Usage
To use the script, run the following command:

Copy code
python main.py
The script will prompt you for a search term (e.g. "laptop") and the number of pages of results to scrape (e.g. 3). It will then scrape the product data for the specified number of pages and save it to a CSV file named results.csv.

The CSV file will contain the following columns:

- Product name
- Product price
- Product rating
-Number of reviews
### Contributing
If you have any suggestions or find any bugs, please open an issue or submit a pull request.


