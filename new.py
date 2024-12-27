# testing file
import requests 
 
proxies_list = open("rotating_proxies_list.txt", "r").read().strip().split("\n") 
 
def get(url, proxy): 
	try: 
		# Send proxy requests to the final URL 
		response = requests.get(url, proxies={'http': f"http://{proxy}"}, timeout=30) 
		print(response.status_code, response.text) 
	except Exception as e: 
		print(e) 
 
def check_proxies(): 
	proxy = proxies_list.pop() 
	get("http://ident.me/", proxy) 
 
check_proxies()
import requests 
 
proxies_list = open("rotating_proxies_list.txt", "r").read().strip().split("\n") 
 
def get(url, proxy): 
	try: 
		# Send proxy requests to the final URL 
		response = requests.get(url, proxies={'http': f"http://{proxy}"}, timeout=30) 
		print(response.status_code, response.text) 
	except Exception as e: 
		print(e) 
 
def check_proxies(): 
	proxy = proxies_list.pop() 
	get("http://ident.me/", proxy) 
 
check_proxies()
