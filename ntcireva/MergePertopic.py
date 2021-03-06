#coding=utf8
import os
import sys
dir = sys.argv[1]
cutoff = sys.argv[2]
tag = sys.argv[3]

for f in os.listdir(dir):
    Dsharp = list()
    Irecall = list()
    D = list()
    Dsharpsum = 0.0
    Dsharpcount = 0.0
    Dsum = 0.0
    Dcount = 0.0
    
    IRel50sum = 0.0
    IRel50count = 0.0
    for l in open(dir+'/'+f):
        segs = l.strip().split(' ')
        if segs[1] == 'D#-nDCG@'+cutoff+'=':
            for item in segs[2:]:
                if item != '':
                    if float(item )<=1:
                        Dsharpsum += float(item)
                        Dsharp.append(float(item))
                    
            Dsharpcount +=1
        if segs[1] == 'I-rec@'+cutoff+'=':
            for item in segs[2:]:
                if item != '':
                    if float(item )<=1:
                        IRel50sum += float(item)
                        Irecall.append(float(item))
                        IRel50count +=1
        if segs[1] == 'nDCG@'+cutoff+'=':
            for item in segs[2:]:
                if item != '':
                    if float(item )<=1:
                        Dsum += float(item)
                        D.append(float(item))
            Dcount +=1

    if Dsharpcount==IRel50count and IRel50count==Dcount:
        print Dsharpcount,f
        if tag+'.dsharpndcg.csv' in os.listdir('.'):
            pt = open(tag+'.dsharpndcg.csv','a')
            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(Dsharp[i]))
            pt.close()
        else:
            pt = open(tag+'.dsharpndcg.csv','w')
            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(Dsharp[i]))
            pt.close()

        if tag+'.irecall.csv' in os.listdir('.'):
            pt = open(tag+'.irecall.csv','a')
            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(Irecall[i]))
            pt.close()
        else:
            pt = open(tag+'.irecall.csv','w')

            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(Irecall[i]))
            pt.close()

        if tag+'.dndcg.csv' in os.listdir('.'):
            pt = open(tag+'.dndcg.csv','a')
            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(D[i]))
            pt.close()

        else:
            pt = open(tag+'.dndcg.csv','w')
            pt.write(f.replace('.txt',''))
            for i in range(0,int(Dsharpcount),1):
                pt.write(','+str(D[i]))
            pt.close()

    else:
        print 'error'
        print f,Dsharpcount,IRel50count,Dcount
   