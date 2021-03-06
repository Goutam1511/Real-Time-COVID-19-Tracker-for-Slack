from requests import get
from bs4 import BeautifulSoup
import json

class currentSituation:
    data_set = {}
    response_rcvd = True
    exception_occrd = False
    def __init__(self):
        try:
            url = 'https://www.mohfw.gov.in/'
            response   = get(url)
            if response.ok:
                html_soup  = BeautifulSoup(response.text, 'html.parser')
                table_body = html_soup.find_all('tbody')[1]
                tr_list    = table_body.find_all('tr')

                for i in tr_list:
                    td_list = i.find_all('td')
                    if len(td_list) == 6:
                        state, indian, foreign, cured, died = td_list[1:]
                        state   = str(state.text)
                        indian  = int(indian.text)
                        foreign = int(foreign.text)
                        cured   = int(cured.text)
                        died    = int(died.text)
                        self.data_set[state] = [indian, foreign, cured, died]
                    if len(td_list) == 5:
                        total_cases_text, indian, foreign, cured, died = td_list
                        total_cases_text = str(total_cases_text.text)
                        indian  = int(indian.text)
                        foreign = int(foreign.text)
                        cured   = int(cured.text)
                        died    = int(died.text)
                        self.data_set[total_cases_text] = [indian, foreign, cured, died]
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
