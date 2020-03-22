from requests import get
from bs4 import BeautifulSoup
import json

class currentStat:
    data_set = []
    response_rcvd = True
    exception_occrd = False
    def __init__(self):
        try:
            url = 'https://www.mohfw.gov.in/'
            response   = get(url)
            if response.ok:
                html_soup  = BeautifulSoup(response.text, 'html.parser')
                span_list  = html_soup.find_all('span', class_ = 'icount')[1:-1]
                for item in span_list:
                    self.data_set.append(int(item.text))
            else:
                self.response_rcvd = False
        except:
            self.exception_occrd = True

    def getCurrentStatus(self):
        if self.response_rcvd:
            if not self.exception_occrd:
                return self.data_set
            else:
                print "Exception Occured at Scrapy"
                return None
        else:
            print "Response not Fetched"
            return None
