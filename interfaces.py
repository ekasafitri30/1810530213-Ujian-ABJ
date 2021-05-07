print("UTS APLIKASI BERBASIS JARINGAN - 1810530213")
print('='*40)


file=open("db-interfaces.txt","a")
while True :
    Answer = input("Input Data Trunk baru [yes/no] : ")
    if Answer == "yes" :
        print('-'*34)
        HostnameSwitch= input ("Masukkan Hostname Switch: ")
        Name          = input ("Masukkan Nama  Interface: ")
        
        print('-'*34)
        file.write('Hostname Switch  : '+HostnameSwitch+',' 'Name : '+Name+'\n')
    else :
        print('='*34)
        print('-'*13 +'  DONE  '+'-'*13)
        print('='*34)
        file=open('db-interfaces.txt','r')
        for item in file:
            item=item.strip()
            print(item)
        file.close()
        break
print('='*34)
file.close()
