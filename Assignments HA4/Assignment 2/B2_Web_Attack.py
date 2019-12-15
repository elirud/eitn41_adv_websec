import requests

hex_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

url_base = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"

name = 'Kalle'
grade = '5'
parameters = {'name': name, 'grade': grade}

result = requests.get(url_base, params=parameters)
