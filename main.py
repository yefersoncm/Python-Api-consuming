# vamos a realizar esta practica para consumir la api () y reforzar los conocimientos
# adquiridos previamente

import requests

if __name__ == '__main__':
	url = 'https://www.google.com.co'
	response = requests.get(url)

	if response.status_code == 200:
		content = response.content
		file = open('google.html', 'wb')
		file.write(content)
		file.close()