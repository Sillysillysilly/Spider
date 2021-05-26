from urllib import parse
import pandas as pd
import requests
import urllib

URL = "https://api.inews.qq.com/newsqa/v1/automation/country/daily/list?countrys=%s&"

headers={
    "Content-Type: application/x-www-form-urlencoded",
    "Host: api.inews.qq.com",
    "Origin: https://news.qq.com",
    "Referer: https://news.qq.com/",
}
def get_reponse(country):
    url=URL%(parse.quote(country))
    data={
        "countrys":country,
    }
    reponse = requests.post(url,data=data)
    return reponse


country = input("请输入国家：")
print(URL%(parse.quote(country)))
res= get_reponse(country)
print(res.text);

# with open("yiqing.txt","a") as f:
#     f.write(res.text)

data=res.text
data=eval(data)
data=data["data"]
data=data[country]
print(data)
df=pd.DataFrame(data)
print(df)
df.to_excel("yiqing.xls",index=False)

df=pd.read_excel("yiqing.xls",index_col=None)

