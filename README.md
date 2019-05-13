# Script-python-config_DHCP_DNS

Ce script permet de configuré en quelques instants un serveur DHCP et DNS et il est à lancer 
avec la commande "sudo" afin de ne pas avoir de problèmes de droits.

Au lancement du script le terminal demandera de configurer les valeurs de certaines variables
par votre nom de domaine, l'ip de votre serveur DNS, le nom du serveur DHCP, ... pour cela juste taper dans le terminal 
la valeur souhaitéé et faire "entrer"
 
Ce script fonctinne pour x sous réseaux ! En effet pour configurer les sous réseux le script rentre dans une boucle où
il pose des questions pour configurer le sous réseau (ip, masque, passerelle,...) et refais des tours de boucles 
tant que i n'est égale à au nombre de sous réseaux désirés

Par ex si vous tapez 3 lorsque le terminal vous demandera le nombre de sous réseaux
remplisser les infos pour le 1er sous réseau puis le terminal reposera les mêmes questions afin de configuré le 2e et fera la 
même chose le troisième puis sortira. 
