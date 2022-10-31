from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        ''' this function responsible to send a request for a REST Countries API to get a country of 
        selected capital and vice versa '''
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        if 'country' in dictionary:
            country=dictionary['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            capital=str(data[0]['capital'][0])
            the_capital =f'The capital of {country} is {capital}.' 


        elif 'capital' in dictionary:
            capital=dictionary['capital']
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data = r.json()
            country=str(data[0]['name']['common'])
            the_capital =f'{capital} is the capital of {country}.'

       
 
        else:
            the_capital = "Enter the name of country or the name of capital "



        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        self.wfile.write(the_capital.encode())
        return