<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/images/readme/banner.jpg" 
     target="_blank" rel="noopener" alt="Sprint">
</div>
<h2 align="center">Sprint</h2>

### Track your workouts one sprint at a time!

*Keeping fit by running or walking is popular amongst millions of people across the entire globe from your local park to the olympic games.* 
*An essential part of increasing an individuals fitness and the ability to objectively gauge their own fitness is logging activity times, intensity, and factors such as surface& weather.* 

*With this in mind the Sprint platform was designed with the main purpose of being a tool that allows the user to log their walking or run activities with ease anywhere and on any device. Sprint wants to make it possible for the user to manage their every single log on the platform, such as changing the activity name, changing their difficulty preference or even deleting that Sprint log altogether.*

#### You can visit the Sprint platform [here.](https://flask-sprint-project.herokuapp.com/)

  - Site mobile demo: *https://www.youtube.com/watch?v=j5vqz2_EDUA*

## Contents
* [Project purpose](#Project-purpose)
     * [UX](#UX)
     * [User-Stories](#User-Stories)
* [Design](#Design)
     * [Typography](#Typography)
     * [Colours](#Colours)
     * [Icons](#Icons)
     * [CRUD and MongoDB](#CRUD-and-MongoDB)
* [Wire-Frames](#Wire-Frames)
     * [Features](#Features)
     * [Features left to be implemented](#Features-left-to-be-implemented)
     * [issues-and-bugs](#issues-and-bugs)
     * [Technologies](#Technologies)
     * [Languages](#Languages)
     * [Libraries](#Libraries)
* [Testing](#Testing)
     * [Version-control](#Version-control)
     * [Deployment](#Deployment)
     * [Local Deployment](#Local-Deployment)
     * [Remote Deployment](#Remote-Deployment)
* [Acknowledgements](#Acknowledgements)
     * [External-Media](#External-Media)


# Project purpose

The purpose of this project is to be used as a personal activity log for my runs; because I am passionate about running and want to keep a daily log of set activities to track my times, distance& activity difficulty. 


## UX


### User Stories

Here are some outside user opinions on what the site should offer:

*"As a local park runner I think the platform should keep a log of my runs and I can compare with my previous runs easily, this shows me where my fitness is at."*

---

*"My name is Lucy, I would like the site to be appealing with lots of color and icons, as I find alot of activity sites to be boring."*

---

*"Hey, my name is Lebron, a professional basketball player, I think that the site should allow me to input my running activity distance and activity difficulty as this keeps a record of what I have done."*

  
  <br>
  
  As this application will be purposely designed for me as the user, this platform will:
  
- Access the platform from all my favourite devices, such as smartphones, tablets, laptops or PCs, without loss of content.

- View all Sprints on one page logged on the platform and all its details, such as description, difficulty, name, and others. 

- Add new Sprint logs on the platform.

- Update any of the logs on the platform.

- Delete any logs on the platform.

- Be able to search through all Sprint logs using a search bar.

- Filter all logs using search bar by title or description.

# Design
Since this application is meant as a personal tool for just for myself, a register and login page was not deemed necessary as this would slow down the process of logging Sprints.

The website designs are inspired by fashion site examples: 
*https://www.sitebuilderreport.com/inspiration/fashion-websites?a=ga&gclid=CjwKCAjwq_D7BRADEiwAVMDdHoGEnRu5zrH-fEWgfpOnhxGxPaq8MuHTTI8feKxabc5NvymTHEQVohoCUJ4QAvD_BwE* 
for example the welcome page which I took the idea of an full page image with a simple subtitle& button that takes the user to the main site.

This project was developed with the focus on a mobile approach first. However, with full responsiveness on other screen sizes.
I applied materialize library to all the major features of the site, which includes the cards, navigation, side-bar, input form, accordian, buttons and the footer.

A major aim of this project was to have a fun and exciting appearance, with dark orange to dark blue proving the perfect contrast. This contrast is pleasant to look at and make texts and icons(orange, white, black colors) stick out in a positive way.


### Typography

- The main fonts selected for this project is **Noto-sans** and **Oswald**. I think they are a well designed and easy to read google fonts.

------

### Colours

- The welcome page is one big image of two runners on an icy surface, the image color tone is a dull blue so I ensured the title& button stand-out, using white text& icons and the button background lights up orange and the white text turns dark blue.

- Main site the colour scheme, I used highly contrasting but equally compatible fonts alongside white texts& icons.

- The homepage cards have an orange background, both cards have an image each with a blue/teel button at the foot of each card against the white background.

- The navigation bar(create, explore and edit pages) on desktop and screen sizes above 768px the background is orange with dark blue icons, white Sprint title and a search bar which the typed text is black.

- Devices on mobile and tablet below 750px I applied a sidenav which bars are white, background color is dark blue, icons are orange and texts white plus an image at the top of 
the sidenav with dark blue sprint title. 

Read full summary of site style colorways here: *https://github.com/michodgs25/Sprint/issues/3#issue-716076941*

------

### Icons

The icons used in this project are provided by [Font Awesome 5.14.0](https://fontawesome.com/).


 ## Crud and MongoDB
   CRUD refers to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete. Persistent storage refers to any data storage device that retains power after the device is powered off. 
   
   For this project the mongoDb platform retains/stores the data when the user departs Sprint. 
   MongoDB stores data in flexible, JSON-like documents, meaning fields can vary from document to document and data structure can be changed over time. 
   
   The document model maps to the objects in the application code, making data easy to work with - https://www.mongodb.com/
   
   The CRUD method is integral to this sites functionality, with this in mind, below is the sprint platform CRUD method:
   
**CREATE** -
*The User can create a sprint log on the create sprint page and save the log to the explore sprints page.*
 
**READ** - 
*User can read every single one of their saved sprint logs on the explore sprints page.*

**UPDATE** -
*User can update a sprint log by clicking the edit button on a sprint log via explore sprints page and change the details of the log.*

**DELETE** -
*User can delete a sprint log via delete button on a sprint log via the explore sprints page, once this is clicked the log is permanently deleted.*

------

  
# Wire-Frames
These wireframes were designed with Balsamiq Mockups. Since the first version of scope, some things have changed during the development of the final version. 

A major change being the homepage cards which instead of the cards being side by, they are stacked with create sprint on top and explore sprints directly below. 

Also a major change was to not include the site logo icon and the social media symbols on the welcome page as this clashed with full page image.

Another two differences between desktop and tablet(below 768px)& mobile, which are breakpoints, which adapts features to fit various screen sizes and the implementation of a side-nav for mobile and tablet 780px& under only.

### Welcome page Desktop And Tablet& Mobile wire-frame

<details>
  <summary>Welcome page</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/sprint-home-wire.png" target="_blank" rel=""/>
     <br>
    <summary>Tablet& Mobile Welcome page</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-home.png" target="_blank" rel=""/>
</div>
</div>
  </details>
  
*Site logo and social media excluded from final product*
  
### Homepage for desktop and tablet& mobile wire-frame
  
  <details>
  <summary>Homepage</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-create-compare.png" target="_blank" rel=""/>
</div>
  </details>
  
  *Breakpoints applied to resize cards for tablet& mobile screens.
  Cards placed horizontally instead of side by side, this fits the mobile first approach.*
  
  -------------------------------------
  
  ### Create activity wire-frame
  
  <details>
  <summary>Create page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/create-activity.png"
     <summary>Tablet& Mobile Create page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-create-page.png"
         </div>
         </div>
    </details>
  
   -------------------------------------
  
  ### Explore page wire-frame
  
  <details>
  <summary>Explore page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/explore-page.png"
    <summary>Tablet& Mobile Explore page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-explore.png"
         </div>
         </div>
    </details>
  
  
   -------------------------------------
   
   ### Edit page wire-frame
   
   <details>
  <summary>Edit Sprint page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/edit-activity.png"
   <summary>Tablet& Mobile edit Sprint page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-edit-actvity.png"
         </div>
         </div>
    </details>

-------------------------

   ### Error page all screen sizes wire-frame
   
   <details>
  <summary>Error page, breakpoints again used like the homepage</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs25/Sprint/blob/master/static/wire-frame/desktop/error-page.png"
         </div>
    </details>
     
     
  *Breakpoints adapt the page to each screen size.* 
    
  ------------
    

# Features

### Welcome page feature

* *Welcome page, has a full sized background-image.*

* *In the middle of the image is the welcome page title, that encourages user to enter.*

* *Below the title is a button titled "Sprint on it", this transports user to home page.*

<details>
  <summary>Welcome page: Desktop top: Tablet left: Mobile right</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-welcome-page.jpg" target="_blank" rel=""/>
  </div>
  </details>
  
  #### Welcome page Summary: 
   - *This feature was inspired by user stories, to be appealing and landing page designs via Google Images.*
   
   ----

### Home& Create or explore Sprint cards feature

* *Adapted from the materialize library, the cards are a creative way to provide the user the two available options: Create or Explore.*

* *Both cards have an image with a button tag: "Create Sprint" and "Explore Sprints" and when button is clicked takes the user to the respective page, which is either the Create or explore.*

* *The cards have a classical look with an image, white blank middle section and button at the center bottom.*

* *The Create activity card takes the user to the create page where user can log a new activity.*

* *The Explore activities card takes the user to the explore page which displays all the previously logged activities by the user.*

<details>
  <summary>Homepage, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-homepage.jpg" target="_blank" rel=""/>
  </div>
  </details>
  
*The button is moved to the center of the card, as it looked better in that position.*
  
  #### Home page Summary:
   - *This feature was inspired by user stories, a local runner and Lucy who wanted to compare lastest run to previous activities and the site to be appealing.*
   
   ----

### Create activity feature

* *The create activity page primary purpose is for user to create and save their latest activity.*

* *The user will input personal details such as name& last name for every activity log.*

* *The title of the activity is very important as this helps locate the particular activity in database when user types in search bar on explore card or explore page.*

* *The description of the activity, allows the user to talk about the experience of doing this activity.*

* *The create page feature provides a activity difficulty select box, which the user can choose between: easy, light, moderate, hard and very hard*

* *The create page has a social media footer in which user can share activity.*

<details>
  <summary>The create activity page, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-create.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>
  
   #### Create activity Summary:
   - *Create activity page, a crucial part of this site, as this allows the user to create an activity log.*
   
   ----
   
   ### Explore activities feature

* *The explore activities feature, has all the logged sprints on one page.*

* *Each log is an accordian initially displaying just the date and title, the user can click on post and an addition box drops down which displays activity description, difficulty of activity and a edit delete post buttons.*

* *This feature has a search bar on the navigation bar, user can search through all the logged activities, nav-bar also follows the user scroll.*

* *Clicking the edit button opens up a version of the create page where user can update title, description, difficulty and the date of activity.*

* *Clicking the delete button will remove post.*

* *This feature footer has the social media links.*

<details>
  <summary>The explore activities page, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-explore.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>
  
   #### Explore activities Summary:
   - *Explore activities page is very positive feature of this site as this increases user interaction by exploring through their own activity logs.*
   
   ----
   
   ### Navigation bar and sidenav features
   
 * *The platform navigation bar is only used for the create sprint, explore and edit pages as the welcome& home page and error page have their own specific navigation.
 The point of this logic was to ensure the user sticks to the platform pathway as intended; the aim being to ensure activities are logged efficiently.*
 
* *When the platform is used via a mobile or tablet device screens 768px& below applies a sidenav which is indicated by bars burger icon and a vertical section slides out to the right. The vertical nav consists of an image with the sprint title and below it three tabs: Home, Create Sprint, Explore Sprints then below a search text input and the reset search button.*

<details>
  <summary>Navigation(top) and sidenav(bottom):</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/nav-sidenav.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>
  
  *Orange background added to sidenav search bar to increase visibility/accessibilty.*
  
----


### Search bar

* *Used on the explore page nav& sidenav to search through my saved sprint logs.*

* *This feature helps the user search through all previously logged sprints without having to labor by scrolling through them all.*

* *If for example the user would type a completely random text, that has nothing to do with any sprint logs, the platform return the nav& footer only.*

* *A reset search button is placed next to the input area, when pressed, refreshes and returns all logged sprints.*

* *Only applied to the explore page exclusively, and is hidden on the create sprint page using this piece of code below:*

`document.addEventListener('DOMContentLoaded', (event) => {
    if (window.location.pathname == '/activity/add') {
    document.querySelector('.search-form').style.display = "none";
  } else {
    document.querySelector('.search-form').style.display = "block";
  }
});`


`document.addEventListener('DOMContentLoaded', (event) => {
  if (window.location.pathname == '/activity/add') {
    document.querySelector('.side-form').style.display = "none";
  } else {
    document.querySelector('.side-form').style.display = "block";
}
});`

The above function is really help in hiding certain elements when extending base.html to multiple pages and was used to streamline the platform ensuring user stays on point, either __logging a sprint__ or __exploring previous logs.__


<details>
  <summary>Search bar</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/search.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>


-------
   
   ### Edit activity feature

* *The edit activity page primary purpose is for user to edit their already logged activity.*

* *The user can edit their logged Sprint.*

* *The edit page feature has two buttons named save changes and cancel changes.*

<details>
  <summary>The edit activity, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-edit.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>
  
   #### Edit activity Summary:
   - *Create activity page, a crucial part of this site, as this allows the user to create an activity log.*
   
 -----
 
 ### Error page feature
 
 * *If the log has been deleted, and if the log page still exists on another page, once refreshed will return this error page.*
 
 * *The page has a green button which transports the user back to the homepage.*
 
 
<details>
  <summary>The edit activity, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/error-feature.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>
  
  #### Error page Summary:
  
  * *Using a defensive programmer approach, the addition of the error page guards against any unforseen circumstance of a log still existing on a different tab after being deleted.*
 
 ------
    
   
## Features left to be implemented

Login and Register pages
* *Create both a login and register pages, to add other users to the platform.*

User profile
* *Add a user profile page, allow new users to create their own personal page on the site.*

Summary: Adding a login page was seriously considered after receiving feedback from Slack [here.](https://github.com/michodgs25/Sprint/blob/master/static/docs/Sprint_peer%20group%20feedback%20review_09102020.pdf). 
But decided against this as much of the site structure had already been built and not enough time to implement properly before the project deadline. So has been moved to future feature implementations.


----------


### Issues and bugs
*This section looks into what existing issues that are still present in the project& what future iterations could do to resolve these issues:*

*Welcome page, on the ipad pro screen the cards push to the top of screen leaving significant space below. When attempting to change this via breakpoints, this impacted other screens such as desktop. Future investigations to look at the card dimensions.*

At this point of the project there are no other errors that I can see that are to the detriment on the platform via manual testing and using google dev console.

-------
 
## Libraries

- Materialize CSS and JS Libraries: 
* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css 

* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

- Python 3.7: https://www.python.org/

- Font Awesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css

- JQuery library: https://jquery.com/ 

## Languages

  - In this project I used *HTML5*, *CSS*, *JAVASCRIPT* and *PYTHON* as programming languages.
   

## Technologies

These technologies helped create, shape and test my code

* MongoDB - https://www.mongodb.com/: provided the database to store my Sprint logs.

* Balslamiq - https://balsamiq.com/:  provided tools to construct the wire-frames of the platform.

* W3.CSS - https://www.w3schools.com/: provided the idea to add an image to the sidenav

* JS hint - https://jshint.com/: Tested my JS code and provided feedback to increase code quality.

* W3S html& css validator - https://validator.w3.org/: Tested both my HTML& CSS code and provided feedback to improve quality.

* Pylint - https://pypi.org/project/pylint/: Used with the IDE terminal typing `pylint app.py` this returns a report of the python code.

* pep8 - http://pep8online.com/: An online python code tester, returns any errors within code inputted.

* mobiReady - https://ready.mobi/: Online app that that test whether the app is mobile ready.

* Google dev tools: found top right corner of the chrome browser, more tool then bottom option. Provided a virtual testing environment.

-------
  

## Testing

Summary: *During the development of this project, I had the experience of facing some problems, exhaustively testing the functionality of each part of the platform and managed to solve most of the problems that arose before writing this document.*

*I received help from some family and friends to do the tests on the platform resources and all the problems presented were solved without problems for example my brother found that on his mobile device there was x-scroll on the create sprint page."*

__See testing documentation here: https://github.com/michodgs25/Sprint/issues/4#issue-716890135__

## Version Control
This sites version control is through github linked to the heroku app, using gitpod IDE, once completed a piece of work, I would type into the terminal:

 #### git add -A
 - *Adds a change in the working directory to the staging area.*
  
#### git commit -m "Update index.html code formatting" 
 - *Captures the state of a project at that point in time. Ensure message is specific to the changes made to the file(s).*
 
#### git push index.html
 - *This pushes the file to the github project repository.*
 
 
 ------


## Deployment


#### Requirements 
You will need the following tools installed on your system:

Python 3 - https://www.python.org/downloads/
An IDE such as Visual Studio, gitpod, Code, or like this project gitpod
An account at MongoDB Atlas - https:https://github.com/michodgs25/Sprint//www.mongodb.com/
Git - https://gist.github.com/derhuerst/1b15ff4652a867391f03


I personally used github on my local machine to develop the site using Python 3.7.3 and deployed to Heroku via Github.

1. To download or clone the site to your local machine you will need to go to my repo see steps in https://help.github.com/en/articles/cloning-a-repository .

2. Before you download or clone the site you will need to ensure you have Python 3.7 installed.

3. Once you have Python installed, created a virtual environment as appropriate to you chosen IDE and os.

4. Run the requirements.txt file as appropriate to your IDE to install the relevant required packages dependencies for the project into your virtual environment.

5. Run the app.py file as appropriate to your chosen environment and os.

6. You should now be able to view the site on your localhost on port 5000.


## Remote Deployment

#### Instructions
To deploy this app to Heroku you need to follow the steps below:

- Create a **requirements.txt** file so that Heroku can install all the dependencies required to run the app.
  `pip freeze > requirements.txt`

- Create a **Procfile** with the command:
  `echo web: python app.py > Procfile`

- In this step, you have to create a free account on the [Heroku website](https://signup.heroku.com/).
-  Login to the account, click on new and then create a new app. In the following screen, you need to give a name and choose the Europe region.
-  In the menu access the **Deploy** option, after that click on Connect to Github. Just below provide the information from the app's repository on GitHub and select the option Enable Automatic Deploy.
- On the Dashboard of the APP, click on Settings and then click on the option **Reveal config Vars**.
- Now you need to add the following variables to **Reveal config Vars**:
  - **IP**: `0.0.0.0`
  - **PORT**: `5000`
  - **MONGO_URI**: `link to your Mongo DB`
  - **SECRET_KEY**: `your chosen secret key`
- You are now ready to access the deployed app on Heroku.

<details>
  <summary>deploy heroku</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/heroku-connect.jpg" 
     target="_blank" rel=""/>
  </div>
  </details>

------

## Acknowledgements

Very Special Thanks to:
- My mentor with Code Institute **Rohit** and the code institute tech support team, who had all the patience to explain and make me understand certain concepts and peculiarities of the project .
- Family, friends, who have tested the platform on their real devices, reporting to me about any usability issues and giving improvement tips to improve the usability.

## Slack feedback

Special thanks to the valuable feedback given by slack, I implemented the feedback on navigation font-size and seriously looked into adding a login page. 
__See feedback here:


#### Read full article here - https://github.com/michodgs25/Sprint/blob/master/static/docs/Sprint_peer%20group%20feedback%20review_09102020.pdf

-----
  
 #### All code adapted is for educational purposes only and not for commercial gain.

## External Media 
All images were take from Google images advanced search with filter - __"free to use or share"__
