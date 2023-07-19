# write a python program to test whether a passed letter is a vowel or not


str= input("enter letter:")
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        print(str,"is a vowel")
    else:
        print(str, "is not a vowel")