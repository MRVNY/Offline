# Offline

Vidéo: https://youtu.be/Z544BtdbaLk 
GitHub: https://github.com/MRVNY/Offline.git

Apres le lancement, l'utilisateur doit choisir un fichier txt qui contient les trames, l'analyseur va ensuite separer les trames 
en fonction de l'offset
Lors d'une analyse de trame, l'analyseur va d'abord séparer les differents octets valides et les mettres dans un tableau 
chaque case du tableau contient deux characteres qui representent l'octet en binaire
ensuite avec ce tableau il separe et analyse les différents champs et les associe, si il y a la possibilité, leurs valeurs
Si les champs ne sont pas complets cela provoque des erreurs et l'utilisateur doit choisir à nouveau un autre fichier valide.

Structure :
main(offline.py) qui apelle la classe Ethernet
Les fonctions sont contenu dans le ficher function.py
La classe Trame sert pour l'interface graphique et est contenue dans le fichier gui.py
output.txt est la sortie 
nos trames de test sont contenue dans le dossier ressource (rsrc)

Ethernet() appelle Ipv4() si le champ EtherType est a 0x0800
Ipv4 appelle tcp() si le champ protocol est a 0x06
tcp() appelle http() si dans les 20 premiers octet de data du tcp il y a "HTTP"
Toutes les fonctions ci dessus renvoient un couple (out:String ,title:String)
out est un string qui stocke toutes les données de l'analyse (Champs et valeurs)
title est une string qui stocke l'information sur l'intitulé de la trame (lors du choix de la trame a afficher)

Quelques options tcp et ipv4 sont implementés