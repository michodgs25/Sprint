<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/images/readme/banner.jpg" 
     target="_blank" rel="noopener" alt="Sprint">
</div>
<h2 align="center">Sprint</h2>

### Track your workouts one sprint at a time!

*Keeping fit by running or walking is popular amongst millions of people across the entire globe from your local park to the olympic games.* 
*An essential part of increasing an individuals fitness and the ability to objectively gauge their own fitness is logging activity times, intensity, and factors such as surface& weather.* 

*With this in mind the Sprint platform was designed with the main purpose of being a tool that allows the user to log their walking or run activities with ease anywhere and on any device. Sprint wants to make possible for the user to manage their every single log on the platform, such as changing the activity name, changing their difficulty preference or even deleting that Sprint log altogether.*

#### You can visit the Sprint platform [here.](https://flask-sprint-project.herokuapp.com/)

  - Site mobile demo: *https://www.youtube.com/watch?v=j5vqz2_EDUA*

## Contents

* [UX](#UX)
* [User-Stories](#User-Stories)
 * [Project purpose](#Project-purpose)
* [Wire-Frames](#Wire-Frames)
 * [CRUD](#CRUD)
 * [Features](#Features)
 * [Technologies](#Technologies)
 * [Testing](#Testing)
 * [Version-control](#Version-control)
 * [Deployment](#Deployment)
 * [Project-barriers-and-the-solutions](#Project-barriers-and-the-solutions)
 * [issues-and-bugs](#issues-and-bugs)
 * [Acknowledgements](#Acknowledgements)
 * [External-Media](#External-Media)


## Project purpose

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

- Filter all logs using search bar by title or

## Design
The website designs are inspired by fashion site examples: 
*https://www.sitebuilderreport.com/inspiration/fashion-websites?a=ga&gclid=CjwKCAjwq_D7BRADEiwAVMDdHoGEnRu5zrH-fEWgfpOnhxGxPaq8MuHTTI8feKxabc5NvymTHEQVohoCUJ4QAvD_BwE* 

for example the welcome page which I took the idea of an full page image with a simple subtitle& button that takes the user to the main site.

This project was developed with the focus on a mobile approach first. However, with full responsiveness on other screen sizes.
I applied materialize library to all the major features of the site, which includes the cards, navigation, side-bar, input form, accordian, buttons and the footer.

The main idea for the design of this project was to have a fun and exciting appearance, with dark orange to dark blue proving the perfect contrast. This contrast is pleasant to look at and make texts and icons(orange, white, black colors) stick out in a positive way.


### Typography

- The main fonts selected for this project is **Noto-sans** and **Oswald**. I think they are a well designed and easy to read google fonts.

------

### Colours

- The welcome page is one big image of two runner on icy surface, the image color tone is a dull blue so I ensured the title& button stand-out, using white text& icons and the button background lights up orange and the white text turns dark blue.

- Main site the colour scheme, I used highly contrasting but equally compatible fonts alongside white texts& icons.

- The homepage cards have a orange card-panel background, both cards have an image each with a blue/teel button at the foot of button against the white background of the cards.

- The navigation bar(create, explore and edit pages) on desktop and screen sizes above 780px the background is orange with dark blue icons, white Sprint title and a search bar which the typed text is black.

- Devices on mobile and tablet below 750px I applied a sidenav which bars are white, background color is dark blue, icons are orange and texts white plus an image at the top of 
the sidenav with dark blue sprint title. 

Read full summary of site colorway here: *https://github.com/michodgs25/Sprint/issues/3#issue-716076941*

------

### Icons

The icons used in this project are provided by [Font Awesome 5.14.0](https://fontawesome.com/).

  
## Wire-Frames
These wireframes were designed with Balsamiq Mockups 3. The first version of scope and some minor things have changed during the development for the final version. 
A major change being the homepage cards which instead of the cards being side by, they are stacked with create sprint on top and explore sprints directly below. 
Also a major change was to not include a icon on the welcome page as this clashed with full page image.

Another two differences between desktop and tablet(below 768px)& mobile, which are breakpoints, which adapts features to fit various screen sizes and the implementation of a side-nav for mobile and tablet 780px& under only.

### Welcome page Desktop

<details>
  <summary>Welcome page</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/sprint-home-wire.png" target="_blank" rel=""/>
</div>
  </details>
  
### Mobile welcome page and tablet width 768px and lower

<details>
  <summary>Tablet& Mobile Welcome page</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-home.png" target="_blank" rel=""/>
</div>
  </details>
  
### Homepage for desktop and tablet& mobile 
  
  <details>
  <summary>Tablet& Homepage</summary>
  <br>
<div align="center">
<img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-create-compare.png" target="_blank" rel=""/>
</div>
  </details>
  
  *Breakpoints applied to resize cards for tablet& mobile screens.*
  
  -------------------------------------
  
  ### Create activity page
  
  <details>
  <summary>Create page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/create-activity.png"
         </div>
    </details>
  
  ### Mobile create activity page and tablets width 768px and lower
  
  <details>
  <summary>Tablet& Mobile Create page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-create-page.png"
         </div>
    </details>
  
   -------------------------------------
  
  ### Explore page
  
  <details>
  <summary>Explore page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/explore-page.png"
         </div>
    </details>
  
  ### Mobile Explore page and tablet width 768px and lower
  
  <details>
  <summary>Tablet& Mobile Explore page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-explore.png"
         </div>
    </details>
  
  
   -------------------------------------
   
   ### Edit page desktop
   
   <details>
  <summary>Edit Sprint page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/desktop/edit-activity.png"
         </div>
    </details>


   ### Edit page mobile and tablet width of 768px and lower
   
   <details>
  <summary>Tablet& Mobile edit Sprint page</summary>
  <br>
  <div align="center">
    <img src="https://github.com/michodgs24/Sprint/blob/master/static/wire-frame/mobile/mobile-edit-actvity.png"
         </div>
    </details>

-------------------------

## Features

### Welcome page

* *Welcome page, has a full sized background-image.*

* *In the middle of the image is the welcome page title, that encourages user to enter.*

* *Below the image is a button titled "Sprint on it", this transports user to create or explore home page.*

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

* *The Create activity card takes the user to the create page where user can log a new activity.*

* *The Explore activities card takes the user to the explore page which displays all the previously logged activities by the user.*

<details>
  <summary>Homepage, Desktop top: Tablet left: Mobile right</summary>
<div align="center">
<img src="https://github.com/michodgs25/Sprint/blob/master/static/images/readme/sprint-homepage.jpg" target="_blank" rel=""/>
  </div>
  </details>
  
  #### Home page Summary:
   - *This feature was inspired by user stories, a local runner and Lucy who wanted to compare lastest run to previous activities and the site to be appealing.*
   
   ----

### Create activity feature

* *The create activity page primary purpose is for user to log their latest activity.*

* *The user will input personal details such as name& last for every activity log.*

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

* *This feature footer has the social media links and sprint icon. User learn more about sprint and share sprint to social media.*

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
   
   
   ## Crud
   CRUD refers to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete. Persistent storage refers to any data storage device that retains power after the device is powered off.
   
   With this in mind below is the sprint platform CRUD method:
   
**CREATE**
*The User can create a sprint log on the create sprint page and save the log to the explore sprints page.*
 
**READ**
*User can read every single one of their saved sprint logs on the explore sprints page.*

**UPDATE**
*User can update a sprint log by clicking the edit button on a sprint log via explore sprints page and change the details of the log.*

**DELETE**
*User can delete a sprint log via delete button on a sprint log via the explore sprints page, once this is clicked the log is permanently deleted.*
   
   
## Features left to implement
   - Summary *"This site starts as a personal tool and as improvements are made and features added to become a public tool."*
   
   * __See full article here: https://github.com/michodgs24/Sprint/issues/1#issue-675980810__ 

## Libraries

- Materialize CSS and JS Libraries: 
* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css 

* https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js

*The materialize CSS& JS libraries are the cornerstone library of this project providing the major features like the nav, sidenav, cards, accordian, footer and custom styling.*
  
- Font Awesome: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css

*Font awesome provide all the icons for this site, such as the social media icons for the footer.*
   


## Technologies

* MongoDB - https://www.mongodb.com/

* Materialize - https://materializecss.com/

* Balslamiq - https://balsamiq.com/

* JQuery library - https://jquery.com/        

* W3.CSS - https://www.w3schools.com/

* JS hint - https://jshint.com/

* W3S html& css validator - https://validator.w3.org/

* Pylint - https://pypi.org/project/pylint/

* mobiReady - https://ready.mobi/

* Google mobile friendly test- https://search.google.com/test/mobile-friendly

* Lighthouse - Find via google developer tools in browser.

* Free formatter - https://www.freeformatter.com/html-formatter.html#ad-output

## Languages

  - In this project I used *HTML5*, *CSS*, *JAVASCRIPT* and *PYTHON* as programming languages.

## Testing

Summary: *"During the development of this project, I had the experience of facing some problems, exhaustively testing the functionality of each part of the platform and managed to solve most of the problems that arose before writing this document.

I received help from some family and friends to do the tests on the platform resources and all the problems presented were solved without problems for example my brother found that on his mobile device there was x-scroll on the create sprint page."*

__See testing documentation here: https://github.com/michodgs25/Sprint/issues/4#issue-716890135__

## Version Control
This sites version control is through github linked to the heroku app, using gitpod IDE, once completed a piece of work, I would type into the terminal:

 #### git add -A
 - *Adds a change in the working directory to the staging area.*
  
#### git commit -m "Update index.html code formatting" 
 - *Captures the state of a project at that point in time. Ensure message is specific to the changes made to the file(s).*
 
#### git push index.html
 - *This pushes the file to the github project repository.*

## Deployment

#### Requirements 
You will need the following tools installed on your system:

Python 3 - https://www.python.org/downloads/
An IDE such as Visual Studio, gitpod, Code, or like this project gitpod
An account at MongoDB Atlas - https:https://github.com/michodgs25/Sprint//www.mongodb.com/
Git - https://gist.github.com/derhuerst/1b15ff4652a867391f03

## Local Deployment
The following instructions are based on use on a Windows 10 OS and IDE git Code. If your OS is different, the commands may be different, but the process, in general, remains the same.

#### Instructions

- Save a copy of the Github repository located at https://github.com/michodgs25/Sprint.
  - Unzip the repo into the chosen folder.
- If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/michodgs25/Sprint
```

- Within the chosen directory, create a virtual environment with the command:
```
python -m venv venv
```  

- Activate the virtual environment with the command:
```
.\venv\bin\activate 
```

- Install all required modules with the command: 
```
pip install -r requirements.txt
```

- Create a file called `.flaskenv` if not exists.

- Inside the `.flaskenv` file check for the following entries:
```
FLASK_ENV=development
FLASK_APP=app.py
```

- Create a `.env` file with your credentials:
e.g
```
MONGO_URI="insert your mongo URI details here"
SECRET_KEY="insert your secret key here"
```

- Create a database in MongoDB Atlas called **third_milestone_project** with a collection called **tasks**
(of course you can choose your own database& collection name)

- Run the application with the command
```
flask run
```
- Open the website at `http://127.0.0.1:5000`

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

## Project barriers and the solutions
* This section looks into the barriers that occurred during the process of this building this project and what solutions were chosen to hurdle those barriers:*

<br>

#### Navigation bar barriers& solutions - 
  
  - Summary: 
  *"The navigation....*

#### Read full article here -  

-----

#### ..... barriers& solutions - 
  
  - Summary:
  *""*

#### Read full article here - 

-----

#### ..... barriers& solutions - 
  
  - Summary:
*""*


----

#### ..... barriers& solutions - 
   
   - Summary:
   *""*
   
 #### Read full article here - 
 
 -----

## issues and bugs
*This section looks into what existing issues that are still present in the project& what future iterations could do to resolve these issues:*

* __Feature__ - 

  - Summary 
  *""*

#### Read full article here - Feature

-----

* __feature__ -  

  - Summary 
  *""*

#### Read full article here - 

-----

* __Navigation__ -

  - Summary 
  *""*
  
#### Read full article here - 

-----

## Acknowledgements

Very Special Thanks to:
- My mentor in Code Institute **Rohit ** who had all the patience to explain and make me understand certain concepts and peculiarities of the project content.
- All people, including family, friends, who have tested the platform on their real devices, reporting to me about any usability issues and giving improvement tips to improve the usability.
  
 #### All code adapted is for educational purposes only and not for commercial gain.

## External Media 
All images were take from Google images advanced search with filter - __"free to use or share"__
