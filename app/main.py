import httpx

get_response = httpx.get("https://httpbin.org/get")

post_response = httpx.post("https://httpbin.org/post")

print("GET response: ",get_response.json())

print("POST response: ",post_response.json())