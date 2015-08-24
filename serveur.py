# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:14:52 2015

@author: Simon
"""

import socket
hote=''
port=12800
connexion_principale=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_principale.bind((hote,port))
connexion_principale.listen(5)
#connexion_principale.setblocking(0)
print("Le serveur ecoute sur le port {}".format(port))

connexion_client, infos_connexion = connexion_principale.accept()

msg_recu=b""
while msg_recu != b"fin":
    msg_recu = connexion_client.recv(1024)
    print(msg_recu.decode())
    connexion_client.send(b"5/5")
    
print("Fermeture de la connexion")
connexion_client.close()
connexion_principale.close()
