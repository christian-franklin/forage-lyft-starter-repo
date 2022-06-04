# Updated forage-lyft-starter-repo
Lyft component updated based on class diagram provided in forage class.

- Removed model classes
- Created CarFactory class
- Created Serviceable class
- Created Engine class
- Created Battery class
- Created nubbin and spindler battery sub-classes
- Updated Car class and individual engine classes
- Created Tire class and sub-classes for Carrigan and Octoprime tires

Serviceable is the parent class for Car which by composition has Engine and Battery classes. Engine + Battery + Tire 
classes have subclasses for each Engine and Battery type. Using abc library the @abstractmethod class is used to search 
down the class tree to check the appropriate components if a service check is needed. 

Car components are created using CarFactory class. Each Car contains an Engine, Battery and Tire which makeup the Car. 
