from html.parser import HTMLParser
import requests
import sys
from colorama import init, Fore, Back, Style

class parse_html(HTMLParser):
    def __init__(self):
        self.final_brow = "---Dracux Browser---   "
        self.print_data = False
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag=='title':
            self.final_brow+='*'
            self.print_data = True
        elif tag=='p':
            self.print_data = True
        elif tag=='a':
                
            self.final_brow+=Fore.RED+'<'
            self.print_data = True

    def handle_endtag(self, tag):
        if tag=='title':
            self.final_brow+='*\n\n'
        elif tag =='p':
            self.final_brow+='\n'
        elif tag == 'a':
            self.final_brow+='>'+Fore.WHITE

    def handle_data(self, data):
        if self.print_data == True:
            self.final_brow+=data
            self.print_data = False

class browse:
    def __init__(self):
        self.my_url='http://www.dracux.com'
        self.r = '<Title>Welcome to my Browser</title>'
        self.keep_going = True
    def navigate(self):
        self.my_url = input("Url: ")
        if self.my_url.upper() == 'Q':
            self.keep_going = False #TODO: this needs an url manager.
        else:
            self.r = requests.get(self.my_url)
    def get_page(self):
        parser = parse_html()
        try:
            parser.feed(self.r.text)
        except:
            parser.feed(self.r)
        print(parser.final_brow)
        self.navigate()

if __name__ == '__main__':
    use_colors = input("Use colors? Y/N: ")
    if use_colors.upper=="N":
        print("I will go all in a boring black & white")
    else:
        init()
    my_browser = browse()
    while my_browser.keep_going:
        my_browser.get_page() 