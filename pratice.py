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

# def area(radius):
#   return 3.142 * radius * radius

# def vol(area,len):
#   print(area * len)

# radius = int(input('radius:'))
# length = int(input('length:'))

# vol(area(radius),length)

#----------------------------------------------------------------------------------------------------------------
#VARIABLE SCOPE
# my_name = 'LEE'

# def print_name():
#   global my_name
#   my_name = 'KIM'
#   print('The name is',my_name)

# print_name()
# print('The name outside of function is', my_name)
#----------------------------------------------------------------------------------------------------------------

#DICTIONARIES
# belt = {'1':'red','2':'pink','3':'white','4':'yellow'}
# print(belt)
# print(belt['1'])
# print(belt['2'])
# print('6' in belt)
# print('3' in belt)
# print(belt.keys())
# print(belt.values())
# belt['5'] = 'green'
# print(belt)

# def loop(dic):
#   belts = list(dic.values())
#   for belt in set(belts):
#     num = belts.count(belt)
#     print(f'There are{num},{belt}belts')

# belts = {}

# while True:
#   name = input('enter name:')
#   color = input('enter color:')
#   belts[name] = color

#   check = input('Countinue? (y/n)')
#   if check == 'y':
#     continue
#   else:
#     break

# loop(belts)
#----------------------------------------------------------------------------------------------------------------

#CLASS
class Planet:
  shape = 'round'

  def __init__(self,name,radius,gravity,system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'
  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape}'
  @staticmethod
  def spin(speed='2000 mile per hour'):
    return f'The speed and spins at {speed}'

hoth = Planet('LEE',20000,5.6,'HOHOHO')
print(f'Name is:{hoth.name}')
print(f'Radius is:{hoth.radius}')
print(f'Gravity is:{hoth.gravity}')
print(hoth.orbit())
print(Planet.commons())
print(Planet.spin('1000 miles'))
#----------------------------------------------------------------------------------------------------------------

