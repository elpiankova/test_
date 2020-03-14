import requests

data = {
    "title": "New New Book",
    "author": "Lev Tolstoy"
}

r = requests.post(
    "http://pulse-rest-testing.herokuapp.com/books/",
    data=data,
    headers={'User-Agent': 'my_app'}
)
print(r.status_code)
print(r.json())
# resp_body = r.json()
# print("********")
# # resp_body = json.loads(r.text)
# print(resp_body)
# print(r.status_code)
# print(r.history[0].status_code)
# print(type(r))
