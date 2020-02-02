# -*- coding:utf-8 -*-
# Copyriht (C) AddyXiao@msn.cn  <addyxiao@msn.cn>
#
#

" A test of property"

class clsStudent(object):
    __slots__=("__name","__age","__score")  #限定为内部属性

    def __init__(self,name="AddyXiao",age=46,score=98.00):
        if not isinstance(name,str):
            raise TypeError("Student Object.name, name must be a string!")
        self.__name=name

        if not isinstance(age,int):
            raise TypeError("Student Object.age, age must be a integer!")
        self.__age=age
    
        if not isinstance(score,float):
            raise TypeError("Stduent Object.score.score, score must be a float!")
        self.__score=score

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("Student Object.name, name must be a string!")
        self.__name=name
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise TypeError("Student Object.age, age must be a integer!")
        self.__age=age
    
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if not isinstance(score,float):
            raise TypeError("Sdudent Object.score, score must be a float!")
        self.__score=score
    
    def print_Sdudent(self):
        print("The Stduent:%s, age is %d, and score is %.2f"%(self.__name,self.__age,self.__score))

stu1=clsStudent()
stu1.name="ClerXiao"
stu1.age=14
stu1.print_Sdudent()

stu2=clsStudent("EleaZhao",44,99.00)
stu2.print_Sdudent()

print(type(stu1))
print(type(stu2))