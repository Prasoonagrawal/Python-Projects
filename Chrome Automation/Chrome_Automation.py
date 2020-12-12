import webbrowser as web
URLS=[]

def open_site():
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    for u in URLS:
        print("opening:"+u)
        web.get(chrome_path).open(u)



URLS=input("Enter URL: ").split()
print(URLS)
open_site()
