name = 'Corey'
age = 28

#greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'
#greeting = 'My name is {} and I am {} years old'.format(name, age)
greeting = 'My name is {name} and I am {age} years old'.format(name=name, age=age)

print(greeting)