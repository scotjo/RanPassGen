import random
import sys
import os

def PWChar(aa,bb):
    #sys.stdout.write(str(chr(random.randrange(aa,bb))))
    return (str(chr(random.randrange(aa,bb))))

PWLen = input ("Password Length:")
ChrList = [PWChar(97,122),PWChar(48,57),PWChar(65,90)]

RandSpecChar = random.randrange(1,32)
if RandSpecChar <= 15:
    ChrList.append(PWChar(33,47)) #15
elif RandSpecChar > 15 and RandSpecChar < 23:
    ChrList.append(PWChar(58,64)) #7
elif RandSpecChar > 22 and RandSpecChar < 29:
    ChrList.append(PWChar(91,96)) #6
else:
    ChrList.append(PWChar(123,126)) #4

for x in range(0, PWLen-4):
    ChrList.append(PWChar(33,126))

for x in range(0, 10):
    PW = random.sample(ChrList, PWLen)
    print ('{}'*len(PW)).format(*PW)
