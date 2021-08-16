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

#minikube dir
if exists('C:\\minikube\\'):
    os.chdir('C:\\minikube\\')
else:    
    os.mkdir('C:\\minikube\\')

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
try:
    os.system('cmd /k "virutalbox.exe --silent --ignore-reboot"') 
except:
    print("Virutalbox cmd did not run.")

#INSTALLTION KUBECTL 
print('\'Instaling\' Kubectl... ')
os.replace("C:\\kubelocalTemp\\kubectl.exe", "C:\\Windows\\System32\\kubectl.exe")
if exists("C:\\Windows\\System32\\kubectl.exe"):
    print("kubectl moved")

#INSTALLION MINIKUBE
print('\'Instaling\' Minikube... ')
os.replace("C:\\kubelocalTemp\\minikube.exe", "C:\\Windows\\System32\\minikube.exe")
if exists("C:\\Windows\\System32\\minikube.exe"):
    print("minikube moved")


userinput = str.lower(input("Type - start - for starting the minikube: "))
if userinput == 'start':
    os.system('cmd /k "minikube.exe start"') 
else: 
    print('DONE! Feel free to start you minikube with command: minikube.exe start')

#Enjoy


