


Python Turtle Graphics Square Drawer
This Python script utilizes the Turtle graphics module to draw a square on the screen.

Table of Contents
Introduction
Dependencies
Installation
Usage
Example
Contributing
License
Introduction
This Python script demonstrates the basic usage of the Turtle graphics module, which allows users to create graphics and drawings using a turtle that can move around the screen.

Dependencies
The script requires Python to be installed on your system. Additionally, it uses the built-in turtle module, which is available in the standard library of Python.

Installation
No installation is required beyond having Python installed on your system. Ensure you have Python installed, and you're ready to run the script.

Usage
To use the script, follow these steps:

Download or clone the script file draw_square.py to your local machine.
Open a terminal or command prompt.
Navigate to the directory where draw_square.py is located.
Run the script using the command: python draw_square.py
Example
Here's a brief example of how the script works:

python
Copy code
import turtle

# Create a turtle object
timmy = turtle.Turtle()

# Draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

# Display the drawing
turtle.Screen().exitonclick()
This code creates a turtle named timmy and uses it to draw a square with each side measuring 100 units.

Contributing
Contributions to improve the script or add new features are welcome. If you'd like to contribute, please fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

![image](https://github.com/guptuv/turtle_rectangle/assets/116263507/bbfb5d99-12d6-441b-9b41-b368f88ce7d0)

