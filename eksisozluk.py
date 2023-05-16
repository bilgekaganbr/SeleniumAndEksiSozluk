# Import necessary modules and packages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Initialize the Firefox browser
browser = webdriver.Firefox()

# Set the URL of the website that wanted to be scrape
url = "https://eksisozluk1923.com/mustafa-kemal-ataturk--34712?p="

# Set variables to track page and entry counts
pageCount = 1
entryCount = 1

# Define a list to store the scraped entries
entries = []

# Scrape entries from multiple pages
while pageCount <= 10:

    # Generate a random page number between 1 and 1290
    randomPage = random.randint(1, 1290)

    # Create the URL for the random page
    newUrl = url + str(randomPage)

    # Open the browser and navigate to the new URL 
    browser.get(newUrl)

    # Find all elements with the CSS class "content"
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")

    # Iterate over the found elements and extract the text
    for element in elements:

        entries.append(element.text)

    # Pause for 1 second to avoid overwhelming the website 
    time.sleep(1)
    
    # Increment the page count
    pageCount += 1

# Write the scraped entries to a file
with open("entries.txt", "w", encoding = "utf-8") as file:

    for entry in entries:

        file.write(str(entryCount) + ".\n" + entry + "\n")

        file.write("***************************\n")

        # Increment the entry count
        entryCount += 1

# Close the browser
browser.close()




