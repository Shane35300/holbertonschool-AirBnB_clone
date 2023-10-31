# AirBnB clone - The console

## Authors:
[![Static Badge](https://img.shields.io/badge/build-Gary-brightgreen?logo=github&label=Github&labelColor=19199&color=191919
)](https://github.com/PereDeMacron)

[![Static Badge](https://img.shields.io/badge/build-Shane-brightgreen?logo=github&label=Github&labelColor=19199&color=191919
)](https://github.com/Shane35300)

[![Static Badge](https://img.shields.io/badge/build-BDX/LVA-brightgreen?logo=undertale&label=C21&labelColor=e80c0c&color=191919
)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)



## Background Context

#### Welcome to the AirBnB clone project!
Before starting, please read the <strong>AirBnB</strong> concept page.
[HBNB Project Overview](https://www.youtube.com/embed/E12Xc3H2xqo)

##### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:



* put in place a parent class (called <font color="red"></font>BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (<font color="red">User</font>, <font color="red">State</font>, <font color="red">City</font>, <font color="red">Place</font>…) that inherit from <font color="red">BaseModel</font>
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
#### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Resources
##### Read or watch:

* <Strong>packages</Strong> concept page

* [cmd module](https://docs.python.org/3.4/library/cmd.html)

* [uuid module](https://docs.python.org/3.4/library/uuid.html)

* [datetime](https://docs.python.org/3.4/library/datetime.html)

* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)

* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)



## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

### General

* How to create a Python package
* How to create a command interpreter in Python using the <font color=red>cmd</font> module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage <font color=red>datetime</font>
* What is an <font color=red>UUID</font>
* What is <font color=red>*args</font> and how to use it
* What is <font color=red>**kwargs</font> and how to use it
* How to handle named arguments in a function

## Requirements

### Python Scripts

* Allowed editors: <font color=red>vi</font>, <font color=red>vim</font>, <font color=red>emacs</font>
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly <font color=red>#!/usr/bin/python3</font>
* A <font color=red>README.md</font> file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using <font color=red>wc</font>
* All your modules should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").\__doc__)'</font>)
* All your classes should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").MyClass.\__doc__)'</font>)
* All your functions (inside and outside a class) should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").my_function.\__doc__)'</font> and <font color=red>python3 -c 'print(\__import__("my_module").MyClass.my_function.\__doc__)'</font>)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

* Allowed editors: <font color=red>vi</font>, <font color=red>vim</font>, <font color=red>emacs</font>
* All your files should end with a new line
* All your test files should be inside a folder <font color=red>tests</font>
* You have to use the [unittest]() module
* All your test files should be python files (extension: <font color=red>.py</font>)
* All your test files and folders should start by <font color=red>test_</font>
* Your file organization in the tests folder should be the same as your project
* e.g., For <font color=red>models/base_model.py</font>, unit tests must be in: <font color=red>tests/test_models/test_base_model.py</font>
* e.g., For <font color=red>models/user.py</font>, unit tests must be in: <font color=red>tests/test_models/test_user.py</font>
* All your tests should be executed by using this command: <font color=red>python3 -m unittest discover tests</font>
* You can also test file by file by using this command: <font color=red>python3 -m unittest tests/test_models/test_base_model.py</font>
* All your modules should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").\__doc__)'</font>)
* All your classes should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").MyClass.\__doc__)'</font>)
* All your functions (inside and outside a class) should have a documentation (<font color=red>python3 -c 'print(\__import__("my_module").my_function.\__doc__)'</font> and <font color=red>python3 -c 'print(\__import__("my_module").MyClass.my_function.\__doc__)'</font>)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

## More Info
### Execution
Your shell should work like this in interactive mode:
	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$

But also in non-interactive mode: (like the Shell project in C)
	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$

All tests should also pass in non-interactive mode: <font color=red>$ echo "python3 -m unittest discover tests" | bash</font>

[Diagrams Image](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231031%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231031T082349Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0ced39559a519fd5f8e13e274da31d47783866e8864e3de8f4dd288203ef609e)]

[HBNB - The Console](https://www.youtube.com/embed/p00ES-5K4C8)
