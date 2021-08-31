import linecache
import random


# 公司
class Company:
    name = ''
    salary = 0
    raiseSalary = 0
    yearEndBonus = 0
    workingHousrs = 0

    def CompanySpeak(self):
        print('boss:'+'You are screwed if you quit')


# 个人
class Staff:
    name = ''
    age = 0
    hopeSalary = 0
    hopeRiseSalary = 0
    anger = 0

    def staffSperk(self):
        print('staff:'+'sorry,boss...')


# 对话函数
def convercation():
    hs = Company()
    wang = Staff()
    wang.anger = '100'
    hs.CompanySpeak()
    wang.staffSperk()



convercation()
