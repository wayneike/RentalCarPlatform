# Online Car Rental Platform

## Project Objective:
Develop an online car rental platform by employing Object-Oriented Programming in Python.

## Problem Statement:
A car rental company has requested you to develop an online platform for renting cars where customers can easily view the cars available for rental on an hourly, daily, or weekly basis. The company will show the current inventory and verify requests by checking the available stock. Upon returning the car, customers will receive an automatically generated bill.

For simplicity, let’s assume that:
1. Customers may rent cars using one of the following options: hourly, daily, or weekly rental.
1. Customers can freely choose the number of cars they wish to rent as long as the quantity of available cars exceeds their requested amount.

## You must use the following tools:
Jupyter Notebook: To create the module and main project files

## Instructions to Perform:

1. Create a module (.py file) for car rental and import the built-in DateTime module to manage the rental time and billing
1. Create a class for renting the cars and define a constructor in it
1. Define a method to display the available cars. Additionally, create methods for renting cars on an hourly, daily, and weekly basis, respectively
1. Within these methods, ensure that the requested number of cars is both positive and less than the total number of available cars
1. Store the rental time of a car in a variable. You can later use this variable in the bill when returning the car
1. Define a method that returns the cars based on rental time, rental mode (hourly, daily, or weekly), and the number of cars rented
1. Within the return method, perform the following actions: update the inventory stock, calculate the rental period, and generate the final bill
1. Create a class for customers and define a constructor in it
1. Define methods for requesting the cars and returning them
1. Now, create the main project file (.ipynb) next and import the car rental module into it
1. Define the main method and create objects for both the car rental and customer classes
1. Within the main method, receive the customer's input to choose between displaying car availability, rental modes, or returning the cars
1. Utilize the appropriate method for the customer's input and display relevant messages
Run the main method to start your project