#This script allow to quickly setup kubernetes cluster on WIN10 machine. 
#Fully automated install of all nesseary software
#
# PS>pip install requests ?
#

from genericpath import exists
import os
import sys
import urllib.request

#TEMPDIR
if exists('C:\\kubelocalTemp\\'):
    os.chdir('C:\\kubelocalTemp\\')
else:    
    os.mkdir('C:\\kubelocalTemp\\')

#LINKS 4 DOWNLOAD
virutalboxUrl = 'https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe'
minikubsUrl = 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe'
kubectlUrl = 'https://dl.k8s.io/release/v1.22.0/bin/windows/amd64/kubectl.exe'

#DOWNLOAD  -- future improvement for  & regex to reduce lines of codes + try execption
print('Downloading files from the internet')
urllib.request.urlretrieve(virutalboxUrl, "virutalbox.exe")
urllib.request.urlretrieve(kubectlUrl, "kubectl.exe")
urllib.request.urlretrieve(minikubsUrl, "minikube.exe")

if exists('C:\\kubelocalTemp\\virutalbox.exe') \
    and exists('C:\\kubelocalTemp\\kubectl.exe') \
    and exists('C:\\kubelocalTemp\\minikube.exe'):
    print('Files downloaded')
else:
    print('Files download failed!')
    exit



#INSTALLATION VIRUTALBOX


#os.system('msiexec /i %s /qn' % msi_location)



#INSTALLTION KUBECTL
#Path to kubectl

#INSTALLION MINIKUBE
#Path to minikube





