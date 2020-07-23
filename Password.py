import requests
import hashlib
def final(data,five2,tail3):
    new_=five2+tail3
    flag=0
    hashes=[line.split(':') for line in data.splitlines()]
    for h,count in hashes:
        if h==tail3:
            print("Password found!!!")
            print("Password repeated",count,"times.")
            flag=1
            break
    if flag==0:
        print("Password not found.")
        print("This password is safe for use.")
      


def request_api(query_data,tail2):
    url="https://api.pwnedpasswords.com/range/"+query_data
    res=requests.get(url)
    final(res.text,query_data,tail2)

def passw(password):
    sha1pass=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    five,tail=sha1pass[:5],sha1pass[5:]
   # print(sha1pass)
    request_api(five,tail)



PASSWORD=input("Enter password:")       
passw(PASSWORD)
 

