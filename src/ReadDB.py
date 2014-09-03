__author__ = 'Administrator'


import json

authusers =  json.load(open('../data/auth_user.json'))
for u in authusers:
    print u['renren_id']
    attr = json.loads(u['attr'])
    print attr['name']

    print '-------------'