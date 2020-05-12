#  # Inheritance: It is the mechanism wherein one class inherits the features of another class.

#  # => Super Class : Whose features are inherited 
#  # => Sub Class   : Who   inherits features of super class
#  # => Reusability : We can derive the new class from an existing class.



# # Single Inheritance
# # A inherits B
# class Parent:
# 	def func1(self):
# 		print('The function is in parent class')

# class Child(Parent):
# 	def func2(self):
# 		print('The function is in child class')

# object = Child()
# object.func1()
# object.func2()	

# # Multiple Inheritance
# # C inherits A , C inherits B
# class Mother: 
#     mothername = "" 
#     def mother(self): 
#         print(self.mothername) 
  
# # Base class2 
# class Father: 
#     fathername = "" 
#     def father(self): 
#         print(self.fathername) 
  
# # Derived class 
# class Son(Mother, Father): 
#     def parents(self): 
#         print("Father :", self.fathername) 
#         print("Mother :", self.mothername) 
  
# # Driver's code 
# s1 = Son() 
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()


# # Multilevel Inheritance
# # A inherits B and B inherits C

# # Base class 
# class Grandfather: 
#     grandfathername =""  
#     def grandfather(self): 
#         print(self.grandfathername) 
  
# # Intermediate class 
# class Father(Grandfather): 
#     fathername = "" 
#     def father(self): 
#         print(self.fathername) 
  
# # Derived class 
# class Son(Father): 
#     def parent(self): 
#         print("GrandFather :", self.grandfathername) 
#         print("Father :", self.fathername) 
  
# # Driver's code 
# s1 = Son() 
# s1.grandfathername = "Srinivas"
# s1.fathername = "Ankush"
# s1.parent() 


# # Heirarchal Inheritance
# # B inherits A, C inherits A, D inherits A
# class Parent: 
#       def func1(self): 
#           print("This function is in parent class.") 
  
# # Derived class1 
# class Child1(Parent): 
#       def func2(self): 
#           print("This function is in child 1.") 
  
# # Derivied class2 
# class Child2(Parent): 
#       def func3(self): 
#           print("This function is in child 2.") 
   
# # Driver's code 
# object1 = Child1() 
# object2 = Child2() 
# object1.func1() 
# object1.func2() 
# object2.func1() 
# object2.func3() 

# # Hybrid Inheritance
# #			A 
# #		B 		C
# #			D
# # B inherits A, C inherits A, D inherits B, D inherits C


# class School: 
#      def func1(self): 
#          print("This function is in school.") 
   
# class Student1(School): 
#      def func2(self): 
#          print("This function is in student 1. ") 
   
# class Student2(School): 
#      def func3(self): 
#          print("This function is in student 2.") 
   
# class Student3(Student1, School): 
#      def func4(self): 
#          print("This function is in student 3.") 
   
# # Driver's code 
# object = Student3() 
# object.func1() 
# object.func3() 


# # Super Function
# # Super function allows us to call a method from the parent class.

# class Parent:
# 	def func1(self):
# 		print('This is func1')

# class Child(Parent):
# 	def func2(self):
# 		super().func1()
# 		print('This is function2')
# ob = Child()
# ob.func2()

# # Method Overriding
# # Method Overriding happens in Inheritance(But called run time polymorphism) and Method Overloading happends in Polymorphism

# class Parent:
# 	def same(self):
# 		print('This is method overriding')
# 	def diff(self):
# 		print('This is different in overriding')
# class Child(Parent):
# 	def same(self):
# 		# super().same()
# 		print('This is method overriding in Child')

# ob = Child()
# ob.diff()
# ob.same()	# Method in the Child class gets executed. Due to overriding


# # Polymorphism:
# # Polymorphism means many forms. 
# # A person at a same time can have differnt characters. For Example a person maybe a husband,
# # brother, father etc. So the same person can poses different behaviour in different situations.
# # This is called Polymorphism.


# # Polymorphism in Python are mainly of Two Types:
# # 	Overloading
# # 	Overriding

# # Giving only 2 result in z=0, whereas all three results in z =4
# def add(x, y, z = 0):  
#     return x + y+z 
  
# # Driver code  
# print(add(2, 3)) 
# print(add(2, 3, 4)) 

# # Polymorphism with methods.
# class India(): 
#     def capital(self): 
#         print("New Delhi is the capital of India.") 
  
#     def language(self): 
#         print("Hindi is the most widely spoken language of India.") 
  
#     def type(self): 
#         print("India is a developing country.") 
  
# class USA(): 
#     def capital(self): 
#         print("Washington, D.C. is the capital of USA.") 
  
#     def language(self): 
#         print("English is the primary language of USA.") 
  
#     def type(self): 
#         print("USA is a developed country.") 

# obj_india = India()
# obj_usa   = USA()

# for country in (obj_india, obj_usa):
# 	country.capital()
# 	country.language()
# 	country.type()


# # Encapsulation
# # . It describes the idea of wrapping data and the methods that work on data within one unit. Data hiding
# # Creating a Base class 

  
# # Creating a base class 
# class Base: 
#     def __init__(self): 
          
#         # Protected member 
#         self._a = 2
  
# # Creating a derived class     
# class Derived(Base): 
#     def __init__(self): 
          
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self)  
#         print("Calling protected member of base class: ") 
#         print(self._a) 
          
# obj1 = Base() 
  
# # Calling protected member 
# # Outside class will  result in  
# # AttributeError 
# # print(obj1.a) 
  
# obj2 = Derived() 

# class Car:
# 	# __private = 100
#     def __init__(self):
#         self.__updateSoftware()

#     def drive(self):
#         print('driving')

#     def __updateSoftware(self):
#         print('updating software')

# redcar = Car()
# redcar.drive()
# redcar.__updateSoftware()  


# # Other programming languages have protected, But python doesnt have it.
# # Only Private

# from abc import ABC, abstractmethod 
  
# class Polygon(ABC): 
  
#     # abstract method 
#     def noofsides(self): 
#         pass
  
# class Triangle(Polygon): 
  
#     # overriding abstract method 
#     def noofsides(self): 
#         print("I have 3 sides") 
  
# class Pentagon(Polygon): 
  
#     # overriding abstract method 
#     def noofsides(self): 
#         print("I have 5 sides") 
  
# class Hexagon(Polygon): 
  
#     # overriding abstract method 
#     def noofsides(self): 
#         print("I have 6 sides") 
  
# class Quadrilateral(Polygon): 
  
#     # overriding abstract method 
#     def noofsides(self): 
#         print("I have 4 sides") 
  
# # Driver code 
# R = Triangle() 
# R.noofsides() 
  
# K = Quadrilateral() 
# K.noofsides() 
  
# R = Pentagon() 
# R.noofsides() 
  
# K = Hexagon() 
# K.noofsides()


# # Interface (Since python has a  complex interface we use interfacing of JAVA)

# # Why And When To Use Interfaces?

# # To achieve security - hide certain details and only show the important details of an object (interface).
# # Java does not support "multiple inheritance" (a class can only inherit from one superclass). 
# # However, it can be achieved with interfaces, because the class can implement multiple interfaces. 
# # Note: To implement multiple interfaces, separate them with a comma (see example below)

# # The implemented class must use all the function of the base interface
# # interface FirstInterface {
# #   public void myMethod(); // interface method
# # }

# # interface SecondInterface {
# #   public void myOtherMethod(); // interface method
# # }

# # class DemoClass implements FirstInterface, SecondInterface {
# #   public void myMethod() {
# #     System.out.println("Some text..");
# #   }
# #   // public void myOtherMethod() {
# #   //   System.out.println("Some other text...");
# #   // }
# # }

# # class object {
# #   public static void main(String[] args) {
# #     DemoClass myObj = new DemoClass();
# #     myObj.myMethod();
# #     myObj.myOtherMethod();
# #   }
# # }