# import requests

# response = requests.get("http://api.open-notify.org/astros")
# print(response.status_code)
import requests
import json
import webbrowser

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    data = response.json()
    return data[0]['url']

def main():
    cat_image_url = get_random_cat_image()
    print("Here's a random cat image for you:")
    print(cat_image_url)
    webbrowser.open(cat_image_url)

if __name__ == "__main__":
    main()