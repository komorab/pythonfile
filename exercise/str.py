#to start the learing of python about string
#coding = utf-8
import json
import os

agent = ["alice", "bob", "cynthia", "david", "ethan"]
'''
the exercise of list; include pop del reverse title "sum" "max" "min" and so on
agent.append("evian")
i = 6
while i:
    if len(agent) > 2:
        absent = agent.pop()
        print("i'm sorry to "+absent.title())
        i -= 1
    else:
        absent = agent.pop()
        print("welcome " + absent + " to my party!")
        i -= 1
long = len(agent)
print(agent)
'''

'''for magic in agent:
    print(magic.title()+", it's a brilliant show")
print("Thanks for everyone")'''

'''
#about list
square = [var ** 3 for var in range(1, 21)]
print(str(min(square))+' ' + str(max(square))+' ' + str(sum(square)))
def three(lis):
    'to find the number could be divided 3 in list'
    count = len(lis)
    while count:
        if square[count - 1] % 3 == 0:
            count -= 1
        else:
            del square[count - 1]
            count -= 1
    return lis
square = three(square)
copy = square[:]
square.append(3)
print(square)
print(copy)
print(square == copy)
'''

'''
tuple
dimensions = tuple(range(1,11))
print(dimensions[:])
lis1 = list(range(1, 11))
tup1 = (lis1, 20)
lis1.append(100)
print(tup1)
'''

'''
students = agent[:]
scores = [88, 79, 93, 73, 98]
rank = {}
for count in range(5):
    rank[students[count]] = scores[count]
print(rank)
for key, value in rank.items():#否则默认读取key
    print(key + " " + str(value))
'''

'''
name = input('Please input your name: ')
score = int(input('Please input your score: '))
'''

'''
#function
def get_rank(name, score, light=1):
    dic = {}
    dic['name'] = name
    dic['score'] = score
    dic['light'] = light
    return dic
print(get_rank('alice', 88))
'''

class Subject:
    """to simulate subject in school"""
    def __init__(self, score_c:int, score_m:int, score_e:int):
        self.score_c = score_c
        self.score_m = score_m
        self.score_e = score_e

    def chinese_score(self):
        return self.score_c

    def math_score(self):
        return self.score_m

    def english_score(self):
        return self.score_e

my_score = Subject(102, 112, 88)
print(my_score.chinese_score())
