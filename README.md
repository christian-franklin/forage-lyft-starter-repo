# Updated forage-lyft-starter-repo
Lyft component updated based on class diagram provided in forage class.

- Removed model classes
- Created CarFactory class
- Created Serviceable class
- Created Engine class
- Created Battery class
- Created nubbin and spindler battery sub-classes
- Updated Car class and individual engine classes

Serviceable is the parent class for Car which by composition has Engine and Battery classes. Engine + Battery classes
have subclasses for each Engine and Battery type. Using abc library the @abstractmethod class is used to search down
the class tree to check the appropriate components if a service check is needed. 

Car components are created using CarFactory class. Each Car contains an Engine and Battery which makeup the Car. 
