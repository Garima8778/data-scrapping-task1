import requests
durl = "https://httpbin.org/patch"
dheader = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
   'user-name': "['arc,'vigo]" 
}
dResp = requests.patch(url = durl,headers = dheader)
jResp = dResp.json()
print('dResp.content',jResp['headers'])