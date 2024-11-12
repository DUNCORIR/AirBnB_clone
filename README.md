AirBnB Clone - The Console
Project Description
This project is the first phase in building an AirBnB clone. The focus of this phase is to develop a command-line interpreter (CLI) that allows users to interact with a simulated backend for an AirBnB-like application. Users can create, retrieve, update, and delete objects through commands within the console. This interpreter serves as the foundational tool for managing the application's data and its persistence layer.

The project includes:

A console for managing instances of various classes.
File storage using JSON to persist data across sessions.
Core models representing different entities (User, Place, City, etc.).
This console will be a basis for later stages, including creating a web application.

Command Interpreter Description
The command interpreter is an interactive shell environment used to manage objects that represent entities within the AirBnB app. It provides functionality for creating, viewing, updating, and deleting these objects and is extensible to accommodate additional commands and classes as the project develops.

How to Start the Command Interpreter
Clone the Repository

git clone https://github.com/duncorir/AirBnB_clone.git
cd AirBnB_clone
Make the Console Executable

chmod +x console.py
Start the Interpreter

./console.py
This will launch the console with a prompt (hbnb) where commands can be entered.

How to Use the Command Interpreter
The interpreter supports several commands for interacting with objects. Commands include:

create: Creates a new instance of a class and saves it.
show: Displays the details of an instance using its ID.
destroy: Deletes an instance based on its ID.
all: Displays all instances, or all instances of a specific class.
update: Updates attributes of an instance based on its ID.
quit: Exits the console.
Each command is followed by parameters that specify the class and/or instance ID to operate on, as well as any attribute values for updates.

Available Commands
Command	Usage Format	Description
create	create <ClassName>	Creates a new instance of the specified class.
show	show <ClassName> <id>	Prints the string representation of an instance.
destroy	destroy <ClassName> <id>	Deletes an instance of the specified class based on its ID.
all	all or all <ClassName>	Shows all instances, or all instances of a specific class.
update	update <ClassName> <id> <attr_name> <attr_value>	Updates an instance by adding or updating an attribute.
quit or EOF	quit or press Ctrl+D	Exits the console.

Examples
1. Creating a New Instance
To create a new instance, use the create command followed by the class name:

(hbnb) create User
This will create a new User instance and return its unique ID.

2. Showing an Instance
To view the details of an instance, use the show command, specifying the class name and instance ID:

(hbnb) show User 1234-5678-9101
3. Destroying an Instance
To delete an instance, use the destroy command with the class name and instance ID:

(hbnb) destroy User 1234-5678-9101
4. Viewing All Instances
To see all instances of all classes, use the all command:

(hbnb) all
To view only instances of a specific class:

(hbnb) all User
5. Updating an Instance
To update attributes of an instance, use the update command with the class name, instance ID, attribute name, and new value:

(hbnb) update User 1234-5678-9101 email "new_email@example.com"
6. Exiting the Console
To exit the console, use the quit command or press Ctrl+D:

(hbnb) quit
Project Files
console.py: The main file for the command interpreter.
models/: Directory containing the model classes (e.g., BaseModel, User, etc.) and storage engine.
tests/: Directory for unit tests for each class and component.
