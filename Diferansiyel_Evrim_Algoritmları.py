#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:28:55 2022

@author: barisbalci
"""

import math
from random import random

#İTERASYON SÜRECİ
 
for dongu in range(0,durma_kriteri):
    
#BAŞLANGIÇ MATRİSİNDEN RASSAL OLARAK ÜÇ FARKLI ÇÖZÜMÜN SEÇİLMESİ
     for kr in random(0,nc):
         
         p=math.ceil(random()*nc)
         q=math.ceil(random()*nc)
         r=math.ceil(random()*nc)
         
#X1yeni: X1 tasarım değişkeni için mutasyona uğrayan (yeni) aday çözüm değeri
#X2yeni: X2 tasarım değişkeni için mutasyona uprayan (yeni) aday çözüm değeri

       X1new = OPT[0][p]+F*(OPT[0][q]-OPT[0][r])
       X2new = OPT[1][p]+F*(OPT[1[]q]-OPT[0][r])
       ......
      
        
#ÇAPRAZLAMA AŞAMASI 
       rand_kr=math.ceil(random()*nc)
       
       if(random()<=CR) or (kr==rand_kr)
           X1=X1new
           X2=X2new
      ......
     
      else:
          X1=OPT[0][kr]
          X2=OPT[1][kr]
          
#iterasyon sonu 
#değer : tüm iterasyonlar sonucunda elde edilen en iyi çözümün amaç fonksiyonu değeri
#sıra: güncellenen OPT matrisinde bu çözümü yer aldığı vektör 

deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])

