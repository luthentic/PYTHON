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
#LIST COMPREHNETION
# prizes = [5,10,50,100,1000]
# dbPrizes = []
# for prize in prizes:
#   dbPrizes.append(prize*2)
# print(dbPrizes)

# dbPrizes = [prize*2 for prize in prizes]
# print(dbPrizes)

# nums = [1,2,3,4,5,6,7,8,9,10]

# evennum = []
# for num in nums:
#   if num % 2 == 0:
#     evennum.append(num)
# print(evennum)

# evennum = [num for num in nums if num % 2 == 0]
# print(evennum)
#----------------------------------------------------------------------------------------------------------------
#MAP
# from random import shuffle

# def jumble(word):
#   anagram = list(word)
#   shuffle(anagram)
#   return ''.join(anagram)

# words = ['APPLE','ORAGNE','GRAPE']
# anagram = []

# # for word in words:
# #   anagram.append(jumble(word))
# # print(anagram)

# # print(list(map(jumble,words)))

# print([jumble(word) for word in words])
#----------------------------------------------------------------------------------------------------------------
#FILTER
# grades = ['A','B','F','C','F','B','F']

# def rmf(grade):
#   return grade != 'F'

# print(list(filter(rmf,grades)))

# print([grade for grade in grades if grade != 'F'])
#----------------------------------------------------------------------------------------------------------------
#LABDA
# nums = [1,2,3,4,5,6]
# print(list(map(lambda a:a*a,nums)))
#----------------------------------------------------------------------------------------------------------------
#DECORATION
# def couch_dis(fuc):
#   def wrapper():
#     print('aaacoughaaa')
#     fuc()
#     print('bbbcouchbbb')
#   return wrapper

# @couch_dis
# def question():
#   print('can you give me a discount on that?')

# question()
#----------------------------------------------------------------------------------------------------------------
# file = open('text.txt')

# for line in file:
#   print(line.rstrip())

# file.seek(50)

# lines = file.readlines(100)
# print(lines)
#----------------------------------------------------------------------------------------------------------------
#FILE WRITE
# quote = [
#   '\nI can do it whatever I want',
#   '\nWe are all the same'
# ]
# with open('text.txt','w') as writeLee:
#   writeLee.write('Hey LEE')
#   writeLee.write('\nWhat do you want?')
# with open('text.txt','a') as writeLee:
#   writeLee.writelines(quote)
#----------------------------------------------------------------------------------------------------------------
#DOWNLOAD IMAGE
import urllib.request

def image(url,file_path,file_name):
  full_path = file_path + file_name +'.jpg'

url = input('ENTER IMG URL:')
file_name = input('ENTER FILE NAME:')