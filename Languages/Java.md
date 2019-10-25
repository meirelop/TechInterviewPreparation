There are two types of modifiers in Java: **access modifiers** and **non-access modifiers**.

# Access modifiers

![Access mods](https://raw.githubusercontent.com/meirelop/TechInterviewPreparation/master/Languages/javaAccessMods.png)


# Non-Access modifiers

Java provides a number of non-access modifiers to achieve many other functionalities.

- The static modifier for creating class methods and variables.

- The final modifier for finalizing the implementations of classes, methods, and variables.

- The abstract modifier for creating abstract classes and methods.

- The synchronized and volatile modifiers, which are used for threads.


### Static variables and methods
**Static Variables**

The static keyword is used to create variables that will exist independently of any instances created for the class. Only one copy of the static variable exists regardless of the number of instances of the class.
Static variables are also known as class variables. Local variables cannot be declared static.

**Static Method**
in Java belongs to the class and not its instances. A static method can access only static variables of class and invoke only static methods of the class.
Usually, static methods are utility methods that we want to expose to be used by other classes <em>without the need of creating an instance</em>em>

Example:
```java
public class MathUtils {

public static long add(long i, long j) {
    return i + j;
}

//static util method
public static int addInts(int i, int...js){
    int sum = i;
    for(int x : js) sum+=x;
    return sum;
}

}


MathUtils.add(100L, 20L);
MathUtils.addInts(1, 2, 3, 4);
```

**When to create static methods?**

- Static Method doesn’t require instance creation, so it’s generally faster and provides better performance. That’s why utility class methods in Wrapper classes, System class, Collections class are all static methods.
- It’s possible to write fluent code when static imports are used. You will see this a lot in testing frameworks such as JUnit and TestNG.
- When your method only depends on its parameters, object state has no effect on the method behavior. Then you can create the method as static.

In all other cases, you should be better with the non-static method.



### Final modifier
**Final methods**
cannot be overridden by any subclasses. As mentioned previously, the final modifier prevents a method from being modified in a subclass.
The main intention of making a method final would be that the content of the method should not be changed by any outsider.

**Final classes**
The main purpose of using a class being declared as final is to prevent the class from being subclassed. If a class is marked as final then no class can inherit any feature from the final class.

### The Abstract modifier
**Abstract Class**
can never be instantiated. If a class is declared as abstract then the sole purpose is for the class to be extended.
A class cannot be both abstract and final (since a final class cannot be extended). If a class contains abstract methods then the class should be declared abstract. Otherwise, a compile error will be thrown.
An abstract class may contain both abstract methods as well normal methods.

### The Synchronized Modifier
The synchronized keyword used to indicate that a method can be accessed by only one thread at a time. The synchronized modifier can be applied with any of the four access level modifiers.



# Java Enums
An enum is a special "class" that represents a group of **constants** (unchangeable variables, like final variables).
```java
enum Level {
  LOW,
  MEDIUM,
  HIGH
}

Level myVar = Level.MEDIUM;
```

# Java Abstraction
Data abstraction is the process of hiding certain details and showing only essential information to the user.
Abstraction can be achieved with either **abstract classes or interfaces**.
An interface is a completely "abstract class" that is used to group related methods with empty bodies.
When a class implements an interface, you can think of the class as signing a contract, agreeing to perform the specific behaviors of the interface. If a class does not perform all the behaviors of the interface, the class must declare itself as abstract.


# Java Collections
### List
Most common type of lists in Java and most flexible.
The Java.util.List is a child interface of **Collection**. It is an ordered collection of objects in which duplicate values can be stored. Since List preserves the insertion order, it allows positional access and insertion of elements. List Interface is implemented by ArrayList, LinkedList, Vector and Stack classes.
List is an interface, and the instances of List can be created in the following ways:
```java
List a = new ArrayList();
List b = new LinkedList();
List c = new Vector(); 
List d = new Stack(); 
```

### Array
Array items can be changed, but Array size cannot be expanded after creation.
Fastest one if you know size of list beforehand
```java
int[] myNum = {10, 20, 30, 40};
```

### ArrayList
The difference between a built-in array and an ArrayList in Java, is that the size of an array cannot be modified. While elements can be added and removed from an ArrayList whenever you want. The syntax is also slightly different:

```java
import java.util.ArrayList;
ArrayList<String> cars = new ArrayList<String>();
```

### Map
Java Map is interface for all dictionary types.
Both HashTable and HashMap are implementations of Map interface.

### HashMap and HashTable
HashMap and Hashtable store key/value pairs in a hash table. When using a Hashtable or HashMap, we specify an object that is used as a key, and the value that you want linked to that key. The key is then hashed, and the resulting hash code is used as the index at which the value is stored within the table.

- 1. HashMap is non synchronized. It is not-thread safe and can’t be shared between many threads without proper synchronization code whereas Hashtable is synchronized. It is thread-safe and can be shared with many threads.
- 2. HashMap allows one null key and multiple null values whereas Hashtable doesn’t allow any null key or value.
- 3. HashMap is generally preferred over HashTable if thread synchronization is not needed

```java
Hashtable<Integer,String> ht=new Hashtable<Integer,String>();
HashMap<Integer,String> hm=new HashMap<Integer,String>(); 
```

