'''
Created on 16 Apr 2018

@author: s258115
'''
from tkinter import *
from tkinter import ttk, filedialog, messagebox #new set of styled widgets, capable of drawing themselves correctly according to the style your OS
import base64
import json
import os
from bs4 import BeautifulSoup
import requests
# pip install beautifulsoup4 requests
# check UI available  package by running python - m tkinter

# --------- TO RUN --------------
# FOLDER C:\Users\S258115\OneDrive\OneDrive - Atos\workspace\Python\python1\src\root\UI\simple_server> 
# COMMAND python -m http.server 8000
# NAVIGATE http://localhost:8000/


# --- Fetching the web page ---

# config dictionary. We need some way of passing data between the GUI application
# and the business logic. Now, instead of polluting the global namespace with many different variables,
# so have a single dictionary that holds all the objects we need to pass back and forth,
# we have one single, clean, easy way of knowing where all the objects that are needed by our application
config = {}
# it's much better to try and leave the global namespace as clean as we can

# The fetch_url function is quite similar to what we did in the script. Firstly, we get
# the url value by calling _url.get(). Remember that the _url object is a StringVar
# instance that is tied to the _url_entry object, which is an Entry. The text field
# you see on the GUI is the Entry, but the text behind the scenes is the value of the
# StringVar object.
def fetch_url():
    # By calling get() on _url, we get the value of the text which is displayed in _url_entry.
    url = _url.get()
    # prepare config['images'] to be an empty list, and to empty the _images variable, which 
    # is tied to _img_listbox. This, of course, has the effect of cleaning up all the items in _img_listbox.
    config['images'] = []
    _images.set(()) # initialized as an empty tuple
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        # _sb is a helper function that sets the text in the status bar for us.
        _sb(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        # call the fetch the images function
        images = fetch_images(soup, url)
        # if found set value and update status bar
        if images:
            # If we have images, using tuple comprehension (which is a generator expression fed to a tuple constructor)
            _images.set(tuple(img['name'] for img in images))
            _sb('Images found: {}'.format(len(images)))
        else:
            _sb('No images found')
        # we update config['images'] to hold the images list. So we can access the images from other 
        # functions by inspecting config['images'] without having to pass that list around    
        config['images'] = images
        
# looping through all of the images found on the page and filling in the 'name' and 'url'
# information about them in a dictionary (one per image). All dictionaries are added to
# the images list, which is returned at the end.        
def fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = (
            '{base_url}/{src}'.format(base_url=base_url, src=src))
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
    return images

# --- Saving the images ---

# user clicks the Scrape button, the save function is called using the callback
def save():
    # check if any images to save
    if not config.get('images'):
        _alert('No images to save')
        return
    # list is not empty, save acts as a dispatcher according to which value is held by _same_method
    # Remember, this variable is tied to the radio buttons, therefore we expect its value to be either 'img' or 'json'.
    if _save_method.get() == 'img':
        # We need to ask the user to choose a directory and assigning the result of the call to dirname.
        # directory we choose must exist
        dirname = filedialog.askdirectory(mustexist=True)
        # then SAVE IMAGES
        _save_images(dirname)
    else:
        # We ask the user to choose a filename, and example is given and filetypes argument. It is a list 
        # with any number of 2-tuples (description, extension) 
        filename = filedialog.asksaveasfilename(
            initialfile='images.json',
            filetypes=[('JSON', '.json')])
        # then SAVE JSON
        _save_json(filename)
        
# We check on both dirname and the presence of at least one image in config['images'].    
def _save_images(dirname):
    if dirname and config.get('images'):
        for img in config['images']:
            img_data = requests.get(img['url']).content
            # join the directory (which means the complete path) to the image name, by means of os.path.join.
            # In the os.path module there's plenty of useful methods to work with paths and filenames.
            filename = os.path.join(dirname, img['name'])
            with open(filename, 'wb') as f:
                f.write(img_data)
        _alert('Done')
        
# Create a JSON object from a Python dictionary (data) that we populate with key/value pairs 
# and Base64 encoded content made by the images check at the beginning that makes sure that 
# we don't proceed unless we have a file name and at least one image to save name ensures that
# if the user presses the Cancel button, nothing bad happens
def _save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data
        with open(filename, 'w') as ijson:
            ijson.write(json.dumps(data))
        _alert('Done')



# --- Alerting the user ---
def _sb(msg):
    # to change status bar we access _status_msg StringVar, as it's tied to the _status label
    _status_msg.set(msg)

def _alert(msg):
    # we can trigger a message box
    messagebox.showinfo(message=msg)
    # The messagebox object can also be used to warn the user (messagebox.showwarning) or to signal
    # an error (messagebox.showerror). Can be used to provide dialogs that ask us if we're sure that 
    # we want to proceed or if we really want to delete that file etc
    # Inspect messagebox by simply printing out what dir(messagebox) returns,
    # you'll find methods like askokcancel, askquestion, askretrycancel, askyesno,
    # and askyesnocancel, as well as a set of constants to verify the response of the user,
    # such as CANCEL, NO, OK, OKCANCEL, YES, YESNOCANCEL, and so on. You can compare
    # these to the user's choice so that you know what the next action to execute when the dialog closes

# --- Argument parsing and scraper triggering ---

# Look at that first line; it is a very common idiom when it comes to scripting.
# According to the official Python documentation, the string '__main__' is the name
# of the scope in which top-level code executes. A module's __name__ is set equal to
# '__main__' when read from standard input, a script, or from an interactive prompt
# when importing it from another module, __name__ won't be '__main__'
# When you run the script directly, like we're going to, __name__ will be '__main__', so the execution logic will run
if __name__ == "__main__":
    _root = Tk() # main window instance of TK
    _root.title('Scrape app') #use the prepending underscore technique for all the names of the tkinter objects, in order to avoid potential collisions with names in the business logic.

    _mainframe = ttk.Frame(_root, padding='5 5 5 5') # a ttk.Frame instance set its parent and padding
    # place this _mainframe on the first
    # row (0) and first column (0) of the parent object (_root). We also say that this frame
    # needs to extend itself in each direction by using the sticky argument with all
    # four cardinal directions. If you're wondering where they came from, it's the from tkinter import *
    _mainframe.grid(row=0, column=0, sticky=(E, W, N, S)) # grid locations 
    
    # not just a simple Frame, but it's actually a LabelFrame, which means we can set the text argument and
    # expect a rectangle to be drawn around it
    _url_frame = ttk.LabelFrame(
    _mainframe, text='URL', padding='5 5 5 5')
    _url_frame.grid(row=0, column=0, sticky=(E, W)) # grid locations 
    # use rowconfigure and columnconfigure to make sure it behaves correctly, should it need to resize
    _url_frame.columnconfigure(0, weight=1)
    _url_frame.rowconfigure(0, weight=1)
    
    _url = StringVar()
    # text to set the URL variable/field 'text'
    _url.set('http://localhost:8000')
    # Entry is the data ENTRY field with a staringVar (url)
    _url_entry = ttk.Entry(
        _url_frame, width=40, textvariable=_url)
    # place in corner then sticky for if resized etc and add padding
    _url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)
    # BUTTON 
    _fetch_btn = ttk.Button(
       _url_frame, text='Fetch info', command=fetch_url)
        # means that when we click this button, we actually call the fetch_url function
    _fetch_btn.grid(row=0, column=1, sticky=W, padx=5)
     
    # second row the images list
    _img_frame = ttk.LabelFrame(
        _mainframe, text='Content', padding='9 0 0 0')
    _img_frame.grid(row=1, column=0, sticky=(N, S, E, W))
    
    _images = StringVar()
    _img_listbox = Listbox(
        _img_frame, listvariable=_images, height=6, width=25)
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)
    # Scrollbar instance. Note that, when we
    # instantiate it, we set its command to _img_listbox.yview. This is the first half
    # of the contract between a Listbox and a Scrollbar. The other half is provided
    # by the _img_listbox.configure method, which sets the yscrollcommand=_
    # scrollbar.set.
    # By providing this reciprocal bond, when we scroll on Listbox, the Scrollbar will
    # move accordingly and vice-versa, when we operate the Scrollbar, the Listbox will
    # scroll accordingly
    _scrollbar = ttk.Scrollbar(
        _img_frame, orient=VERTICAL, command=_img_listbox.yview)
    _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    _img_listbox.configure(yscrollcommand=_scrollbar.set)
    
    # Radio Frame, ready to be populated. Note that the Listbox is occupying (0, 0)
    # on _img_frame, the Scrollbar (0, 1) and therefore _radio_frame will go in (0, 2).
    _radio_frame = ttk.Frame(_img_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))
    
    _choice_lbl = ttk.Label(
        _radio_frame, text="Choose how to save images")
    _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    _save_method = StringVar()
    _save_method.set('img')
    # Radiobutton is also driven by a bond to an external variable, _save_method
    # Image only radio button
    _img_only_radio = ttk.Radiobutton(
        _radio_frame, text='As Images', variable=_save_method,
            value='img')
    _img_only_radio.grid(
        row=1, column=0, padx=5, pady=2, sticky=W)
    _img_only_radio.configure(state='normal')
    # json only radio button
    _json_radio = ttk.Radiobutton(
        _radio_frame, text='As JSON', variable=_save_method,
            value='json')
    _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky=W)
    
    # third row of _mainframe we place the Scrape button. Its command is save, which saves 
    # the images to be listed in Listbox, after we have successfully parsed a web page
    _scrape_btn = ttk.Button(
        _mainframe, text='Scrape!', command=save)
    _scrape_btn.grid(row=2, column=0, sticky=E, pady=5)
    
    # give it a little status bar effect we set its relief property to 'sunken'
    # and give it a uniform padding of 2 pixels. It needs to stick to the _root window left,
    # right and bottom parts, so we set its sticky attribute to (E, W, S)
    _status_frame = ttk.Frame(
        _root, relief='sunken', padding='2 2 2 2')
    _status_frame.grid(row=1, column=0, sticky=(E, W, S))
    _status_msg = StringVar()
    # place a label in it and, this time, we tie it to a StringVar object, because we
    # will have to modify it every time we want to update the status bar text. 
    _status_msg.set('Type a URL to start scraping...')
    _status = ttk.Label(
        _status_frame, textvariable=_status_msg, anchor=W)
    _status.grid(row=0, column=0, sticky=(E, W))

    # Finally, on the last line, we run the application by calling the mainloop method on the Tk instance.
    _root.mainloop()