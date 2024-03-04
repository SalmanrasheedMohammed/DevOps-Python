# string concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result) # Hello World


# string length
s3 = "Hello world"
s3length = len(s3)
print("s3:", s3length) # s3: 11


# string uppercase and lowercase
s4 = "hello welcome to the world!"
u1 = s4.upper()
l1 = s4.lower()
print("Uppercase:", u1) # Uppercase: HELLO WELCOME TO THE WORLD!
print("Lowecase:", l1)  # Lowecase: hello welcome to the world!


# string replace
s5 = "hello world"
replace = s5.replace("hello", "Welcome")
print("s5:", replace) # s5: Welcome world


# string split
s6 = "Hello world"
words = s6.split()
print("Split words:", words) # Split words: ['Hello', 'world']


# string strip
s7 = "hello world I am good"
words = s7.strip()
print("Stripped text:", words) # Stripped text: hello world I am good
