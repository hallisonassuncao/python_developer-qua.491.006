# TODO  crie um programa que mostre a hora atual sempre sendo atualizado a cada segundo

import os
import time
import datetime

# declaração de variaveis 
hora = datetime.datetime.now().strftime("%H:%M:%S")
                                        
# exibir a hora atual                                     
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(time.strftime("%H:%M:%S"))  
    time.sleep(1)  
