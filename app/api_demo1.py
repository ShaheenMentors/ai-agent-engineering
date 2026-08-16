import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python",
    "body": "Today I learned POST requests.",
    "userId": 1
}

response = requests.post(url, json=new_post)

data = response.json()

print("=" * 40)
print(f"Status Code : {response.status_code}")
print(f"ID          : {data['id']}")
print(f"Title       : {data['title']}")
print(f"Body        : {data['body']}")
print(f"User ID     : {data['userId']}")
print("=" * 40)