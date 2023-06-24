# import urllib
# import urllib.request
#
# try:
#     site = urllib.request.urlopen('https://www.google.com.br/')
# except urllib.error.URLError:
#     print('erro')
# else:
#     print('sucesso')
import webbrowser
try:
    webbrowser.open('https://www.google.com.br')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print('Conseguir abrir com sucesso a página do google')
