#🐍Python Web Load Balancer

A small web load balancer I built to learn how requests can be shared between multiple web servers.

The load balancer listens on port **8080** and forwards each GET request to one of two backend servers. It uses round-robin routing, so requests are sent to each server in turn.

## How it works

```text
Browser → Load balancer (port 8080) → Backend server 1 (port 9001)
                                    → Backend server 2 (port 9002)
```

## Requirements

- Python 3

This project uses Python’s standard library, so it does not need additional packages.

🪟## Run it on Windows

Open three terminals in the project folder.

In the first terminal, start backend server 1:

```powershell
python backend.py server-1 9001
```

In the second terminal, start backend server 2:

```powershell
python backend.py server-2 9002
```

In the third terminal, start the load balancer:

```powershell
python balancer.py
```

Then open [http://localhost:8080](http://localhost:8080) in your browser. Refresh the page to see responses from the backend servers.

## Project files

- `balancer.py` — receives requests and forwards them to backend servers in turn.
- `backend.py` — runs a small backend server and displays its name in the response.

## What I learned

- How a reverse proxy receives and forwards web requests.
- How round-robin routing distributes requests across servers.
- How multiple local web servers can run on different ports.

This is a learning project. It currently handles GET requests and uses a fixed list of two local backend servers.
