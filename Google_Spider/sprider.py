import urllib
from imagefinder import ImageFinder
import random
import os


class Spider:
    base_url = ''
    project_name = ''
    
  
    def __init__(self, content):
        Spider.base_url = 'https://www.google.com/search?'

        self.search_content = {'hl':'en', 'tbm':'isch', 'source':'hp', 'q':content, 'op':content, 'safe':'active', 'ssui':'on'}
        self.search_content = urllib.parse.urlencode(self.search_content, 'utf-8')
        Spider.base_url += self.search_content
      
        
    def parse(self):
        html_string = ''
        header = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
        req = urllib.request.Request(Spider.base_url, headers = header)

        resp = urllib.request.urlopen(req)
        html_byte = resp.read()
        html_string = html_byte.decode("utf-8")
        
        image_finder = ImageFinder(Spider.base_url)
        image_finder.feed(html_string)

        self.link = image_finder.get_link()

    def write_image(self):
        folder_name = 'Result'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        for hl in self.link:
            full_name = str(random.randint(1,1000)) + '.jpg'
            
            urllib.request.urlretrieve(hl, folder_name + '/' + full_name)

content = input('Google  search:\n')

spider = Spider(content)
spider.parse()
spider.write_image()

