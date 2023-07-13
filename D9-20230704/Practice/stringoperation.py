text="string methods"
print(text.capitalize())

text1="String Methds"
print(text1.casefold())

string="Hello python"
print(string.center(50))

txt="My name is stale"
# enc=txt.encode()
# print(enc)
print(txt.find("name"))

txt="H\te\tl\tl\to"
x=txt.expandtabs(3)
print(x)

msg="My name is {name}"
print(msg.format(name="Abi"))
txt1="I am {} years old".format(21)
print(txt1)

fruit="Apple"
print(fruit.index("l"))

strng="Abi15"
print(strng.isalnum())
print(strng.isalpha())
print(strng.isascii())