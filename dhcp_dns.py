import fileinput
import sys
import os
from socket import *


###########	remplace des éléments	###########
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

###########	DHCP	###########
def dhcp_conf()
	os.system("apt-get install isc-dhcp-server")

	fichier = open("/etc/dhcp/dhcpd.conf","w")
	fichier.write("##### Option générale par défaut #####\n")
	fichier.write("\n### RÉSEAU #####\n")
	fichier.write("\nserver-name \""+server_name+"\";") #nom du serveur dns
	fichier.write("\nauthoritative;")
	fichier.write("\noption subnet-mask "+subnet_mask+";")
	fichier.write("\noption domain-name \""+ domain +"\";")
	fichier.write("\noption domain-name-servers "+ option_dns +";")
	fichier.write("\nddns-update-style none;")
	fichier.write("\ndefault-lease-time 3600;")
	fichier.write("\nmax-lease-time 7200;")
	fichier.write("\nlog-facility local7;\n")
###########	sous reseaux	###########
	fichier.write("\n##### RÉSEAUX #####\n")
	fichier.write("\n## Déclaration sous réseaux")	
	i=0
	for i in range(0,sous_res):
		subnet=input("Entrez le sous réseau : ")
		netmask=input("Entrez le masque : ")
		broadcast=input("Entrez le broadcast : ")
		ntp=input("Entrez le serveur ntp : ")
		routers=input("Entrez le routeur : ")
		pool=input("Entrez le pool d'adresse (ex: ip_deb ip_fin) : ")

		fichier.write("\nsubnet "+subnet+" netmask "+netmask+" {")
		fichier.write("\n  option domain-name \""+domain+"\";")
		fichier.write("\n  option broadcast-address "+broadcast+";")
		fichier.write("\n  option ntp-servers "+ntp+";")
		fichier.write("\n  option routers "+routers+";")
		fichier.write("\n  range "+pool+";")
		fichier.write("\n  ping-check = 1;")
		fichier.write("\n}\n")
	fichier.close()
	interfaces=input("Entrez les interfaces d'écoute (ex si plusieurs ens33 ens34) : ")
	replaceAll("/etc/default/isc-dhcp-server","INTERFACESv4=\"\"","INTERFACESv4=\""+interfaces+"\"")
	os.system("service isc-dhcp-server restart")

###########	DNS	###########
def dns_conf():
	os.system("apt-get install bind9")
	os.system("cp /etc/bind/db.local /etc/bind/"+domain)
		
	a = open("/etc/bind/named.conf.local","w")
	a.write("\nzone \""+domain+"\" {\n")
	a.write("	type master;\n")
	a.write("	file \"/etc/bind/"+domain+"\";\n")
	a.write("	allow-query { any; };\n")
	a.write("};")
	a.close()

	replaceAll("/etc/bind/"+domain,"localhost. root.localhost.","ns.site."+domain+". root."+domain+".")
	replaceAll("/etc/bind/"+domain,"localhost.","ns")
	replaceAll("/etc/bind/"+domain,"127.0.0.1",ip)
	replaceAll("/etc/bind/"+domain,"@	IN	AAAA	::1","ns	IN	A	"+ip)	
	f=open("/etc/bind/"+domain,"a")
	f.write("www	IN	A	"+ip)
	f.write("\nmailx	IN	A	"+ip)
	f.write("\n@	IN MX 100 mailx."+domain+".")
	f.close()
	os.system("service bind9 restart")


###########	main	###########
domain = input("Entrez le nom de domaine : ")
ip = input("Entrez l'ip du serveur dns : ")
server_name = input("Entrez le nom du serveur DHCP : ") # "dns.ubuntu-fr.lan"
subnet_mask = input("Entrez le masque : ")
option_dns = input("Entrez les options dns (si plusieurs mettez ceci ', ' entre les ip, ex : 1.1.1.1, 2.2.2.2) : ") # 192.168.100.193, 8.8.8.8, 192.168.100.252
sous_res=int(input("Entrez le nombre de sous réseaux : "))

dhcp_conf()
dns_conf()









