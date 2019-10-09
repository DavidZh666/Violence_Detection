import os
import random

train=0.7
test=0.15
val=0.15


def split(list):
    nameno=os.listdir(list[0])
    namefight=os.listdir(list[1])
    random.shuffle(nameno)
    random.shuffle(namefight)

    nametrain=nameno[0:int(len(nameno)*train)]
    nametest=nameno[int(len(nameno)*train):int(len(nameno)*(test+train))]
    nameval=nameno[int(len(nameno)*(test+train)):len(nameno)]

    nametrain=nametrain+namefight[0:int(len(nameno)*train)]
    nametest=nametest+namefight[int(len(namefight)*train):int(len(namefight)*(test+train))]
    nameval=nameval+namefight[int(len(namefight)*(test+train)):len(namefight)]

    random.shuffle(nametrain)
    random.shuffle(nametest)
    random.shuffle(nameval)

    return (nametrain,nametest,nameval)

if __name__=="__main__":
    list = ["/nfs30/daves/datasets/ourdatas/Train/fight/", "/nfs30/daves/datasets/ourdatas/Train/no/"]
    (nametrain,nametest,nameval)=split(list)
    with open("trainlist40_0.txt",'w') as f:
        for name in nametrain:
            f.write(name + '\n')
    with open('testlist40_0.txt','w') as f:
        for name in nametest:
            f.write(name+'\n')
    with open("vallist40_0.txt",'w') as f:
        for name in nameval:
            f.write(name+'\n')
