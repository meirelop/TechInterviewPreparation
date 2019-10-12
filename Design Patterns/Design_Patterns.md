# Most Common Design Patterns

## Singleton
The singleton pattern is used to limit creation of a class to only one object. This is beneficial when one (and only one) object is needed to coordinate actions across the system. There are several examples of where only a single instance of a class should exist, including caches, thread pools, and registries.
It’s trivial to initiate an object of a class — but how do we ensure that only one object ever gets created? The answer is to make the constructor ‘private’ to the class we intend to define as a singleton. That way, only the members of the class can access the private constructor and no one else.\
**Important consideration:** It’s possible to subclass a singleton by making the constructor protected instead of private. This might be suitable under some circumstances. One approach taken in these scenarios is to create a register of singletons of the subclasses and the getInstance method can take in a parameter or use an environment variable to return the desired singleton. The registry then maintains a mapping of string names to singleton objects, which can be accessed as needed.

```java
public final class Singleton {

    private static volatile Singleton instance = null;
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized(Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

## Factory Method

A normal factory produces goods; a software factory produces objects. And not just that — it does so without specifying the exact class of the object to be created. To accomplish this, objects are created by calling a factory method instead of calling a constructor.
The factory pattern comes under the creational patterns list category. It provides one of the best ways to create an object. In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface.
![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Design%20Patterns/factory.png)

```python
class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print (button_obj.create_button(b).get_html())
   
# output: 
# <img></img>  
# <input></input>  
# <obj></obj>
```

## Strategy Pattern


The strategy pattern is a type of behavioral pattern. The main goal of strategy pattern is to enable client to choose from different algorithms or procedures to complete the specified task. Different algorithms can be swapped in and out without any complications for the mentioned task.
This pattern can be used to improve flexibility when external resources are accessed.

```python
import types

class StrategyExample:
   def __init__(self, func = None):
      self.name = 'Strategy Example 0'
      if func is not None:
         self.execute = types.MethodType(func, self)

   def execute(self):
      print(self.name)

def execute_replacement1(self): 
   print(self.name + 'from execute 1')

def execute_replacement2(self):
   print(self.name + 'from execute 2')

if __name__ == '__main__':
   strat0 = StrategyExample()
   strat1 = StrategyExample(execute_replacement1)
   strat1.name = 'Strategy Example 1'
   strat2 = StrategyExample(execute_replacement2)
   strat2.name = 'Strategy Example 2'
   strat0.execute()
   strat1.execute()
   strat2.execute()

# output:
# Strategy Example 0
# Strategy Example 1from execute 1
# Strategy Example 2from execute 2
```

## Observer

In this pattern, objects are represented as observers that wait for an event to trigger. An observer attaches to the subject once the specified event occurs. As the event occurs, the subject tells the observers that it has occurred.

```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Observer:
    def __init__(self, observable):
        observable.register_observer(self)
    
    def notify(self, observable, *args, **kwargs):
        print('Got', args, kwargs, 'From', observable)


subject = Observable()
observer = Observer(subject)
subject.notify_observers('test')
# output: Got ('test',) {} From <__main__.Observable object at 0x10d5ad358>
```

## Builder

Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.

**Advantages of Builder Pattern:**
- It provides clear separation and a unique layer between construction and representation of a specified object created by class.
- It provides better control over construction process of the pattern created.
- It gives the perfect scenario to change the internal representation of objects.

```python
from __future__ import print_function
from abc import ABCMeta, abstractmethod


class Car(object):
    def __init__(self, wheels=4, seats=4, color="Black"):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return "This is a {0} car with {1} wheels and {2} seats.".format(
            self.color, self.wheels, self.seats
        )


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value
        return self

    def set_seats(self, value):
        self.car.seats = value
        return self

    def set_color(self, value):
        self.car.color = value
        return self

    def get_result(self):
        return self.car


class CarBuilderDirector(object):
    @staticmethod
    def construct():
        return CarBuilder().set_wheels(8).set_seats(4).set_color("Red").get_result()

car = CarBuilderDirector.construct()
print(car)
# output: This is a Red car with 8 wheels and 4 seats.
``` 

## Adapter 
This allows incompatible classes to work together by converting the interface of one class into another. Think of it as a sort of translator: when two heads of states who don’t speak a common language meet, usually an interpreter sits between the two and translates the conversation, thus enabling communication./
If you have two applications, with one spitting out output as XML with the other requiring JSON input, then you’ll need an adapter between the two to make them work seamlessly.

![alt CAP triangle](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Design%20Patterns/adapter.png)

```python
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."
RECHARGE = ["Recharge started.", "Recharge finished."]
POWER_ADAPTERS = {"Android": "MicroUSB", "iPhone": "Lightning"}
CONNECTED = "{} connected."
CONNECT_FIRST = "Connect {} first."

class RechargeTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def recharge(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class FormatIPhone(RechargeTemplate):
    @abstractmethod
    def use_lightning(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class FormatAndroid(RechargeTemplate):
    @abstractmethod
    def use_micro_usb(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

class IPhone(FormatIPhone):
    __name__ = "iPhone"

    def __init__(self):
        self.connector = False

    def use_lightning(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))

class Android(FormatAndroid):
    __name__ = "Android"

    def __init__(self):
        self.connector = False

    def use_micro_usb(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))

class AndroidRecharger(object):
    def __init__(self):
        self.phone = Android()
        self.phone.use_micro_usb()
        self.phone.recharge()

class IPhoneRecharger(object):
    def __init__(self):
        self.phone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()

print("Recharging Android with MicroUSB recharger.")
AndroidRecharger()

print("Recharging iPhone with iPhone recharger.")
IPhoneRecharger()
```


## State
The state pattern encapsulates the various states a machine can be in, and allows an object to alter its behavior when its internal state changes. The machine or the **context**, as it is called in pattern-speak, can have actions taken on it that propel it into different states. Without the use of the pattern, the code becomes inflexible and littered with if-else conditionals.

```python
class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    """ State of being powered on and working """
    name = "on"
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    """ State of being in suspended mode after switched on """
    name = "suspend"
    allowed = ['on']


class Hibernate(ComputerState):
    """ State of being in hibernation after powered on """
    name = "hibernate"
    allowed = ['on']


class Computer(object):
    """ A class representing a computer """

    def __init__(self, model='HP'):
        self.model = model
        # State of the computer - default is off.
        self.state = Off()

    def change(self, state):
        """ Change state """
        self.state.switch(state)


if __name__ == "__main__":
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)
    
# output:    
# Current: off  => switched to new state on
# Current: on  => switched to new state off
# Current: off  => switched to new state on
# Current: on  => switched to new state suspend
# Current: suspend  => switching to hibernate not possible.
# Current: suspend  => switched to new state on
# Current: on  => switched to new state off
```










Java Patterns:
https://www.journaldev.com/1827/java-design-patterns-example-tutorial