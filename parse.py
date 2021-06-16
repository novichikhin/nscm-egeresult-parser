import requests
from bs4 import BeautifulSoup

class Parser:
    __url = 'http://nscm.ru/egeresult/tablresult.php'

    __results = []

    def __init__(self, lastname, name, idnomer):
        data = {
            'Lastname': lastname,
            'Name': name,
            'idnomer': idnomer
        }

        html = self.__get_html(data)
        self.__parse_html(html)

    def get_results(self):
        return self.__results
        
    def __get_response(self, data):
        # headers?
        response = requests.post(self.__url, data=data)
        return response

    def __get_html(self, data):
        response = self.__get_response(data)
        response.encoding = 'utf-8'

        return response.text

    def __parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table_tab_result = soup.find('table', {'class':'tab_result'})
        tbody = table_tab_result.find('tbody')
        for tr in tbody:
            tds = tr.find_all('td')
            tmp_result = {
                'subject': tds[0].text,
                'date': tds[1].text,
                'score': tds[2].text
            }
            self.__results.append(tmp_result)