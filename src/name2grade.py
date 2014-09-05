#coding=utf8
__author__ = 'luocheng'
from collections import defaultdict

user2motion = defaultdict(lambda:0.0)
for l in open('../data/usermotion.txt').read().split('\n'):
    segs = l.strip().split('\t')
    user2motion[segs[0]] = segs[1]

fout = open('../data/id2user2tag.txt','w')
gradestat = defaultdict(lambda:0)
gradesum = defaultdict(lambda:0.0)
for l in open('../data/id2user.txt'):
    segs = l.strip().split('\t')
    id = segs[0]
    name = segs[1]
    fout.write(id+'\t'+name)
    try:
        fout.write('\t'+user2motion[id]+'\t'+str(int(float(user2motion[id]))))
    except:
        fout.write('\t'+'0.0\t'+'0')
        print id
    for i in [0,1,2,3]:
        for l in open('../data/j'+str(i)+'names.txt'):
            n = l.strip()
            if n in name:
                fout.write('\t'+str(i))
                gradestat[i] +=1
                gradesum[i]+=float(user2motion[id])
    fout.write('\n')
fout.close()

for k,v in gradestat.items():
    print k,v,gradesum[k]/gradestat[k]
fout = open('../data/id2user2tag_in.txt','w')
for  l in open('../data/id2user2tag.txt').readlines():
    if len(l.strip().split('\t'))<=4:
        pass
    else:
        fout.write(l)
fout.close()




