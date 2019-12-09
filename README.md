# FundamentalProject
http://34.89.71.123:8001/ << app

http://34.89.71.123:8080/ << Jenkins

https://docs.google.com/presentation/d/1cRoFtsZOBRWkOkHCWkkano-a5muyupsxD3uyUedDJmM/edit#slide=id.p  << Presentation slides

Project brief:
* To create a functioning CRUD application utilising all the technology, tools and methodologies that we have have learnt during training.
* Additional requirements included:
  -a Trello (or other project management) board listing user stories, risks, tasks and issues etc.
  -clear documentation and architecture
  -tests with coverage reports
  -a functioning front-end and intergrated API's, using Flask
  -intergration into a VCS (in this case, Git) and use of a CI server (Jenkins)
  
 * My app:
  - To create a colour palette maker wherein you can create a palette containing several colours as well as to be able to update, delete and read, as per CRUD.
  - Initially I had wanted to add a RGB output option so colours would be shown as a block of colour as well as an included colour chart and a random palette generator where a randomiser button would pull random values for the palettes to be generated.
  
 * ERD:
 
 https://drive.google.com/open?id=1snn3IzJlxp0i6okfLU9TtKbMiUW5cQOF << ERD
 
 - The above link shows my current ERD. Initially, I was going to have only two tables; that of the colour and palettes but then, with having multiple foreign keys in the palettes table, I had also planned to have a third joining table. With issues with foreign keys and being unsure with how to resolve the issue, I switched the colour foerign keys in the palette table to string input. After implementing a login and registration system with an account, I also added a user table and used the user ID as a foerign key in the palette table to to identify who the palette was created by.
 
 * Technologies used:
 
  -Python
  -Flask
  -Git
  -Github
  -SQLAlchemy
  -Trello
  -Jenkins
  -Gunicorn
  
  https://drive.google.com/open?id=14wmKgL5HFprAqtxZQ3n3C5DmVUTZgv_C  << test coverage report
  
*  Issues faced and how to improve:
  - As mentioned, issues with the foreign keys led me to have to change how I mapped my tables. I would research more into how to get multiple foreign keys in a table to work so that I would not have to restructure as I have had to this time
  - Cutting close to time, I would strive to improve my organisational and time management skills. Utilising the Trello boards better, setting daily goals with a weekly calendar and checking in with my progress with lists are some of the ways I would try to tackle this.
  - Strive to be better with all technologies, methodologies and tools I've learnt, be familiar enough to be able to navigate and utilise them with ease through practice as well as independent study.
  - Have more self confidence, being able to differentiate between actual abilities and imposter syndrome.
  - With the app itself, I would attempt to deliver a wholly functioning app within the time constraint and, hopefully. also add some decor to make a nicer user interface. 
  -With this particular app, I would like to include the features I was unable to implement this time; the random generator and library categories as well as a search by function wherein the user would be able to find a colour or a palette by any attribute that is related to it e.g. by hue category, colour name, hex code or by palette theme if theme categories are implemented. 
  - If I were to be more confident and ambitious, I would also like to implement a colour picker where the user can pick their colours from a chart or table directly and also be able to export the palettes in some format, such as an image file like .png or .jpeg .
  

