import requests

response = requests.get("https://catfact.ninja/fact")
print(response.status_code)

data = response.json()
print("Cat Fact:, data['fact]")