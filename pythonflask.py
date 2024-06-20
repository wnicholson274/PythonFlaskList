""" # remove these to un-comment the code

# imports flask from the flask module
from flask import Flask 

# creates an instance of the flask class
app = Flask(__name__)

# defines a route for the URL 

@app.route("/") 

class Person: 
    def __init__(self, name, age):  #this function is being used to create instances for the name and age 
        self.name = name
        self.age = age

    def __str__(self): #this function is converting the instances (name and age) into strings so that it easier for human comprehension 
        return f"Name: {self.name}, age: {self.age}"


def create_person(): # this function creates the objects (name and age) and allows the user to input their name and age to the instances.
    people = [] #this creates an empty list for each instance that is going to be allocated to this list.
    for i in range(6): #This line starts a for loop that will iterate 6 times. The range(6) function generates a sequence of numbers from 0 to 5, so i will take each value in this sequence one at a time.
        name = input(f"Enter name for person {i + 1}: ")
        age = int(input(f"Enter age for person {i + 1}: ")) # line 23 + 24 both get the users input.
        person = Person(name, age) 
        people.append(person) #This line adds the newly created Person object to the people list.
    return people #After the loop completes this line returns the people list, which now contains 6 Person objects created from the user's input.

def display_people(people):
    for person in people: #this line is saying that for every object in the people list , print said object which are the name and age
        print(person)


if __name__=="__main__": # this line is used to ensure that certain parts of the code only run when the script is executed directly, and not when it is imported as a module in another script.
    app.run(host='0.0.0.0', port=5000, debug=True) # runs the flask web server
    people_list = create_person() # this line calls the create_person function, which prompts the user to input names and ages for six people
    display_people(people_list) #This line calls the display_people function with the people_list as an argument, which prints out the details of each Person object in the list.

""" # remove these to un-comment the code

# imports flask from the flask module
from flask import Flask

# creates an instance of the flask class
app = Flask(__name__)

class Person:
    def __init__(self, name, age): #this function is being used to create instances for the name and age 
        self.name = name
        self.age = age

    def __str__(self): #this function is converting the instances (name and age) into strings so that it easier for human comprehension
        return f"Name: {self.name}, Age: {self.age}"

def create_person(): # this function creates the objects (name and age) and allows the user to input their name and age to the instances.
    people = [] #this creates an empty list for each instance that is going to be allocated to this list.
    for i in range(30): #This line starts a for loop that will iterate 6 times. The range(6) function generates a sequence of numbers from 0 to 5, so i will take each value in this sequence one at a time.
        person = Person(name=f"Person {i + 1}", age=20 + i)
        people.append(person) #This line adds the newly created Person object to the people list.
    return people #After the loop completes this line returns the people list, which now contains 6 Person objects created from the user's input.

# defines a route for the URL 
@app.route("/")

def display_people(): #This line defines display_people function and is called when the program is run, which prints out the details of each Person object in the list.
    people = create_person() # this line calls the create_person function, which prompts the user to input names and ages for six people
    people_list_html = "<ul>" # initializes an HTML unordered list to hold the people data
    for person in people: #this line is saying that for every object in the people list, print said object which are the name and age
        people_list_html += f"<li>{person}</li>" # adds each person's string representation as a list item in the HTML list
    people_list_html += "</ul>"  # closes the HTML unordered list
    return f"<h1>People Data</h1>{people_list_html}" # returns the complete HTML to be displayed in the browser, including the list of people

if __name__ == "__main__": # this line is used to ensure that certain parts of the code only run when the script is executed directly, and not when it is imported as a module in another script.
    app.run(host="0.0.0.0", port=5000, debug=True) # runs the flask web server

    