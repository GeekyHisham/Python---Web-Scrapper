import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_quotes(url):
    # Request the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        response.encoding = 'utf-8'  # Ensure the response is treated as UTF-8
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = []
        authors = []

        # Find elements containing the quotes and authors
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').get_text(strip=True)
            author = quote.find('small', class_='author').get_text(strip=True)
            quotes.append(text)
            authors.append(author)

        # Check if any results were found
        if quotes and authors:
            # Save the results to a CSV file
            df = pd.DataFrame({'Quote': quotes, 'Author': authors})
            df.to_csv('quotes.csv', index=False, encoding='utf-8-sig')
            print("CSV file created successfully with the following quotes and authors:")
            print(df)
        else:
            print("No quotes found.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


if __name__ == "__main__":
    quotes_url = 'http://quotes.toscrape.com/'  # URL of the site to scrape
    scrape_quotes(quotes_url)
