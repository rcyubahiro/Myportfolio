import requests
def get_dot_data():
    # url = "https://www.youtube.com"
    response = requests.get("https://www.youtube.com")
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
print(get_dot_data())    