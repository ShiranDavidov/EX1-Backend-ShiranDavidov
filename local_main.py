import httpx

get_response = httpx.get("http://localhost/get")

post_response = httpx.post("http://localhost/post")

print("GET response: ",get_response.json())

print("POST response: ",post_response.json())