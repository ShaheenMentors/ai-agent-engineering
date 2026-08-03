import requests

response = requests.get("http://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.text)

params = {
    "userId": 1,
    "id": 20
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.url)