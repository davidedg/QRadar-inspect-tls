# QRadar mitmproxy chroot bundle

On a temporary Linux machine (Ubuntu latest will do fine):

    docker pull mitmproxy/mitmproxy
    docker run --entrypoint /bin/true --name mitmproxy_export mitmproxy/mitmproxy
    docker export mitmproxy_export > mitmproxy.tar
    docker rm mitmproxy_export

Use `scp` to transfer `mitmproxy.tar` to QRadar host and then unpack it in `~/mitmproxy`
\
You should be able to run:
```
chroot ~/mitmproxy mitmproxy --version
Mitmproxy: 10.2.1
Python:    3.11.7
OpenSSL:   OpenSSL 3.1.4 24 Oct 2023
Platform:  Linux-3.10.0-1160.95.1.el7.x86_64-x86_64-with-glibc2.31
```
