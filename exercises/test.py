str="a/b/c/./../d//f/"

str.replace("../","")
str.replace("./","")
str.replace("/","")

newStr=str.split()

print (newStr)