// Object Oriented Programming (OOPs) Concept in Java

// 1.Polymorphism
// 2.Inheritance
// 3.Encapsulation
// 4.Abstraction
// 5.Class
// 6.Object
// 7.Method
// 8.Message Passing





Basic OOPs Interview Questions
1. What is the difference between OOP and SOP?
   OOP is a programming which is based on objects. SOP is a programming where program is divided into methods.
   OOP is bottoms up. SOP is tops down
   OOP has features like data hiding. SOP doesnt have such features.
   OOP has concept called reusability. SOP doesnt have that 

2. What is OOPs?
   OOPs (Object-Oriented Programming) is a type of programming which is based on objects rather than just functions and procedures. 
   individual objects are grouped into classes. OOPs implements entities like inheritance, polymorphism, hiding, etc into programming. 
   It also allows binding data and code together.


3. Why use OOPs?
=> Simplicity in complex problems
=> Reusability
=> Encapsulation (Hiding of data)
=> Polymorphism
=> Data Abstraction

4.What are the main features of OOPs?
=>Inheritance
=>Encapsulation
=>Polymorphism
=>Data Abstraction

5.What is object?
It is an instance of class. Where object can be combination of data structures, variables and functions

6. What is a class ?
class is a blueprint for creating objects

7.Difference between class and structures.
structures=> collection of user defined data types 

9. What is the difference between a class and an object?
Defination.
Class is a logical entity whereas Object is a physical entity.

10. What is inheritance?
Inheritance is a feature of OOPs which allows classes inherit common properties from other classes. 
For example, if there is a class such as ‘vehicle’, other classes like ‘car’, ‘bike’, etc 
can inherit common properties from the vehicle class. This property helps you get rid of redundant code 
thereby reducing the overall size of the code. (Reusability)

11. Different Types of Inheritence.
Single 		 Inheritance:	A inherits B
Multiple 	 Inheritance:	
Multilevel 	 Inheritance:
Hierarchical Inheritance:
Hybrid		 Inheritance:

12. Difference between mulitple and multilevel inheritance.
B inherits A, C inherits A (Multiple)
A inherits B inherits C    (Multilevel)

13. What is hybrid inheritance?
Hybrid inheritance is a combination of multiple and multi-level inheritance.

14. What is hierarchical inheritance?
Hierarchical inheritance refers to inheritance where one base class has more than one subclasses. 
For example, the vehicle class can have ‘car’, ‘bike’, etc as its subclasses.

15. What are the limitations of inheritance.
Jumping back and forth in the program leads to delay.
Improper use of inheritance will lead to wrong results

16. What is a superclass?
A superclass or base class is a class that acts as a parent to some other class or classes.

17. What is a subclass?
A class that inherits from another class is called the subclass. 

18. What is polymorphism?
Polymorphism refers to the ability to exist in multiple forms.
A man is a husband, father, brother.

19. What is static polymorphism?
Static polymorphism (static binding) is a kind of polymorphism that occurs at compile time.
An example of compile-time polymorphism is method overloading.

20. What is dynamic polymorphism?
Runtime polymorphism or dynamic polymorphism (dynamic binding) is a type of polymorphism which is resolved during runtime. 
An example of runtime polymorphism is method overriding.

21. What is method overloading?
Method overloading is a feature of OOPs which makes it possible to give the same name to more than one methods within a class 
if the arguments passed differ.

22. What is method overriding?
Method overriding is a feature of OOPs by which the child class or the subclass can redefine methods present in the base/ parent class
Here, the method that is overridden has the same name as well as the signature meaning the arguments passed and the return type.

23. What is operator overloading?
Operator overloading refers to implementing operators using user-defined types based on the arguments passed along with it.

Examples:
	print(1 + 2)  
	print("Geeks"+"For")  
  
	print(3 * 4) 
	print("Geeks"*4) 

25. What is encapsulation?
Encapsulation refers to binding the data and the code that works on that together in a single unit. 
For example, a class. Encapsulation also allows data-hiding as the data specified in one class is hidden from other

26. What are 'access specifiers'?
Access specifiers or access modifiers are keywords that determine the accessibility of methods, classes, etc in OOPs.
These access specifiers allow the implementation of encapsulation.

27. What is the difference between public, private and protected access modifiers?

Name 		Access from own Class 		Access from derived Class 		Access from world

public 		YES							YES								YES
private 	YES							NO 								NO
protected   YES							YES								NO



28. What is data abstraction?
Data abstraction is a very important feature of OOPs that allows displaying only the important information 
and hiding the implementation details.
For example, while riding a bike, you know that if you raise the accelerator,speed increase, but you don’t know how it actually happens. 

29. How to achieve data abstraction?
Data abstraction can be achieved through:

	Abstract class
	Abstract method

30. What is an abstract class?
An abstract class is a class that consists of abstract methods. These methods are basically declared but not defined. 
If these methods are to be used in some subclass, they need to be exclusively defined in the subclass.

31. Can you create an instance of an abstract class?
No. Instances of an abstract class cannot be created because it does not have a complete implementation. 
However, instances of subclass inheriting the abstract class can be created

32. What is an interface?
It is a concept of OOPs that allows you to declare methods without defining them. 
Interfaces, unlike classes, are not blueprints because they do not contain detailed instructions or actions to be performed. 
Any class that implements an interface defines the methods of the interface

// 34. What are virtual functions?
// Virtual functions are functions that are present in the parent class and are overridden by the subclass. These functions are used to achieve runtime polymorphism.

// 35. What are pure virtual functions?
// Pure virtual functions or abstract functions are functions that are only declared in the base class. This means that they do not contain any definition in the base class and need to be redefined in the subclass.
36. What is a constructor?
A constructor is a special type of method that has the same name as the class and is used to initialize objects of that class.

37. What is a destructor?
A destructor is a method that is automatically invoked when an object is destroyed. 
The destructor also recovers the heap space that was allocated to the destroyed object, closes the files and database connections of object

38. Types of constructors

Default constructor 		Easy
Parameterized constructors  Easy
Copy constructors 			Thats helpful when we want to copy a complex object that has several fields, 
or when we want to make a deep copy of an existing object.

Static constructor: Not in Java

Private constructor: The use of private constructor is to serve singleton classes. 
A singleton class is one which limits the number of objects creation to one




// // 1.What is Object Oriented Programming?
// // 2.Why OOP?
// // 3.What are main features of OOP?
// // 4.What is encapsulation?
// // 5.What is Polymorphism? How is it supported by C++?
// // 6.What is Inheritance and its purpose?
// // 7.What is Abstraction?
// // 8.
// // 9.
// // 10.
// // 11.
// // 12.
// // 13.
// // 14.


 What happens if you don’t use lamport clock
 A)no global ordering between processes since they have their local clocks

Corba USes IDL (Interface Defination Language)

inter language communcation
likt REST is used now
earlier it was CORBA
for communication between languages


CUDA is used for Parallel communication


MAp reduce
apReduce is a processing technique and a program model for distributed computing based on java. 
The MapReduce algorithm contains two important tasks, namely Map and Reduce. 
Map takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs). 
Secondly, reduce task, which takes the output from a map as an input and combines those data tuples into a smaller set of tuples. 
As the sequence of the name MapReduce implies, the reduce task is always performed after the map job.

Map : Key value pair
Reduce : Concise data


CORBA
CORBA is essentially a design specification for an Object Request Broker (ORB), where an ORB provides the mechanism required for 
distributed objects to communicate with one another, whether locally or on remote devices, written in different languages, or at different 
ocations on a network.


[9:59 AM, 5/12/2020] Shashank Gupta: Total ordering mai vector timestamp use hota hai
[9:59 AM, 5/12/2020] Shashank Gupta: Partial mai happems before relationship
[9:59 AM, 5/12/2020] Shashank Gupta: 3.3 seconds
[9:59 AM, 5/12/2020] Shashank Gupta: Map reduce mai
[9:59 AM, 5/12/2020] Shashank Gupta: Word length
[10:00 AM, 5/12/2020] Shashank Gupta: Hardware interoperability
[10:00 AM, 5/12/2020] Shashank Gupta: ....
[10:01 AM, 5/12/2020] Shashank Gupta: Orb banate hai
[10:01 AM, 5/12/2020] Shashank Gupta: Interface mai library defn hota hai
[10:02 AM, 5/12/2020] Shashank Gupta: Usse pata chalta hai

Election Algorithms:
Election algorithms choose a process from group of processors to act as a coordinator. 
If the coordinator process crashes due to some reasons, then a new coordinator is elected on other processor. 
Election algorithm basically determines where a new copy of coordinator should be restarted.

1. The Bully Algorithm –
This algorithm applies to system where every process can send a message to every other process in the system.

The Dynamic Invocation Interface (DII) is an API which allows dynamic construction of CORBA object invocations. 
It is used at compile time when a client does