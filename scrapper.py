import os
import re
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def sanitize_image_url(url):
    # Remove query parameters and fragments from the URL
    match = re.search(r'(https?://[^?]+)', url)
    if match:
        return match.group(1)
    return url

def is_valid_image_url(url):
    # Basic validation for image URLs
    return url.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'))

def fetch_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(delay)
    return None

def download_image(url, folder):
    try:
        sanitized_url = sanitize_image_url(url)
        response = fetch_with_retry(sanitized_url)
        if response:
            img = Image.open(BytesIO(response.content))
            img = img.resize((32, 32))  # Resize image to 32x32 pixels
            file_extension = sanitized_url.split('.')[-1]
            file_name = f"{os.path.basename(sanitized_url).split('?')[0].split('#')[0]}"
            img_path = os.path.join(folder, file_name)

            img.save(img_path)
            return img_path
        else:
            print(f"Failed to fetch image after retries: {url}")
            return None
    except Exception as e:
        print(f"Failed to process image from URL {url}: {e}")
        return None

def scrape_images(urls, folder='data/images'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img', src=True)
        for tag in img_tags:
            img_url = tag['src']
            if img_url and is_valid_image_url(img_url):
                img_path = download_image(img_url, folder)
                if img_path:
                    print(f"Downloaded {img_path}")


# Example usage
if __name__ == '__main__':
    # List of URLs to scrape
    image_urls = [
        'https://media.istockphoto.com/id/1594523005/photo/mental-trauma.webp',
        'https://media.istockphoto.com/id/1561991852/photo/cobwebs-against-black-wall-in-the-background.webp',
        'https://media.istockphoto.com/id/1483625643/photo/human-hands-silhouette-behind-frosted-glass.webp',
        # Add more URLs as needed
    ]

    scrape_images(image_urls, 'data/images')
