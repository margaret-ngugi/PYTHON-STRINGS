# A string is a data structure in Python that represents a 
#sequence of characters.
#strings are immutable,once defined you cannot change it value

#we can also access characters from string using indexing
x="magdaline"
print(x[3])

#find string length ,returns the length of a string
a = "margaret wairimu!"
print(len(a))

#looping through a string
b="I am from Kenya"
for x in b:
    print(x)

#finding a phrase in a string,we use in keyword,returns true 
#if the text contains string
c="I love travelling to various places"
print("travelling" in c)

#slicing strings
#using the range indexing,,it does not include the last position
d ="school"
print(d[1:3])

#slice from start
e = "AkiraChix"
print(e[:3])  #extracts characters from start to third position#3 not included

#slice to end
f="margaret"
print(f[2:]) #extracts characters from 2 position to the end

#negative indexing
g ="magdaline"
print(g[-5:-1])

#modifying strings
#converting a string to various cases
#e.g
s="arguments"
print(s.upper())#upper converts all characters in a string to uppercase

s1="parameters"
print(s.title())#converts the first letters of each word to upperCase

#removing white space
#strip() ,removes space from the beginning or end
s2 ="My school is called Kio"
print(s2.strip())

#string concantenation,combining or joining two or more strings together
# using the + operator
s3 = "My name is ann"
s4 = "I love reading"
s5 = s3+s4
print(s5)

#formating strings
#format()
#The format() method takes the passed arguments, formats them, and 
#places them in the string where the placeholders {} are:
age = 40
txt = "my name is faith,and I am {}"
print(txt.format(age))


#string methods
#isnumeric(),true if all characters are numeric/numbers
n1 = "I am 12 years old"
print(n1.isnumeric())

#isdigit(),true if all characters are digits
n2 = "123"
print(n2.isdigit())

#index(),returns the index position of a given character in a string 
#returns an error if the character does not exist in the string
n3 = "Nyahururu"
print(n3.index("y"))


#find,returns the index position of a qiven character in a string
#returns false -1 if the character does not exist

n4 = "paradise"
print(n4.find("f")) #returns -1 since the character does not exist in the string.

#count(),returns the number of occurences of a qiven character in a string
t ="My name is ann."
print(t.count("n"))


#replace(),replace all the occurences of a givencharacter in a string
r = "wairimu"
print(r.replace("i","o"))



#quizz
#write the name welcome two times
str1 = 'Welcome'
print(str1*2)#In the case of a string, the * operator is used to repeat a string.

#Extract the string from[:6]
str1 = 'Welcome'
print (str1[:6] + ' PYnative')
#explation
#The + operator is used for concatenating.
#To get a substring from the original string, we can use a slice [], operator.

#convet the following string to lowerCase
st = "She loves dancing"
print(st.lower())  #converts all characters in a string to lowerCase

#convert he following interger into a string

number = 78
print(str(number)) #str() method converts an integer to a string


#My key takeaways are:
#I have learned the different methods we use in strings.
#We can be able to access characters from a string,find length,replace and also convert a string to different cases
#A string is a data structure in Python that represents a 
#sequence of characters.It is immutable




    
