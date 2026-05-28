# 🐍 Python OOP Revision — Learning by Building Projects

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Focus-OOP%20Concepts-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Goal-FastAPI%20Backend-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
</p>

---

## 📖 About This Repository

Most people learn Object-Oriented Programming by reading definitions and memorizing syntax. This repository takes a completely different approach — every concept is learned by building a small, real-world project that actually uses that concept in a meaningful way.

The core philosophy here is simple: **if you cannot build something with it, you have not truly understood it.**

This repository documents my personal journey of mastering Python OOP from the ground up, with a long-term goal of becoming strong in backend development using FastAPI. Every topic is explained with context — not just *what* it is, but *why* it exists and *where* it is used in real software systems.

---

## 🎯 Goals of This Repository

- Build a deep, practical understanding of Python OOP — not just surface-level syntax knowledge.
- Connect every theoretical concept to a real project so the learning sticks.
- Develop a backend engineering mindset by thinking in terms of systems, contracts, and data protection.
- Use this foundation to confidently move into FastAPI, REST APIs, and scalable backend architecture.

---

## 🗺️ OOP Learning Roadmap

The topics in this repository are not independent — they build on each other in a specific order. Understanding this progression is important because each concept either solves a limitation of the previous one or extends it.

```
Classes & Objects            →   Defines the blueprint and creates instances
        ↓
Constructor (__init__)       →   Initializes objects properly at creation time
        ↓
Inheritance                  →   Reuses and extends existing class logic
        ↓
Method Overriding            →   Customizes inherited behavior in child classes
        ↓
Overloading & Duck Typing    →   Makes functions flexible without strict type rules
        ↓
Polymorphism                 →   Builds systems that work with any compatible object
        ↓
Abstraction                  →   Enforces rules and hides complex internals
        ↓
Encapsulation                →   Protects internal data through controlled access
```

---

## 🧠 Topics Covered

---

### 1️⃣ Classes and Objects

#### 📌 What is a Class?

A class is a blueprint or template that defines the structure and behavior of a particular type of object. It does not hold any data on its own — it simply describes what properties an object will have and what actions it can perform. Think of a class like an architectural plan for a building — the plan itself is not a building, but every building constructed from it will share the same layout.

#### 📌 What is an Object?

An object is a real, independent instance created from a class. Each object has its own separate copy of the class's variables, completely independent from all other objects created from the same class.

```python
user1 = BankAccount("Balaji", 10000)
user2 = BankAccount("Arjun", 5000)
# user1 and user2 are completely independent objects
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `class ClassName:` | Defines a new class |
| `object = ClassName()` | Creates an instance of the class |
| `object.attribute` | Accesses an attribute of the object |
| `object.method()` | Calls a method on the object |

#### 💡 Key Points

- A class is defined once but can be used to create unlimited objects.
- Every object created from the same class is independent — changing one does not affect another.
- Class names in Python follow **PascalCase** convention, for example `BankAccount`, `UserProfile`.
- The relationship between a class and an object is often described as: *class is the type, object is the value.*

#### ⚠️ Important Notes

- A class definition does not execute any code — it only describes the structure. Code runs only when an object is created or a method is called.
- Accessing an attribute that does not exist on an object raises an `AttributeError`.

---

### 2️⃣ Constructor — `__init__()`

#### 📌 What is a Constructor?

A constructor is a special method that Python automatically calls the moment an object is created. Its primary job is to initialize the object's variables and set up the initial state before anything else happens. Without a constructor, every object would start empty and you would have to manually assign values after creation — which is error-prone and unprofessional.

```python
class User:
    def __init__(self, name, role="viewer"):
        self.name = name
        self.role = role
```

#### 📌 What is `self`?

`self` refers to the specific object that is currently calling the method. When you write `self.name = name`, you are telling Python: *store this value inside this particular object, not globally.* This is how each object maintains its own separate data.

In Java, the same concept is handled by `this`. In Python, `self` must be explicitly written as the first parameter of every instance method — Python does not add it automatically.

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `def __init__(self):` | Defines the constructor method |
| `self` | Refers to the current object instance |
| `self.variable = value` | Creates and assigns an instance variable |
| `def __init__(self, name="default"):` | Constructor with a default argument |

#### 💡 Key Points

- `__init__()` is automatically called — you never call it manually.
- `self` must always be the first parameter of `__init__()` and every other instance method.
- You can set default values directly in the constructor parameters to make certain fields optional.
- Instance variables created with `self.` are unique to each object. Variables defined without `self.` inside a method are just local variables and disappear when the method ends.

#### ⚠️ Important Notes

- `__init__()` is not technically a constructor in the traditional sense — Python uses `__new__()` to create the object, and `__init__()` to initialize it. For everyday use, think of `__init__()` as the constructor.
- If you do not define `__init__()`, Python uses a default empty one inherited from the base `object` class.
- `self` is a naming convention, not a reserved keyword. You could name it anything, but **never do this** — it is universally expected to be `self`.

---

### 3️⃣ Inheritance

#### 📌 What is Inheritance?

Inheritance is a mechanism that allows a child class to automatically receive all the variables and methods of a parent class. The child does not rewrite that logic — it inherits it and can then extend or modify behavior as needed. This creates an **IS-A** relationship between the two classes.

```python
class Dog(Animal):   # Dog inherits from Animal
    pass
```

#### 📌 What is `super()`?

`super()` is a built-in function that gives you a reference to the parent class. It is most commonly used inside the child's constructor to call the parent's `__init__()` so that the parent's variables get properly set up before the child adds its own. Without `super()`, the parent's constructor never runs and the child object is missing whatever the parent was supposed to initialize.

```python
def __init__(self, name):
    super().__init__(name)   # Runs parent's __init__ first
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `class Child(Parent):` | Child inherits from Parent |
| `super().__init__()` | Calls the parent class constructor |
| `super().method()` | Calls a parent class method |
| `isinstance(obj, Class)` | Checks if an object is an instance of a class |
| `issubclass(Child, Parent)` | Checks if one class inherits from another |

#### 💡 Key Points

- Inheritance follows the **IS-A** principle — use it only when the child genuinely *is a* type of the parent. A `Dog` is an `Animal`. A `SavingsAccount` is a `BankAccount`.
- Python supports **multiple inheritance** — a child class can inherit from more than one parent at the same time.
- When a child does not define its own `__init__()`, Python automatically uses the parent's.
- The parent class is also called the **base class** or **superclass**. The child is also called the **derived class** or **subclass**.

#### ⚠️ Important Notes

- Calling `super().__init__()` is not optional when the parent has variables that need to be set up — skipping it will cause `AttributeError` when those variables are accessed later.
- In multiple inheritance, Python follows the **MRO (Method Resolution Order)** using the C3 linearization algorithm to decide which parent's method runs first. You can inspect it with `ClassName.__mro__`.
- Do not use inheritance just to reuse code if the IS-A relationship does not genuinely exist — that is a design mistake and leads to fragile code.

---

### 4️⃣ Method Overriding

#### 📌 What is Method Overriding?

Method overriding is when a child class provides its own implementation of a method that already exists in the parent class. When that method is called on a child object, Python runs the child's version instead of the parent's. The method name must be exactly the same in both parent and child.

```python
class Dog(Animal):
    def speak(self):          # Overrides Animal's speak()
        return "Woof!"
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| Same method name in child | Triggers overriding automatically |
| `super().method()` | Calls the parent's version of the overridden method |
| `@override` *(Python 3.12+)* | Explicitly marks a method as an override for clarity |

#### 💡 Key Points

- Overriding requires the method name to be identical in both the parent and child class.
- The child can completely replace the parent's behavior, or call `super().method()` first and then add to it.
- Overriding is the primary mechanism behind polymorphism — it is what allows the same method call to behave differently across different objects.
- Overriding is **optional** — if the child does not override a method, it simply inherits and uses the parent's version as-is.

#### ⚠️ Important Notes

- If you override a method but still need the parent's logic to run, always call `super().method()` explicitly — Python will not run it automatically.
- Do not confuse **overriding** with **overloading**. Overriding means replacing behavior in a child class. Overloading means handling different argument combinations in the same class.

---

### 5️⃣ Overloading and Duck Typing

#### 📌 Method Overloading in Python

Method overloading is the concept of having multiple versions of the same method that handle different numbers or types of arguments. Unlike Java or C++, Python does **not** support true method overloading — you cannot define the same method name twice in the same class. Python achieves the same result using `*args`, `**kwargs`, and default parameter values.

```python
def add(self, *args):
    return sum(args)   # Works for 2, 3, or any number of arguments
```

#### 📌 What is Duck Typing?

Duck typing is a core Python concept that comes from the phrase: *"If it walks like a duck and quacks like a duck, then it is a duck."* Python does not check what *type* an object is — it only checks whether the object has the method or property being used. This makes Python functions naturally flexible and removes the need for strict type hierarchies.

```python
def run_report(report):
    report.generate()   # Works for any object that has a generate() method
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `*args` | Accepts any number of positional arguments |
| `**kwargs` | Accepts any number of keyword arguments |
| `def method(self, x=None):` | Default argument as an overloading workaround |
| `hasattr(obj, 'method')` | Checks if an object has a specific attribute or method |

#### 💡 Key Points

- In Python, defining the same method name twice in a class does not cause an error — the second definition simply replaces the first. This is why true overloading is not possible.
- Duck typing is the reason Python does not need interfaces or strict type declarations to achieve flexible, reusable code.
- Duck typing enables **plug-and-play design** — any object that has the right methods will work in a function, regardless of its class hierarchy.

#### ⚠️ Important Notes

- Duck typing is powerful but can hide bugs. If you pass an object that does not have the expected method, Python raises an `AttributeError` only at runtime — not at compile time.
- Use `hasattr(obj, 'method_name')` to safely check whether an object supports a method before calling it, especially in dynamic systems.

---

### 6️⃣ Polymorphism

#### 📌 What is Polymorphism?

Polymorphism means *many forms*. In OOP, it means that the same method call can produce completely different behavior depending on which object it is called on. The calling code stays the same — only the behavior changes based on the object's type. Polymorphism is what makes systems flexible, extensible, and easy to scale.

```python
payment.pay(amount)   # Same call — different behavior for UPI, Card, Crypto
```

#### 📌 Types of Polymorphism

**1. Runtime Polymorphism (Method Overriding)**
The most common type. The correct method is chosen at runtime based on the actual object type, not the variable type.

**2. Compile-time Polymorphism (Method Overloading)**
Achieved in Python through `*args` and default arguments. The method handles different argument combinations.

**3. Duck Typing Polymorphism**
The most Pythonic form. Any object that has the required method works — no inheritance relationship is needed.

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| Same method name across classes | Enables polymorphic behavior |
| `for obj in list: obj.method()` | Classic pattern to demonstrate polymorphism |
| `isinstance(obj, Class)` | Check object type at runtime if needed |

#### 💡 Key Points

- Polymorphism is not a standalone feature — it is built on top of overriding and duck typing.
- The real power of polymorphism is that the calling code does not need to change when you add new types. You simply create a new class with the same method name.
- Polymorphism promotes the **Open/Closed Principle** — your system should be open for extension (add new types) but closed for modification (no changes to existing code).

#### ⚠️ Important Notes

- Overriding and overloading are **techniques** used to achieve polymorphism. Polymorphism is the **outcome**.
- Do not confuse polymorphism with just calling different methods. True polymorphism means the *same* interface, the *same* method call, producing different behavior.

---

### 7️⃣ Abstraction

#### 📌 What is Abstraction?

Abstraction means hiding complex internal implementation details and exposing only what the outside world needs to interact with. The user of a class should not need to understand *how* it works internally — they only need to know *what* it does and *how to use it*.

The classic real-world analogy is driving a car. You use the steering wheel, brake, and accelerator — you do not need to understand the engine's fuel injection or the ABS system. All that complexity is *abstracted* away.

In Python, abstraction is implemented using **Abstract Base Classes (ABCs)** from the `abc` module. An abstract class defines a *contract* — a list of methods that every child class must implement.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount): pass
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `from abc import ABC, abstractmethod` | Imports the tools needed for abstraction |
| `class MyClass(ABC):` | Declares an abstract base class |
| `@abstractmethod` | Marks a method as abstract — child must implement it |
| `pass` | Placeholder body for abstract methods |

#### 💡 Key Points

- An **abstract class** cannot be instantiated directly. Attempting to create an object from it raises a `TypeError`.
- A class that inherits from an abstract class **must implement all abstract methods** — otherwise it too becomes abstract and also cannot be instantiated.
- Abstract classes can also contain **concrete methods** (regular, non-abstract methods) that subclasses inherit without needing to override.
- Abstraction is the foundation of designing **APIs, frameworks, and plugin systems** where you define the rules but let others fill in the implementation.

#### ⚠️ Exception Cases

- If a child class inherits from an abstract class but does not implement even one of the abstract methods, Python raises a `TypeError` at object creation time — not at class definition time.
- You can have an abstract class that contains only concrete methods and no abstract methods at all. This is technically valid, but defeats the purpose of using `ABC`.
- Abstract methods *can* have a body (implementation). Child classes can call it via `super().method()` while still being required to override it.

#### 📊 Abstraction vs Inheritance — Key Differences

| Aspect | Inheritance | Abstraction |
|---|---|---|
| Overriding | Optional — child *can* override | Mandatory — child *must* override |
| Parent instantiation | Parent can be instantiated | Abstract parent **cannot** be instantiated |
| Purpose | Code reuse | Enforcing a contract / structure |
| Message to child | *"You can customize this."* | *"You must implement this."* |
| Module required | None | `from abc import ABC, abstractmethod` |

---

### 8️⃣ Encapsulation

#### 📌 What is Encapsulation?

Encapsulation means protecting an object's internal data and only allowing it to be accessed or modified through controlled, validated methods. The goal is to ensure that the internal state of an object is never accidentally corrupted by outside code. It bundles the data and the logic that governs that data together inside the same class.

#### 📌 Access Modifiers in Python

Python uses naming conventions — not strict keywords like `private` or `protected` in Java — to indicate how accessible a variable should be.

| Convention | Syntax | Meaning |
|---|---|---|
| Public | `self.name` | Fully accessible from anywhere |
| Protected | `self._name` | Accessible, but treat with care — internal use intended |
| Private | `self.__name` | Name-mangled — not meant for direct external access |

```python
self.name     # Public
self._age     # Protected
self.__bill   # Private → becomes self._ClassName__bill internally
```

#### 📌 What is Name Mangling?

When you prefix a variable with double underscores like `self.__bill`, Python internally renames it to `_ClassName__bill`. This process is called **name mangling**. It is not encryption or true security — it is Python's way of preventing accidental access and avoiding naming conflicts when child classes are involved.

Python's philosophy on private variables:
> *"You* can *access it if you really try — but the naming tells you that you* shouldn't."*

#### 📌 Getter and Setter Methods

A **getter** is a method that safely reads a private variable. A **setter** is a method that safely modifies a private variable — with validation built in. Together, they form a *controlled gateway* to private data.

```python
def get_bill(self): return self.__bill           # Getter
def set_bill(self, amount):                      # Setter with validation
    if amount > 0: self.__bill = amount
```

#### 🔑 Keywords and Syntax

| Keyword / Syntax | Purpose |
|---|---|
| `self.__variable` | Declares a private instance variable |
| `self._variable` | Declares a protected instance variable |
| `def get_x(self):` | Getter method to read private data |
| `def set_x(self, value):` | Setter method to modify private data with validation |
| `@property` | Python's built-in decorator for clean getter/setter syntax |
| `_ClassName__variable` | How Python stores private variables internally (name mangling) |

#### 💡 Key Points

- Encapsulation is about **protecting architecture**, not achieving security. Private variables exist to prevent bugs — not to lock out developers.
- Setters allow you to add validation logic so that invalid data (negative bill amounts, empty names, out-of-range values) is rejected before it ever reaches the private variable.
- Python's `@property` decorator offers a cleaner, more Pythonic alternative to writing explicit `get_x()` and `set_x()` methods.
- Encapsulation keeps the object's internal state always valid and consistent — this is called maintaining **data integrity**.

#### ⚠️ Exception Cases and Important Notes

- Python's private variables are **not truly private**. You can still access `obj._ClassName__variable` directly if you really want to. Python trusts the developer — it only prevents *accidental* access.
- Protected variables (`_name`) are purely **by convention** in Python. The interpreter does not enforce any restriction on them — it is a signal to other developers that the variable is for internal use.
- If a child class inherits from a parent and both define `self.__variable`, they do **not** conflict — name mangling gives them different internal names (`_Parent__variable` and `_Child__variable`).

---

## 🛠️ Projects Built

### 🏦 Bank Account System
**Concepts practiced:** Classes, Objects, Constructor, `self` keyword.

This project simulates a basic bank account with deposit and withdrawal functionality. It demonstrates how to model a real-world entity as a class, initialize it through a constructor, and create multiple independent account objects that do not interfere with each other.

---

### 🎮 Game Character System
**Concepts practiced:** Inheritance, Method Overriding, Polymorphism.

This project builds a role-playing game character hierarchy where a base `Character` class is extended by specific types like `Warrior`, `Mage`, and `Rogue`. Each character type overrides the combat methods with unique behavior, demonstrating how polymorphism allows one function to handle all character types through the same interface.

---

### 🏥 Hospital Management System
**Concepts practiced:** Encapsulation, Private variables, Getters and Setters.

This project models a patient records system where sensitive data like billing and medical history is protected using private variables. All modifications go through setter methods with validation, ensuring the system never ends up in an invalid or inconsistent state.

---

### 💳 Payment Gateway System
**Concepts practiced:** Abstraction, Polymorphism, Abstract Base Classes.

This project builds a payment processing system where a `PaymentGateway` abstract class defines the contract that all payment providers must follow. Multiple providers — UPI, Card, Crypto — implement the interface differently, and the checkout system works with all of them through a single `pay()` call without caring about the underlying implementation.

---

## 💡 Key Takeaways

- OOP is not just syntax — every concept exists because it solves a real, recurring problem in software engineering.
- **Classes and Objects** let you model real-world entities and create multiple independent instances from a single blueprint.
- **Constructors** guarantee that every object starts fully initialized, removing the risk of working with incomplete objects.
- **Inheritance** reduces duplication by letting child classes reuse logic from a parent instead of rewriting it.
- **Overriding** lets child classes customize inherited behavior without changing the parent's structure.
- **Duck typing** makes Python functions flexible — they care about what an object *can do*, not what *type* it is.
- **Polymorphism** allows you to build systems that work with any compatible object, making your code future-proof and extensible.
- **Abstraction** enforces contracts — it guarantees that certain methods will always exist on any class that claims to follow a specific interface.
- **Encapsulation** protects your system's internal logic from accidental misuse, ensuring data integrity through controlled, validated access.

---

## 🚀 Future Roadmap

- [ ] Advanced OOP — Mixins, Multiple Inheritance, MRO (Method Resolution Order)
- [ ] Magic / Dunder Methods — `__str__`, `__repr__`, `__len__`, `__eq__`, `__add__`
- [ ] `@property` Decorator — Pythonic getter and setter syntax
- [ ] File Handling — Reading, writing, and managing files with OOP design
- [ ] Database Integration — SQLite and PostgreSQL with OOP models
- [ ] REST API Design — Understanding HTTP, request/response architecture
- [ ] FastAPI Projects — Building production-ready APIs with Python
- [ ] Authentication Systems — JWT, OAuth2, session management
- [ ] Backend Architecture — Services, repositories, dependency injection patterns

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| `abc` module | Abstract Base Classes for Abstraction |
| Git & GitHub | Version control and project tracking |
| FastAPI *(upcoming)* | Backend API framework |

---

## 👤 Author

**Balaji**
Learning Python OOP by building real projects, developing a backend engineering mindset, and working toward professional FastAPI development.

[![GitHub](https://img.shields.io/badge/GitHub-GoondlaBalaji-black?style=flat&logo=github)](https://github.com/GoondlaBalaji/Python-OOPS-Revision-with-Projects)

---

<p align="center">Built with curiosity, consistency, and a lot of <code>self</code>.</p>
