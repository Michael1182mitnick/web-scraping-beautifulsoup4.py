# web_scraping_with_beautifulsoup
# Write a Python script to scrape data from a website, parse the HTML content, and store the extracted data in a structured format like CSV or JSON.

import requests
from bs4 import BeautifulSoup
import csv
import json


def scrape_books_to_scrape():
    # URL to scrape
    url = "http://books.toscrape.com/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all book items
    books = soup.find_all("article", class_="product_pod")

    # List to store extracted book data
    extracted_data = []

    # Loop through each book and extract the title, price, and availability
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find(
            "p", class_="instock availability").text.strip()

        # Store the extracted data in a dictionary
        book_data = {
            "Title": title,
            "Price": price,
            "Availability": availability
        }

        # Add the book data to the list
        extracted_data.append(book_data)

    # Return the extracted data
    return extracted_data


def save_to_csv(data, filename="books.csv"):
    """Save extracted data to a CSV file."""
    # Define the column names
    fieldnames = ["Title", "Price", "Availability"]

    # Open a file for writing
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the rows
        for row in data:
            writer.writerow(row)

    print(f"Data saved to {filename} successfully.")


def save_to_json(data, filename="books.json"):
    """Save extracted data to a JSON file."""
    # Open a file for writing
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Data saved to {filename} successfully.")


if __name__ == "__main__":
    # Scrape data
    book_data = scrape_books_to_scrape()

    if book_data:
        # Save data to CSV
        save_to_csv(book_data)

        # Save data to JSON
        save_to_json(book_data)
