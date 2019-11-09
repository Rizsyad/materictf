from Crypto.Util.number import inverse
from lxml import html
import requests

def factor_db_p(x):
	target = 'http://factordb.com/index.php'
	Params = {'query':x}
	page = requests.get(url=target, params=Params)
	tree = html.fromstring(page.content)
	p = tree.xpath('//font[@color="#000000"]/text()')
	return p[0]
	
def factor_db_q(x):
	target = 'http://factordb.com/index.php'
	Params = {'query':x}
	page = requests.get(url=target, params=Params)
	tree = html.fromstring(page.content)
	q = tree.xpath('//font[@color="#000000"]/text()')
	return q[1]
           

n = int(input("input N: "))
c = int(input("input c: "))
e = int(input("input e: "))

print("1. p belum diketahui")
print("2. q belum diketahui")
print("3. p dan q belum diketahui")
choice = int(input("Pilih menu: "))

if choice == 1:
	q = int(input("input q: "))
	p = n/q
elif choice == 2:
	p = int(input("input p: "))
	q = n/p
else:
	p = int(factor_db_p(n))
	q = int(factor_db_q(n))

	
phi = ((p-1)*(q-1))
d = inverse(e, phi)
m = pow(c,d,n)
print(hex(m)[2:-1]).decode('hex')

