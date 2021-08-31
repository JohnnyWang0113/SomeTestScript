# 公司

class Company:
    name = ''
    salary = 0
    raiseSalary = 0
    yearEndBonus = 0
    workingHousrs = 0

    def __init__(self, name, salary, raiseSalary, yearEndBonus, workingHousrs):
        self.name = name
        self.salary = salary
        self.raiseSalary = raiseSalary
        self.yearEndBonus = yearEndBonus
        self.workingHousrs = workingHousrs

    def CompanySpeak(self):
        print('PUA语句')



