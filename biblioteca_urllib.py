'''
La biblioteca urllib se encarga de obtener el código de cualquier página web.
'''

from urllib import request

response = request.urlopen('http://google.com')
print(response.read())
