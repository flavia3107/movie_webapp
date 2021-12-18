# Cs50 Final Project

#### Video Demo: https://youtu.be/0apIuDxfHds

#### Description:

My final project is a web application, which was created with **Python, JavaScript, HTML, CSS** languages and **Flask** framework.

The project is treated as an application which can be used for booking tourist packages in Albania.
The homepage of the application has elements like bootstrap carousel, which displays views of some of the most attractive tourist spots. Directly after the carousel element, there are shown three elements that briefly describe what the packages offered and below that there are three sections that describe what type of tourism are offered.

Layout.html is a file that is used to create the same structure for each application template, thus avoiding redundancy and duplication of the same structure on each page. This file contains imports of CSS files, bootstrap and other needed file for using external components, as well as the code needed to display modals anywhere in the app. Modals are used on highlight.html, sailing.html and walking.html pages to show descriptive videos of tourist spots.

When the user clicks one of the view details buttons, he will navigate directly to the page that gives the most detailed description of the selected package.

Once the descriptive page opens, a short paragraph is placed at the beginning of the page, that describes exactly what this package includes and below in chronological order are the itineraries in the form of sections. Each section will have an image placed to the left or right (depending on the index), a title indicating the city, a detailed description of what will be done during the day and a play episode button that will trigger modal. The modal will display the specified video (which is taken from YouTube) and display it in the application via the html iframe element. To have a dynamic modal, a script was used in the layout.html file and inside the script is written the logic for capturing the element as well as for changing the source of the video. Basically this is the structure for **walking.html, sailing.html and highlights.html**

In case the user is interested, at the top of the page, to the right of the title is placed a join us button, which serves to navigate the registration page, i.e. register.html. This file contains the html element of the form, which will be used to get the information from the user. The form itself will have the following fields: firstname, lastname, package, phone and email as well as a submit button that will send this data to the file specified in the form attribute, in this case to register using the post method.

The received information will be used in app.py, which contains the logic of the application, i.e. where the routes are defined as well as the part of the connection to the database. The register definition will check if the method is post or not, and if it is post then the values will be stored in variables and by the execute method of MySQL will insert those values as a new record in the bookings table (previously defined ) and if everything goes well it will redirect the user to the main page. If the method is Get it will redirect the user to the register form.

The last template file is about.html that contains information about Albania as well as the necessary elements for the user to contact the site or the people behind the site.

The static folder contains the images used by the application and the css files needed to style the application.
The modal.css file is used to style modals used to display videos.
File cards.css is used to style all sections of daily itineraries.
File about.css and nicepage.css, which was the existing template on the internet were used to style the about page.
And the latest style.css used to style parts of the application in general.

**Files in the template folder**
| File |Description  
|--------------------|----------------------------------------------------|
|about.html| used as template for about menu  
|highlights.html| has information about the albanian highlights package  
|index.html|main view of the app
layout.html| used as basic blue print for the rest of the html files  
|register.html|has the form needed for actually booking a package
|walking.html|has information about the walking albania package
sailing.html|has information about the sailing albania package
