import os
import webbrowser
urls = ['url1', 'url2']
browser = webbrowser.get()
for url in urls:
    browser.open(url)