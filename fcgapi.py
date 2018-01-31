from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from cookies import cookie
import requests
import re


class FcGuerrillaApi:
    
    def __init__(self):
        self.browser = RoboBrowser(history=True)
        self.browser.session.cookies.update(cookie)
        self.browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')

    class Link:
        def __init__(self, text, link, answ):
            self.link = "http://www.forocoches.com/foro/%s"%(link)
            self.text = text
            self.answ = answ


    def get_general_main(self):
        self.browser.open('https://www.forocoches.com/foro/forumdisplay.php?f=2')
        fpage = None
        fpage = self.browser.parsed
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
                            links.append(self.Link(_text,_href,_answ))
            
        return links

    def open_link(self,url):
        self.browser.open(url)
    
    def set_post(self, url, text, thread_id,securitytoken, loggedinuser):
        data = {
                'message':text,
                'wysiwyg':'0',
                'styleid':'5',
                'signature':'1',
                'fromquickreply':'1',
                's':'',
                'securitytoken':securitytoken,
                'do':'postreply',
                't':thread_id,
                'p':'who cares',
                'specifiedpost':'0',
                'parseurl':'1',
                'loggedinuser':loggedinuser,
                'ajaxqrfailed':'1'
        }
        self.browser.open(url, method='post', data=data)
    
    def get_post_data(self, url):
        self.browser.open(url)
        page =  self.browser.parsed
        soup = BeautifulSoup(str(page), 'html.parser')
        hids = None
        hids = soup.find("form",{"name":"vbform"}).find_all("input",{'type':'hidden'})
        for hid in hids:
            if hid["name"]=="securitytoken":
                securitytoken = hid["value"]
            if hid["name"]=="loggedinuser":
                loggedinuser = hid["value"]
        return securitytoken, loggedinuser

    def post_message(self, url, message):
        foo = self.get_post_data(url)
        search = re.search( r'[0-9]*$',url)
        thread_id = search.group()
        self.set_post(
                'https://www.forocoches.com/foro/newreply.php?do=postreply&t=%s'%(thread_id),
                message,
                thread_id,
                foo[0],
                foo[1])






