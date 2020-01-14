"""
Copyright @ Author: Liaoyuan Wang
bug report or feedback or suggestion: wly_ustc@hotmail.com
"""
from datetime import datetime as dt
class caldate:
#  def __init__(self):
#    self.date = dt.date(dt.today())

  def age(self, dobstr): 
    self.txt = dobstr
    self.dob = dt.date(dt.strptime(self.txt,'%m/%d/%Y'))
    self.date = dt.date(dt.today())
    self.tmp = self.date - self.dob
    self.dltstr = str(self.tmp)
    self.dltdays = self.dltstr.split(' ')[0]
    self.age = round(float(self.dltdays)/365,2)
#    print("The difference is ",self.dltdays,".\nThe age is ",self.age,".\n")
    return self.age

  def agestr(self, dobstr):
    self.txt = dobstr
    self.dob = dt.date(dt.strptime(self.txt,'%m/%d/%Y'))
    self.date = dt.date(dt.today())
    self.tmp = self.date - self.dob
    self.dltstr = str(self.tmp)
    self.dltdays = self.dltstr.split(' ')[0]
    self.age_years = int(int(self.dltdays)/365)
    self.age_days = int(self.dltdays) - self.age_years * 365
    self.age = str(self.age_years) + 'y' + str(self.age_days) + 'd'
    return self.age

  def days(self, DateStart, DateEnd):
    self.startday = dt.date(dt.strptime(DateStart,'%m/%d/%Y'))
    self.endday = dt.date(dt.strptime(DateEnd,'%m/%d/%Y'))
    self.tmp = self.endday - self.startday
    self.dltstr = str(self.tmp)
    self.days = int(self.dltstr.split(' ')[0])
    return self.days
