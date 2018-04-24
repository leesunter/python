'''
Created on 23 Apr 2018

@author: s258115
'''
import argparse #we'll need to parse the arguments. which we'll feed to the script itself (argparse).
import base64 #We will need the base64 library to save the images within a JSON file (base64 and json)
import json #We will need the base64 library to save the images within a JSON file (base64 and json)
import os #open files for writing (os).
from bs4 import BeautifulSoup #for scraping the web page easily
import requests #to fetch its content. requests is an extremely popular library for performing HTTP requests, built to avoid the difficulties and quirks of using the standard library urllib module. It's based on the fast urllib3 third-party library.
# pip install beautifulsoup4 requests


# --------- TO RUN --------------
# FOLDER C:\Users\S258115\OneDrive\OneDrive - Atos\workspace\Python\python1\src\root\UI\simple_server> 
# COMMAND python -m http.server 8000
# NAVIGATE http://localhost:8000/



    
    
    
# --- Business logic ---
def scrape(url, format_, type_):
    try:
        page = requests.get(url) # fetch the page at the given url argument.
    except requests.RequestException as rex:
        print(str(rex)) # wrap and print the error
    else:
        # BeautifulSoup library allows us to parse a web page in no time
        soup = BeautifulSoup(page.content, 'html.parser') 
        images = _fetch_images(soup, url)
        images = _filter_images(images, type_)
        _save(images, format_)

# looping through all of the images found on the page and filling in the 'name' and 'url'
# information about them in a dictionary (one per image). All dictionaries are added to
# the images list, which is returned at the end.
def _fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = (
            '{base_url}/{src}'.format(
                base_url=base_url, src=src))
        # split the img_url string using '/' as a separator, and take the last item as the image name.
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
        # use as a debug and get [{'url': 'http://localhost:8000/img/owl-alcohol.png', 'name': 'owlalcohol.
        # png'}, {'url': 'http://localhost:8000/img/owl-book.png', 'name': 'owl-book.png'}, ...] etc
        print(images)
        return images    
    
    
    
def _filter_images(images, type_):
    if type_ == 'all':
        return images
    # allowed extensions from the ext_map dictionary, and use it to filter the images in the list
    ext_map = {
        'png': ['.png'],
        'jpg': ['.jpg', '.jpeg'],
        }
    return [
        img for img in images
        if _matches_extension(img['name'], ext_map[type_])
    ]
    
#split the name of the image getting its extension and checking whether it is within the list of allowed ones    
def _matches_extension(filename, extension_list):
    name, extension = os.path.splitext(filename.lower())
    return extension in extension_list

def _save(images, format_):
    # if not empty
    if images:
        if format_ == 'img':
            _save_images(images)
        else:
            _save_json(images)
        print('Done')
    else:
        print('No images to save.')
        
#loop on the images list and for each dictionary we find there we perform a GET request on the image URL 
# and save its content in a file, which we name as the image itself
def _save_images(images):
    for img in images:
        img_data = requests.get(img['url']).content
        # Python's with statement supports the concept of a runtime context defined
        # by a context manager. This is implemented using a pair of methods
        # (contextmanager.__enter__() and contextmanager.__exit__(exc_type,
        # exc_val, exc_tb)) that allow user-defined classes to define a runtime context that
        # is entered before the statement body is executed and exited when the statement ends
        # using a context manager, in conjunction with the open function, gives us
        # the guarantee that if anything bad were to happen while writing that file, the resources
        # involved in the process will be cleaned up and released properly regardless of the error
        with open(img['name'], 'wb') as f:
            f.write(img_data)
            # When we open a file, we get a handler for it and, no matter what happens, we want
            # to be sure we release it when we're done with the file. A context manager is the tool
            # we need to make sure of that

def _save_json(images):
    # fill in the data dictionary. The image name is the key, and the
    # Base64 representation of its binary content is the value. When we're done populating
    # our dictionary, we use the json library to dump it in the images.json file.
    data = {}
    for img in images:
        img_data = requests.get(img['url']).content
        b64_img_data = base64.b64encode(img_data)
        str_img_data = b64_img_data.decode('utf-8')
        data[img['name']] = str_img_data
    with open('images.json', 'w') as ijson:
        ijson.write(json.dumps(data))
        
        
        
        
        
# --- Argument parsing and scraper triggering ---
# Look at that first line; it is a very common idiom when it comes to scripting.
# According to the official Python documentation, the string '__main__' is the name
# of the scope in which top-level code executes. A module's __name__ is set equal to
# '__main__' when read from standard input, a script, or from an interactive prompt
# when importing it from another module, __name__ won't be '__main__'
# When you run the script directly, like we're going to, __name__ will be '__main__', so the execution logic will run
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')
    parser.add_argument(
        '-t',
        '--type',
        
        choices=['all', 'png', 'jpg'],
        default='all',
        help='The image type we want to scrape.')
    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'],
        default='img',
        help='The format images are saved to.')
    parser.add_argument(
        'url',
        help='The URL we want to scrape for images.')
    args = parser.parse_args() #order to parse all the arguments
    scrape(args.url, args.format, args.type)
    
# python scrape.py http://localhost:8000
# python scrape.py -t png http://localhost:8000
# python scrape.py --type=png -f json http://localhost:8000        