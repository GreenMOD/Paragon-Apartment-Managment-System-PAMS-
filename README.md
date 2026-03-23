# Paragon-Apartment-Managment-System-PAMS-
*All companies are fictional and for the purpose of the project*

## Agile
An Agile framework is a structured approach based on taking an iterative approach to  project management. [Joseph A. Griffin](https://cps.northeastern.edu/faculty/joseph-griffin/)  said 'Think of Agile broadly as a guiding orientation for how we approach project work.'
### Scrum
Scrum is a specific methodology of agile, sometimes called Agile Scrum. An important aspect of Scrum is its roles, Alongside the developers  is the Scrum Master who organises meeting and insures that all developers adhere to the Scrum methodology. More seniorly is the Product Owner who sets out the vision, builds the gap between the stakeholders and developers. Agile also needs agile ceremonies. An important ceremony within Scrum is a Scrum Sprint. Sprints are short (in our case usually one or two weeks long) events where a goal is set and the team attempts to deliver said goal within the set time. 

Before we moved to Agile Scrum we fell into the Waterfall methodology as we were not yet aware of the flexibility required for our project. The Waterfall methodology also appeared more appealing as the timescale for our project had already been laid out with little chance for change on blackboard. The set time was the 23rd of April 2025 and that allowed for planning and assignment of group roles to be done early on. The project also lended itself to effective use of Waterfall as the goal described in the document on blackboard is not going to change and sets out everything we need to provide. 

Over time we transitioned from Waterfall to Agile Scrum as it proved to be more effective for managing how our group project. A particularly useful aspect of Agile Scrum methodology is the scrum meetings which allowed our team to consolidate and plan out what to do next. We also naturally organised into the roles of the methodolgy. EXPAND
<br>
<br>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/6c346b2e-b313-4588-b3e3-b7a4f8c998f1" /><br>
*Chet Hendrickson (right) and another man (potentially Kent Beck) look to Ron Jeffries (centre) for advice, unsure of what to say Jeffries looks to his Pepsi for advice. 2015*
<br>
<br>
## Implementation
When we began our project, we decided on Python as the language we wanted to develop our application with. This is because Python was the most accessible language that we all knew. Python was also the best choice as the library we were planning on using for connecting to our database was my-sql-connector. My-sql-connector is a library that had drivers for Python that we all used last year for setting up database connectivity. However, when it came to the framework for displaying the GUI and providing functionality with the front end, it was a more difficult decision. 
### PySide 6
Pyside 6 was an obvious first choice. Based off the Qt framework, Pyside 6 is a contains a vast number of cross-platform compatible widgets. These widgets range from labels and buttons to whole windows and pop ups.
<br>
<br>
One of the main benefits of Pyside was that it comes with Qt Designer, an application that makes the designing stage of development must more efficient. Qt Designer allows a user to drag and drop buttons and labels to where they would like them. This gives a graphical preview of the window currently being created and prevents the waste of time with setting up basic values such as position and parents. However, the functionality of these widgets must be connected to functions written in the front end and only provides support with the designing stage.
<br>
<br>
Due to most widgets inheriting from the QWidget class, pages are simple to create and functionality can be easily reused, swapped out or changed to fit the scenario. One of the main features of PySide that made us consider it was the StackedWidget. The StackedWidget stores pages containing groups of widgets linked to a given page. When a specific page is selected, the stackedWidget hides all other pages and only shows then widgets related to that page index. This creates an incredible method of traversal through that application that is both seamless and professional.
<br>
<br>
However, PySide 6 is a framework rather than a wrapper for Python. This means that though we can create a more modern and professional application, it has a steep learning curve that without experience may slow development. It also means that it must be downloaded from third-party software as it is not a module included in the standard Python library.
### Tkinter
Tk Interface, Tkinter for short, is a module that in contrast to PySide comes preinstalled when downloading the distribution. It provides an interface for Tk and Tcl, which are responsible for the creation and running of the application. Tool Command Language, Tcl, contains the necessary scripts for building and running the window and Toolkit, Tk, contains the widgets and GUI components to display the application and business logic.
<br>
<br>
The main benefit of Tkinter is that it offers a lightweight and cross-platform experience with the basic widgets needed for an application. This means that implementation can be developed on most hardware without difficulty. It also has a simple syntax and is easy to learn, reducing the training time dramatically. 
However, PySide has a much larger list of widgets that are highly specialised in their function. 
### Conclusion
