print("All about Identifier and variables in python")

'''
Dynamically typed lanaguge so we do not need to give any data type of variable it will dynamically allocate the space depends type of value we put (class)
'''
name='Vivek'
NAME="Shubham"
age =24
print("Data type of name variable : ",type(name),type(age))

# Case Sensetive - > variable are case sensitive since its hold each id while exicuting the program 

print ("address for the variable are differnat evern name of variable is same " ,id(name),id(NAME))

# we can able to use the reserver key word as variable or identifer in coding since it has specifc meaning 
# example if elif else id help def for while in range import etc there are 32 reserve keyword by python that we cant use it in our laguage
import keyword
x=list((keyword.kwlist))
print(len(x))
