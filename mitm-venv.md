# QRadar mitmproxy python venv

Create a new virtual env:

    python3 -m venv ~/mitmproxy-venv

Activate, upgrade and install mitmproxy:

    source ~/mitmproxy-venv/bin/activate && pip install --upgrade pip setuptools ; deactivate
    source ~/mitmproxy-venv/bin/activate && pip install mitmproxy ; mitmproxy --version ; deactivate

Final output:
```
Mitmproxy: 5.3.0
Python:    3.6.8
OpenSSL:   OpenSSL 1.1.1h  22 Sep 2020
Platform:  Linux-3.10.0-1160.62.1.el7.x86_64-x86_64-with-redhat-7.9-Maipo
```
