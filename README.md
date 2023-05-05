# phproxy-chainer
python module for requests via multiple phproxy

# example
```py
import phproxyChainer

phproxy = phproxyChainer.phproxyChainer()
phproxy.add_chain("https://m.amv.org.mx/index.php")
phproxy.add_chain("https://www.gauvreau.fr/index.php")
print(f"{phproxy.get_chain()}")

response = phproxy.get_via_chain("https://google.com")
print(response.text)
```
