#This script allow to quickly setup kubernetes cluster on WIN10 machine. 
#Fully automated install of all nesseary software
#

from genericpath import exists
import os
import sys
import urllib.request
import subprocess

def checkInstalltionFiles():
    if exists('virutalbox.exe') and exists('kubectl.exe') and exists('minikube.exe'):
        return True
    else:
        return False

#TEMPDIR
if exists('C:\\kubelocalTemp\\'):
    os.chdir('C:\\kubelocalTemp\\')
else:    
    os.mkdir('C:\\kubelocalTemp\\')

virutalboxUrl = 'https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe'
minikubsUrl = 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe'
kubectlUrl = 'https://dl.k8s.io/release/v1.22.0/bin/windows/amd64/kubectl.exe'

if checkInstalltionFiles():
    print("Files are downloaded")
else:
    print('Downloading files from the internet')
    urllib.request.urlretrieve(virutalboxUrl, "virutalbox.exe")
    urllib.request.urlretrieve(kubectlUrl, "kubectl.exe")
    urllib.request.urlretrieve(minikubsUrl, "minikube.exe")
    if checkInstalltionFiles():
        print("Files are downloaded")
    else:
        print("Download fails")

#INSTALLATION VIRUTALBOX
print('Installing Virutalbox...')

#os.system('msiexec /i %s /qn' % "virutalbox.exe")


os.system('cmd /c "virutalbox.exe --silent --ignore-reboot"') 

#INSTALLTION KUBECTL 
print('\'Instaling\' Kubectl... ')
#Path to kubectl

#INSTALLION MINIKUBE
print('\'Instaling\' Minikube... ')
#Path to minikube


#Enjoy

print('DONE!')
