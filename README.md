# EX1-Backend-ShiranDavidov
EX1-ShiranDavidov


# http-api-demo-natalieaflalo
#### Reposetory content
In this repo there are:
1. Dockerfile and client.py file for HTTP requests that runs remotely throw https://httpbin.org/
2. localhost.dockerfile and local_client.py for HTTP requests that runs locally throw http://localhost

*This is training for EX1*

#### How to run the remote version:
1. Clone project: `git clone https://github.com/EASS-HIT-2022/http-api-demo-natalieaflalo.git`
2. Create the image: `docker build . -t remote-demo`
3. Run image: `docker run remote-demo`
4. Expected output: 
```
GET response:  {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-httpx/0.22.0', 'X-Amzn-Trace-Id': 'Root=1-62364dff-283b392f1f11729960f31a8c'}, 'origin': '77.137.75.12', 'url': 'https://httpbin.org/get'}
POST response:  {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '0', 'Host': 'httpbin.org', 'User-Agent': 'python-httpx/0.22.0', 'X-Amzn-Trace-Id': 'Root=1-62364dff-119ad0b1004f539e4010d732'}, 'json': None, 'origin': '77.137.75.12', 'url': 'https://httpbin.org/post'}
```

#### How to run the local version:
1. Clone project: `git clone https://github.com/EASS-HIT-2022/http-api-demo-natalieaflalo.git`
2. Create the image: `docker build . -t local-demo -f localhost.dockerfile`
3. Run kennethreitz/httpbin in the background: `docker run -d -p 80:80 kennethreitz/httpbin`
4. Run image using network to connect the container to the host that runs kennethreitz/httpbin: `docker run --network host local-demo`
5. Expected output:
```
GET response:  {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Host': 'localhost', 'User-Agent': 'python-httpx/0.22.0'}, 'origin': '172.17.0.1', 'url': 'http://localhost/get'}
POST response:  {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Content-Length': '0', 'Host': 'localhost', 'User-Agent': 'python-httpx/0.22.0'}, 'json': None, 'origin': '172.17.0.1', 'url': 'http://localhost/post'}
```

**Good luck!**





