# Smart_Device_Management_System

## Project Overview

The **Smart Device Management System** is a Python Object-Oriented Programming (OOP) mini project that simulates the management of smart home devices. The program demonstrates the core principles of OOP, including **Encapsulation**, **Inheritance**, **Properties (Getter and Setter Methods)**, and **Polymorphism through inherited methods**.

The system allows users to manage different smart devices such as a **Temperature Sensor**, **Smart Light**, and **Security Camera** using a simple menu-driven interface.

---

# Objectives

* Demonstrate the use of Object-Oriented Programming in Python.
* Create reusable classes using inheritance.
* Protect sensitive data using encapsulation.
* Control access to private attributes with getter and setter methods.
* Simulate basic smart home device operations.

---

# Features

The program allows users to:

* Display information about all smart devices.
* Turn any device ON.
* Turn any device OFF.
* Read temperature from a temperature sensor.
* Increase or decrease smart light brightness.
* Start recording using the security camera.
* Stop recording using the security camera.
* Exit the application.

---

# Classes Used

## 1. SmartDevice (Parent Class)

This is the base class for all smart devices.

### Private Attributes

* `__device_id`
* `__power_status`

### Public Attribute

* `name`

### Methods

* `turn_on()`
* `turn_off()`
* `display_info()`

The class also uses Python properties (`@property`) to provide controlled access to private attributes.

---

## 2. TemperatureSensor (Child Class)

Inherits from **SmartDevice**.

### Additional Attribute

* `temperature`

### Additional Method

* `read_temperature()`

This class simulates reading the current room temperature.

---

## 3. SmartLight (Child Class)

Inherits from **SmartDevice**.

### Additional Attribute

* `brightness`

### Additional Methods

* `increase_brightness()`
* `decrease_brightness()`

Brightness values are validated to remain between **0 and 100** using property setters.

---

## 4. SecurityCamera (Child Class)

Inherits from **SmartDevice**.

### Additional Attribute

* `recording_status`

### Additional Methods

* `start_recording()`
* `stop_recording()`

This class simulates the recording functionality of a smart security camera.

---

# Object-Oriented Programming Concepts Demonstrated

## Encapsulation

Private attributes are protected using double underscores (`__`).

Examples:

* `__device_id`
* `__power_status`
* `__brightness`

These attributes are accessed using getter and setter methods.

---

## Inheritance

The following classes inherit from `SmartDevice`:

* TemperatureSensor
* SmartLight
* SecurityCamera

This reduces code duplication and promotes code reusability.

---

## Getter and Setter Methods

Python's `@property` decorator is used to safely access and modify private attributes while enforcing validation.

---

## Menu-Driven Interface

The application provides a console-based menu that allows users to interact with the smart devices.

Available menu options include:

1. Display Device Information
2. Turn Device ON
3. Turn Device OFF
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Stop Recording
8. Exit

---

# Sample Devices

The program creates three smart devices:

| Device                  | ID     |
| ----------------------- | ------ |
| Living Room Sensor      | TS-112 |
| Dining Room Smart Light | SL-432 |
| Entrance Door Camera    | SC-098 |

---

# Requirements

* Python 3.x
* No external libraries are required.

---

# How to Run

1. Save the Python file.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:

```bash
python "Smart Device Management System.py"
```

5. Select menu options by entering the corresponding number.

---

# Expected Learning Outcomes

After completing this project, learners should be able to:

* Understand class creation in Python.
* Apply inheritance to reduce code duplication.
* Implement encapsulation using private attributes.
* Use properties (`@property`) for controlled attribute access.
* Build a menu-driven application using Object-Oriented Programming.

---

# Author

**Name:** Fredenard Amankwah

**Course:** Object-Oriented Programming (Python)

**Project Title:** Smart Device Management System

---

# Conclusion

This project demonstrates how Object-Oriented Programming can be used to build a simple smart home management application. It showcases important OOP concepts such as encapsulation, inheritance, properties, and object interaction while providing a practical, menu-driven system for controlling smart devices.
