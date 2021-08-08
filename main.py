#This script allow to quickly setup kubernetes cluster on WIN10 machine. 
#Fully automated install of all nesseary software

import os
import sys
import requests

#TEMPDIR
os.mkdir('C:\\kubelocalTemp\\')
os.chdir('C:\\kubelocalTemp\\')

#LINKS 4 DOWNLOAD
virutalboxUrl = 'https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe'
minikubsUrl = 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe'
kubectlUrl = 'https://dl.k8s.io/release/v1.22.0/bin/windows/amd64/kubectl.exe'

#DOWNLOAD FILES



#INSTALLATION VIRUTALBOX


os.system('msiexec /i %s /qn' % msi_location)



#INSTALLTION KUBECTL
#Path to kubectl

#INSTALLION MINIKUBE
#Path to minikube





