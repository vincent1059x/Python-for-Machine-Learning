my_string= 'I\'m living in \'Ho Chi Minh\' city'
print(my_string)
char=my_string[-1]
print(char)
sub_string=my_string[::2]
print(sub_string)
greeting="Hello Xin Chao Cac Ban"
channel="Vincent Le Channel"
sentence = greeting + " Chao Mung Cac ban den voi " + channel
print(sentence)
my_string= ['Xin', 'Chao', 'Cac', 'Ban']
sentence = ' '.join(my_string)
print (sentence)

if "X" in sentence:
    print("yes")
else:
    print("No")

print("   I am alone    ".strip())
print ("on an island".strip('o'))

print("but life is good".split('life'))

print("Help me".replace("me", "you"))
     

my_string = 'Need to make a fire'
print(my_string.count("e"))

name = "codexplore"
pi=3.14
heights =10.65
my_string = f"I am {pi:.5f} pi; height is {heights}"
print(my_string)

presidents = ["Washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Adams", "Jackson"]

for index, name in enumerate(presidents, start=1):
    print(f"President {index}: {name}")