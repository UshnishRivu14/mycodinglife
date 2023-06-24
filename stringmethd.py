a = 'Ushnish'
print(a)
# converting string to upper case 
print(a.upper())
#converting string to lower case
print(a.lower())

#removing  white spaces before and after the string
str2 = " space white "
print(str2.strip())
#string all special characters like !,@
str1 = 'Hello !!'
print(str1.rstrip("!"))

str3 = 'My name is ushnish rivu , actually its ushnish sarkar'
print(str3.replace('rivu','Sarkar'))

#spilting a string 
#it converts a string elements into lists
str4 = "Hello every one"
print(str4.split(" "))

#capetalize an steing's first letter to capital
srt5 = "welcome everyone to my blog"
print(srt5.capitalize())

#Count moves a string to the middle 
strr = "Welcome to the console!!"
print(strr.center(50))
print(strr.center(50,'.'))
 #checks how many times a value is repeated in a string
st = 'My name is ushnish rivu , actually its ushnish sarkar'
print(st.count("ushnish"))

# Checks whether a stringm ends with it or not
gh = "welcome to the console !!!"
print(gh.endswith("!"))
print(gh.endswith('to',4,10))

#find() a value index
hgk = 'His name is dan'
print(hgk.find('dan'))

#index() gives the index or position of a value ina  string
print(hgk.index("name"))

#isalnum() checks whether a value is alphanumeric or not
a = "WelcomeToTheConsole"
print(a.isalnum())

#isalpha() checks whether a string contains only characters A-Z, a-z or not
ds = 'Welcome978'
print(ds.isalpha()) 

#islower() checks whether a string is of lower case or not
hd = 'hello world'
print(hd.islower())

#isprintable() whether a string is printable or not
isp = 'hello everyone\n'
print(isp.isprintable())

#isspace() chceks whether a string contains only of white space or not
dhs = '     '
print(dhs.isspace())

#istitle() checks whether the first letter of every word in a string is of capital or not
w = 'Welcome To the Console'
print(w.istitle())

#isupper() checks whether a string is of all upper case or not 
f = "HELLO HOW R U"
print(f.isupper())

#startwith() checks whether a string starts with a vakue or not
h = '---Welcome==='
print(h.startswith('-'))

#swapcase() changes upper to lower case and vice versa
i = 'Welcome Everyone to My blog'
print(i.swapcase())

#title() changes each first letter of the word to upper case
k = "he's name is dan. he is a honest man."
print(k.title())