# Forage Lyft Back-end Engineering Project
The goal of this project was to review starter code with basic unit tests and then plan out a new architecture which
allows for easier ways of changing car components and checking if a car needs to be serviced based on certain 
parameters.

Step 1 - Plan out new architecture using class diagram.
Step 2 - Refactor code based on plan
Step 3 - Enhance unit tests
Step 4 - Add new features and expand unit tests

My original class diagram was not quite what the program had in mind but at a high level it was close. Difference being
that Lyft engineers had a CarFactory which creates cars that have different components, and then uses a Serviceable
class to check if a car needs to be serviced. 

Using a provided class diagram (not the one I had in the repo) created Serviceable which is the parent class for Car 
which by composition has Engine, Battery and tire classes. These classes have subclasses for each Engine, Battery, and  
Tire type. Using abc library the @abstractmethod class is used to search down the class tree to check the appropriate 
components needs_service method to check if one of the service conditions has been met. 

I included my original class diagram below to show my first attempt at planning out the project vs the classes correct
answer. 

![My UML diagram](UMLdiagram_ChristianFranklin.pdf)

![Courses UML diagram](Course_ClassDiagram.pdf)
