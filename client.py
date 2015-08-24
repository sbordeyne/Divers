# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:20:20 2015

@author: Simon
"""

import socket

hote='localhost'
port=12800
connexion_serveur=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote,port))
print("Connexion etablie sur le port {}".format(port))

msg_send=b""
while msg_send !=b"fin":
    msg_send=input("> ")
    msg_send=msg_send.encode()
    connexion_serveur.send(msg_send)
    msg_recu=connexion_serveur.recv(1024)
    print(msg_recu.decode())

print("Fermeture de la connexion")
connexion_serveur.close()