from bs4 import BeautifulSoup
import requests

html = requests.get("https://books.toscrape.com/")
print(html.status_code)
soup = BeautifulSoup(html.text, 'html.parser')

# Save the HTML to a file
with open("/home/aadarsh/Desktop/Github/AI_ML_Learning_Roadmap/03_web_scraping/01_books_scraper/book_to_scrape.html", "w") as html_file:
    html_file.write(soup.prettify())

# Read it back and scrape
with open("/home/aadarsh/Desktop/Github/AI_ML_Learning_Roadmap/03_web_scraping/01_books_scraper/book_to_scrape.html", "r") as html_file:
    hot_soup = BeautifulSoup(html_file, 'html.parser')

    books = hot_soup.find_all("article", class_="product_pod")
    print(f"Found {len(books)} books\n")

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    # ✅ Open output ONCE outside the loop with "w"
    with open("/home/aadarsh/Desktop/Github/AI_ML_Learning_Roadmap/03_web_scraping/01_books_scraper/output.txt", "w") as out_file:

        for book in books:
            # --- TITLE ---
            title = book.find("h3").find("a")["title"]

            # --- PRICE ---
            price = book.find("p", class_="price_color").text.strip()

            # --- STAR RATING ---
            star_class = book.find("p", class_="star-rating")["class"][1]
            stars = rating_map[star_class]

            # --- AVAILABILITY ---
            availability = book.find("p", class_="availability").text.strip()

            # --- LINK ---
            link = "https://books.toscrape.com/" + \
                book.find("h3").find("a")["href"]

            # ✅ Write all books to same file with newlines
            out_file.write(f"Title:  {title}\n")
            out_file.write(f"Price:  {price}\n")
            out_file.write(f"Stars:  {'⭐' * stars} ({star_class})\n")
            out_file.write(f"Status: {availability}\n")
            out_file.write(f"Link:   {link}\n")
            out_file.write("-" * 50 + "\n")

            # ✅ Also print to terminal so you can see it working
            print(f"Title:  {title}")
            print(f"Price:  {price}")
            print(f"Stars:  {'⭐' * stars} ({star_class})")
            print(f"Status: {availability}")
            print(f"Link:   {link}")
            print("-" * 50)

print("\n✅ Done! Check output.txt")
