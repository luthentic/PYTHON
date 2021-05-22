# ARTHMETIC
# 5 / 5 float 
# 5 // 5 integer
# 5 ** 5 integer
#----------------------------------------------------------------------------------------------------------------
# INPUT
# greet = 'hello' string
# greet[0] = h
# greet[0:3] = hell

# name = input('Tell me your name:')
# name = 3 * 9 * int(name) **2
# print(name)

# num1 = 3.19495959
# num2 = 10.51204024
# format method
# print('num 1 is {0:.3} and num2 is {1:.4}'.format(num1,num2))

# age =   int(input('Enter your ages:'))
#----------------------------------------------------------------------------------------------------------------
# IF
# if age<20:
#   print('you are under 20')
# elif age == 30:
#   print('you are under 30') 
# else:
#   print('you are wise')

# LEE = ['SW','SB','SM','SY']
# for LEEE in LEE:
#   if LEEE == 'SW':
#     print(LEEE)
#     break
#   else: print(LEE)
#----------------------------------------------------------------------------------------------------------------

# WHILE
# pp = 10
# ss = 0
# while ss < pp:
#   print(ss)
#   ss += 1

#----------------------------------------------------------------------------------------------------------------
# RANGE
# for m in range(0,20):
#   print(m)

# for n in range(0,20,4):
#   print(n)

# number = ['1','2','3','4','5']
# for n in range(len(number)):
#   print(n, number[n])

# for n in range(len(number) -1, -1, -1):
#   print(n, number[n])
#----------------------------------------------------------------------------------------------------------------
#FUNCTION

# def greet(name='LEE',time='5pm'):  
#   print(f'GOOD {time} {name}, hope you well')

# name = input('name:')
# time = input('time:')
# greet(name,time)

def area(radius):
  return 3.142 * radius * radius

def vol(area,len):
  print(area * len)

radius = int(input('radius:'))
length = int(input('length:'))

vol(area(radius),length)