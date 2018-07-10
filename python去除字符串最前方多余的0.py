#a= "0001111000"

#b=str(int(a))

#print b


import re
subject = '00000000110013300'
result = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", subject)
print result
