# 8th note
#print("hi, " + "please tell me your name and I will say its length : ")
name = input("hi, " + "please tell me your name and I will say its length : \n")
length = len(name)
print("Your name is " + name + " and its length is")
print(length)
#print(name + length) #TypeError: can only concatenate str (not "int") to str
# print("Your name is " + name + " and its length is") and print(length) cannot 
# be concatenated since they are different data types