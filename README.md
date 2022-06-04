# Forage Lyft Back-end Engineering Project
The goal of this project was to review a sample starter code project that would not scale well and then plan out a new 
architecture which allows for easier ways of changing car components and checking if a car needs to be serviced 
based on certain parameters. The idea being to keep scalability in mind for future changes or additional components. 

- Step 1 - Plan out new architecture using class diagram.
- Step 2 - Refactor code based on plan
- Step 3 - Enhance unit tests
- Step 4 - Add new features, change existing parameters and expand unit tests

My original class diagram was not quite what the program had in mind but at a high level it had similarities. 
One big difference being that the correct plan had a CarFactory which creates cars that have different components, 
and then uses a Serviceable class to check if a car needs to be serviced. 

Using the provided class diagram I created Serviceable which is the parent class for Car. Within Car by composition 
there is Engine, Battery and Tire classes. These classes have subclasses for each Engine, Battery, and Tire type. 
Using abc library the @abstractmethod wrapper is used to search down the class tree to check the appropriate components 
needs_service method to see if any of the service conditions have been met. 

i.e. we start at Serviceable and if the needs_service returns True for any component within the child class Car or
its related component classes then we know a Car needs to be serviced. 

CarFactory is then used in combination with the other classes to pick and choose which components make up a Car. 

Unittests were created to test different combinations of Engine, Battery and Tire that make up various Car objects.

I included my original class diagram below to show my first attempt at planning out the project vs the classes correct
answer. 

![My UML diagram](UMLdiagram_ChristianFranklin.pdf)

![Courses UML diagram](Course_ClassDiagram.pdf)

To see the original starter code, check the original source of my forked repo.

![Original Starter Code](https://github.com/vagabond-systems/forage-lyft-starter-repo)