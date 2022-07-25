#Crie um código em python que teste se o site Pudim está acessivel pelo computador
import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mSEM CONEXÃO\033[m')
else:
    print('\033[32mSITE ACESSIVEL\033[m')
    