from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time

from reddit import getTopPostsToday

def getTitleScreenShot(url, filename):
    driver = webdriver.Chrome()

    # Load the website
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)  # You might need to adjust the wait time depending on your internet speed

    # Find the 'div' element directly above the title
    above_div_element = driver.find_element(By.CSS_SELECTOR, "div[slot='credit-bar']")

    # Find the title element (h1)
    post_title_element = driver.find_element(By.CSS_SELECTOR, "h1")

    # Take a screenshot of the entire page
    driver.save_screenshot("./screenShots/reddit_post_full.png")

    # Get the location and size of both elements
    above_div_location = above_div_element.location
    above_div_size = above_div_element.size

    title_location = post_title_element.location
    title_size = post_title_element.size

    # Open the full page screenshot
    image = Image.open("./screenShots/reddit_post_full.png")

    # Calculate the coordinates to crop the area including both the div and the title
    left = min(above_div_location['x'], title_location['x'])
    top = above_div_location['y']
    right = max(above_div_location['x'] + above_div_size['width'], title_location['x'] + title_size['width'])
    bottom = title_location['y'] + title_size['height']

    # Crop the area that includes both elements
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(filename)

    # Adding fake bottom
    # top_image = Image.open("./screenShots/reddit_post_title_with_div.png")
    # bottom_image = Image.open("./screenShots/reddit_vote_bottom.png")

    # width1, height1 = top_image.size
    # width2, height2 = bottom_image.size

    # # Resize the bottom image to match the width of the top image
    # if width1 < width2:
    #     bottom_image = bottom_image.crop((width2 - width1, 0, width2, height2))  # Crop from the right


    # # After cropping, check if widths are the same
    # if width1 != bottom_image.size[0]:  # Compare with the updated width of bottom_image
    #     print("width1: ", width1)
    #     print("width2: ", bottom_image.size[0])  # Get the new width after cropping
    #     raise ValueError("Images do not have the same width")
    
    # combined_height = height1 + height2
    # combined_image = Image.new('RGB', (width1, combined_height))
    # combined_image.paste(top_image, (0, 0))
    # combined_image.paste(bottom_image, (0, height1))

    # combined_image.save(filename)

    # Close the browser
    driver.quit()

post = getTopPostsToday("hypotheticalsituation", 3)
url = post[2][2]
print(url)
getTitleScreenShot(url, "./screenShots/final.png")