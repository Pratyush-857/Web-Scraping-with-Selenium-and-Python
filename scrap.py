import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.example.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data you want
    title = soup.title.string
    print("Title:", title)

    # Find all paragraphs
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.text)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
