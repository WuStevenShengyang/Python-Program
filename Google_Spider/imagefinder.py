from html.parser import HTMLParser
from urllib import parse
from urllib import request

class ImageFinder(HTMLParser):
    def __init__(self, base_url):
        super().__init__()

        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for (attribute, value) in attrs:
                if attribute == 'src':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        
    def get_link(self):
        return self.links
        
    
    def error(self, message):
        pass
