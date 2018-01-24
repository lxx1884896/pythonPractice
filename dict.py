# items0 = [['name','Tomy'],['age',42]]
# print dict(items0)
# #
# # # d = dict(name = 'Tomy',age = 42) # there is no quote
# # # print d
#
# items2= [('name','Tomy'),('age',42)]
# s=dict(items2)
# print s
# for key in s:
#     print key, s[key]
# for item in s.items():
#     print item
#
# for key, value in s.items(): # or for (key, value) in dict.items():
#     print key, value

from copy import deepcopy

# d = {}
# d['name'] = ['Alfred', 'Bertrand']
#
# c = d.copy()
# dc = deepcopy(d)
#
# d['name'].append('Clive')
#
# print c
# print dc
#
# d['name'] = 123
# print c
# print dc
# print d
#
# dict={'ba':'2','sad':'3','ba':'2','sad':'3'}
# print dict.popitem()
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    print letterGirls.setdefault(girl[0],[])
    letterGirls.setdefault(girl[0], []).append(girl)
    letterGirls.get(girl[0], []).append(girl)
    print letterGirls

