# CS50Capstone
PROJECT TITLE": CAPSTONE PROJECT FOR CS50'S WEB PROGRAMMING WITH PYTHON AND JAVASCRIPT
NAME OF WEBSITE - RATEIT

DESCRIPTION OF PROJECT
RATEIT is an online recommendation platform which allows users to sign up and register to use the service. Logged-in users are then allowed to register their own businesses to the website and have them rated by other users who register on the platform. Users are only allowed to rate the business once after which they are unable to re-rate the business. Users are also allowed to make comments to a business page which they can edit if they are unsatisfied with it.

PROJECT REQUIREMENTS
RATEIT fulfills all the requirements detailed for this course. A summary of which is listed below:
1. This project is distinct from other projects in the CS50W course as it is not a social network or e-commerce platform. 
2. The project has 5 distinct models in its design and utilizes JavaScript in the front-end, including for editing comments posted.
3. The design of the website is mobile responsive with corresponding CSS properties.

PROJECT DETAILS - RUNNING THE APPLICATION
To begin using the application, a person must make profile using the 'register' link at the top of the screen. After registration, the user is taken to the homepage where he/she is allowed to register a new business. They can supply an image to their business posting as well as other details. Ratings out of 10 are then made to each individual business listing as well as any associated comments. The average rating from all users is then aggregated and displayed next to the name of the business on the webpage. Note each user can only rate the business once after which a message will display saying they have already rated this business. This is to prevent a user from rating a business multiple times in hopes of artificially altering its score. 

Each user has a profile page which can be accessed by clicking their name shown on the top of the screen. There they will see their profile picture as well as any businesses they have registered on the website. Clicking on any of those business names will take them to their business' webpage where their average rating is visible at the top of the screen. Users who are logged in will also see 'edit' buttons near each comment they have made allowing them to edit comments they have made to each business. 

FILE DESCRIPTION
Templates folder: HTML documents which render various pages including the user's profile page, a business' page, registration and login page's etc.
Static folder: Contains a CSS file for editing the look of DOM elements on the page. Also contains the javascript file 'main.js' for implementing the JavaScript logic on the page. 
Media Folder: Contains all the media file uploads for the website including those for profile pictures and business images.
