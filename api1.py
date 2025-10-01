import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.status_code)
data = response.json()
print(data["id"])
print(data['title'])





url2="https://jsonplaceholder.typicode.com/posts"
new_post={
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response2=requests.post(url2,json=new_post)
print(response2.status_code)
print(response2.json())


headers = {
    'Content-type': 'application/json; charset=UTF-8',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}