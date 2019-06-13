# Script-python-config_DHCP_DNS
##Présentation
Ce script permet de configurer en quelques instants un serveur DHCP et DNS et il est à lancer 
avec la commande "sudo" afin de ne pas avoir de problèmes de droits.

##Utilisation
Tout d'abourd, mettre les deux fichiers res.ini et dhcp_dns.py sur la racine puis ouvrir le fichier res.ini et 
déclarer vos sous réseaux dedans de la façon suivante (exemple pour 2 sous réseaux) :

```
[reseau0]
subnet: 10.0.0.0
netmask: 255.255.255.0
broadcast: 10.0.0.255
ntp: 10.0.0.1
routers: 10.0.0.1
pool: 10.0.0.2 10.0.0.254

[reseau1]
subnet: 10.0.0.0
netmask: 255.255.255.0
broadcast: 10.0.0.255
ntp: 10.0.0.1
routers: 10.0.0.1
pool: 10.0.0.2 10.0.0.254
```


Le script possède 2 modes : mode interactif et mode argument

### Mode interactif :
Pour lancer ce mode taper `sudo dhcp_dns.py -i`. Lors de l'exécution de ce script le terminal demandera alors de configurer les 
valeurs de certaines variables sous formes de questions (par exemple : le nom de domaine, l'ip de votre serveur DNS, ...), pour cela juste 
taper dans le terminal la valeur souhaitée et faire "entrer"

### Mode argument :
Pour lancer ce mode taper `sudo dhcp_dns.py -d <domain> -a <addr ip> -n <server name> -m <subnet mask> -o <option dns> -r <nb sous res> --interfaces=<"interface1 interface2 or_more">`.
Avec ce mode les valeurs des variables sont mentionnées par arguments.
#### Paramètres
```
-h : aide 
-i : lancer le mode interactif
-d : rentrer votre nom de domaine dns (ex : mondomaine.net)
-a : rentrer votre adresse IP (ex : 10.0.1.2)
-n : rentrer votre nom de serveur dhcp (ex : ubuntu.lan)
-m : rentrer votre masque pour le serveur (ex : 255.255.255.0)
-o : rentrer les options dns (ex : 8.8.8.8,1.1.1.1)
-r : rentrer le nombre de sous réseau que vous avez configuré dans le fichier res.ini si vous mettez pas le bon des sous réseau ne 
seront pas configuré !
```
