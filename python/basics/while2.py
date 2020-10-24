#!/user/bin/python 

for letter in 'Python':
    if letter == 'h':
        break
    print ('Current letter: ', letter)

var = 10
while var > 0:
    print ("Current variale value:",var)
    var = var-1
    if var== 5:
        break
print ("Good bye!")


for letter in 'Python':
    if letter == 'h':
        continue
    print ('Currrent variable value :', var)
print ("Good bye")

for letter in 'Python':
    if letter == 'h':
        pass
        print ("This is a pass block")
        continue
    print ("Current letter:", letter)
print ("Good bye!")