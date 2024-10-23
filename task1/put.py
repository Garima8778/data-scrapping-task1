import requests
durl = "https://httpbin.org/put"
dheader = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
   'user-name': "['arc,'vigo]" 
}
dResp = requests.put(url = durl,headers = dheader)
jResp = dResp.json()
print('dResp.content',jResp['headers'])

string= "['arc,vigo]"
list_from_string = requests.literal_eval(string)
result_list = requests.literal_eval(string)
print(result_list)