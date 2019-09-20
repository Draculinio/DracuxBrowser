from html.parser import HTMLParser
import requests
import sys
from colorama import init, Fore, Back, Style

class parse_html(HTMLParser):
    def __init__(self):
        self.final_brow = "---Dracux Browser---            "
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
        elif tag=='input':
            for attr in attrs:
                if attr[0]=='type':
                    if attr[1]=='text':
                        self.final_brow+=Back.WHITE+'__________________'+Back.BLACK+'\n'
            #print(attrs)

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

    def get_url(self,url):
        self.final_brow += Fore.BLUE+url+Fore.WHITE+"      "

class browse:
    def __init__(self,initial_url):
        self.my_url=initial_url
        self.r = '<Title>Welcome to my Browser</title>'
        self.keep_going = True
    def navigate(self):
        if self.my_url.upper() == 'Q':   #first commands
            self.keep_going = False #TODO: this needs an url manager.
        else:   #Other things
            if '.' not in self.my_url:
                self.my_url = 'http://www.duckduckgo.com/?q='+self.my_url

            elif self.my_url[0:4]!="http":
                self.my_url = "http://www."+self.my_url
            try:
                self.r = requests.get(self.my_url)
            except:
                print("Site Does not exist")
    def set_url(self):
        self.my_url = input("Url: ")
    def get_page(self):
        parser = parse_html()
        parser.get_url(self.my_url)
        try:
            parser.feed(self.r.text)
        except:
            parser.feed(self.r)
        print(parser.final_brow)
        self.set_url()
        self.navigate()
        

if __name__ == '__main__':
    colors= False
    initial_url="http://www.dracux.com"
    #managing arguments
    if len(sys.argv)>1:
        if sys.argv[1].upper()=='C': #C argument starts with color
            print("COLOR")
            colors=True
        elif sys.argv[1]!=None:
            initial_url=sys.argv[1]
    #end of managing arguments
    if colors==False:
        use_colors = input("Use colors? Y/N: ")
        if use_colors.upper()=="N":
            colors = False
            print("I will go all in a boring black & white")
        else:
            colors = True
            init()
    else:
        init()
    my_browser = browse(initial_url)
    my_browser.navigate()
    while my_browser.keep_going:
        my_browser.get_page()