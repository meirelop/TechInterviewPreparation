# args and kwargs
###Args
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.


The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher order functions such as map and filter, etc.

Example:
```python
def myFun(arg1, *argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
```

###Kwargs
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
Example for usage of **kwargs:
```python
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')  
```


# Mutable and Immutable objects

**Python data type mutability:**
![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Languages/mutability.png)

In python variable binds to an object which holds value.
````python
# variable a binds to an object which holds value 1 in memory
id(a) # -> 1814233584
a = 1

# object with value 1 still exists in memory, but we lost binding to it, and now it binds to an object with value 2
id(a) # -> 1814233616
a = 2

````
Once immutable object loses bind to previous object, Garbage Collector collects it.
There is no way to get back to that object. Unless you use mutable object.

![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Languages/immutable_memory.png)

As contrary, mutable objects always save their initial memory location.
![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Languages/mutable_memory.png)

```python
a = ["milk", "eggs"]
id(a) # -> 18142336666

a = ["milk", "eggs", "bread"]
id(a) # -> 18142336666
```
## Do not use mutable default arguments in Python! 

In Python, when passing a mutable value as a default argument in a function, the default argument is mutated anytime that value is mutated.

```python
def foo(a=["milk", "eggs"]):
    a.append("bread")
    return a


print(foo())  # ['milk', 'eggs', 'bread'] 
print(foo())  # ['milk', 'eggs', 'bread', 'bread']
```

Python "retains" the default value and ties it to the function in some way. Since it is mutated inside the function, it is also mutated as a default. In the end, **we use a different default every time the function is called!**   

**So instead, do this:**
```python
def foo(a=None):
    if a is None:
        a = []
    a.append("bread")
    return a
```

resources:
https://freecontent.manning.com/mutable-and-immutable-objects/
https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/

