# http://www.xuanshu.com/
import requests

# resp = requests.get('http://www.xuanshu.com/')
resp = requests.get('http://www.xuanshu.com/sort/1.html')
print(resp.text)
