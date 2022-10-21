import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "c194238432msh2f6a82117a32918p10cff4jsn385be31864bb",
    'X-RapidAPI-Host': "api-nba-v1.p.rapidapi.com"
    }

conn.request("GET", "/seasons", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



 const submit = document.querySelector('button[type="submit"]');