from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from cookies import cookie

browser = RoboBrowser(history=True)
browser.session.cookies.update(cookie)
browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')

class Link:
    def __init__(self, text, link, answ):
        self.link = "http://www.forocoches.com/foro/%s"%(link)
        self.text = text
        self.answ = answ


def get_links():
    browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')
    fpage = None
    fpage = browser.parsed
    soup = BeautifulSoup(str(fpage), 'html.parser')
    trs = None
    trs = soup.find_all("tr")
    links=[]
    for tr in trs:
        if 'class="alt1"' in str(tr):
            soup2 = BeautifulSoup(str(tr), 'html.parser')
            foo = soup2.find_all("a")
            _text,_answ= None, None
            for link in foo:
                if 'href="showthread.php?t=' in str(link) and 'id="thread_title' in str(link):
                    
                    _text = link.text
                    _href = link['href']
            
                    _pos= str(tr).find('Respuesta')
                    if _pos != -1:
                        bar = str(tr)[_pos:_pos+25].split(',')
                        j = bar[0][11:]
                        _answ = j
                    if _text != None and _answ != None:
                        links.append(Link(_text,_href,_answ))
        
    return links

print(get_links())
for link in get_links():
    print(link.text, link.answ)

