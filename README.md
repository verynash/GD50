# Final Project - ZJC Custom Kicks Store Page
## Video Demo:  <https://youtu.be/nOCLPb5hNsg>
## Description:
This project was set to be a big task for me. I am currently military and looking to have some skills prepared when I get out in a few months. My sister is an artist, and recently started her own business. I decided that an excellent use of this project would to be to develop a template for a store website she could use if she decided to get her own domain and upkeep a virtual shop.

## Tools and Creation
### Languages and Tech
In order to create a fully functional website, I used five major formats:
- HTML, for the basic layout of the site
- Javascript, for functionality
- CSS, for design
- Python, for functionality
- SQL, for storing user information and inventory information

Aside from those, I included pictures as .jpg and .png files, a .txt file for the requirements, and this .md file.

### Sessions
This page has users, and uses sessions to remember that user. The goal is to eventually set up the ability to email directly from the site, but being new to coding I found that it would be a bit too large an endeavor for me to take on at this point.

### Improvements
This page is good as a starter. It has the basic layout and important structures for ecommerce. The next step is to include .php functionality so that I can add in an email option, allowing a user to email the store owner directly.

I also plan on finding a smoother design for the homepage. Of the pages, it feels the least integrated for mobile. I would like to add vertical depth and eliminate some of the issues I encountered using grids.

## Design
### Color Scheme
I decided on the color scheme for the site when I was looking through my sister's portfolio. She had a shoe that was silver and red, with Ali and Mike Tyson each on a shoe. I knew immediately that using a silver/gray background with red/black as accents would create a slick, cool feel to the store. I let that become the main theme for the site, while leaving the background of the navbar white so it was more clear and distinct from the body of the site.

### homepage.html

Though the first thing you see, the homepage was the last page I worked on. I found that it was most feasible to design the homepage after I knew where my links would be going, and what images I would have available to fill up the page. In the end I decided that the two most important pages to visit would be the page displaying the portfolio of custom shoes that have already been sold, and the page showing what is available for sale at the moment.

For each of those pages I added a few images of works that stood out. The goal is to grab the attention of the user and draw them deeper into the site.

I also added a link to the facebook page for ZJC Custom Kicks, and will add any additional social media pages later created to the homepage.

### kicks.html

The kicks page is fairly simple. I make sure to let the user know immediately that none of these shoes are for sale, they have already been made and sold.

After that I created a gallery with a bunch of custom shoes that are finished. They increase in size when you hover, and you can click on each image to bring up a full size image. I wanted this page to be clear, and to look cool. This is what will bring in interest for those who might want to design their own shoes.

### apparel.html

The apparel page is for everything wearable other than shoes. This page shows some of the different types of clothing that can be worked with. It also shows a branded sweatshirt and a custom painted dress shirt. It isn't the main attraction of the store, but it does offer a way to rep the brand. It also lets you know that if you want to step outside of the box, you can really get creative with your order.

### rts.html

Th Ready to Sell page is a lot like the Kicks page, but it has a link to the order page attached to a label for each pair. This will only be updated with shoes that have been made already and haven't yet been sold.

### aboutme.html

Every young entrepreneur needs to share a little bit about themselves. This page is a brief introduction that my sister put together. It talks about her life and family, and her excitement to begin expanding her new business.

### order.html

The order page was one of the tougher pages to decide how to design. Initially, I wanted a user to be able to email my sister directly from the site. After multiple attempts that either caused large user interface issues or downright failed, I scrapped the idea. Instead, there is a list of all of the starting prices for her inventory, and her email will be listed in order to contact and create an order. As it is still a small personalized business, she does not have a formal ordering system and is personally involved in each transaction. Users must be logged in to view this page, to avoid spammers overflowing the inbox. I have not listed her actual email as this is a development page, and not a production environment.

### layout.html

This file sets up the basic framework for the site. It includes:
- navigation bar, responsive to a user being logged in or not
- a placeholder for the other pages to be plugged into
- a footer that allows the user to scroll up and return to the homepage, as well as a copyright for the business.

### login.html

This is the basic login page. It links to the register page, and returns apology.html if there is an issue. It requires an account be registered.

### apology.html

This page gives an error message and then has the login page rerendered.

### register.html

This page allows a user to create an account. It requires a unique username, an email and a password, which must be confirmed. If any errors occur, it redirects to apology2.html. Otherwise, the password is hashed and the username, email, and password hash are stored in a database.

### apology2.html

This page returns an error message and rerenders the register page.

### styles.css

This is the CSS style page for the website. If I continue building, I may introduce other stylesheets.

### modal.js

This javascript file allows the introduction of a modal, and allows users to click on pictures in a gallery and make them full size, along with a close button to the modal.

### app.py

The python implementation for the website. It configures the use of sessions first, and allows you to use a SQL database, ZJC.db. For the login page, it clears the session and searches the database for your login information. If there is no match, it gives an error message and renders the login again. Otherwise, it logs the user in. There is a logout function. A register function that allows you to create new users follows that. Each of the routes are defined below, and the order route requires a user be logged in.

### helper.py

This python page defines the login_required function, which requires that a user be logged in to view a page.

Then it defines a format for converting an integer to a dollar amount, which was used initially and then scrapped, but may return if I change my inventory database again.

After that are the apology functions, which will render error messages defined in app.py

### requirements.txt

This lists the required tech needed to run the site.

### ZJC.db

This is my SQL database. It includes two tables:

- users contains:
    - usernames
    - emails
    - a hash of a password

- inventory contains:
    - Types of inventory
    - size
    - prices for the different forms of artwork that can be implemented
