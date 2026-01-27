FLASK PROJECT
-This is a personal project that will help me understand Python, web dev, and AI more. For now, I don't know what this project will entail but I am deteremined to get better
at development. My main goal with this project is to show the skills i developed throughout this project's journey.

Day 1 (Jan 23, 2026)
-I started the beginnings of a Flask project. I will be using simple HTML and CSS for the pages along with Bootsrap for page features. I began installing the necessary programs like pip,
Flask, and Python3 to my computer. After, I created a simple Flask that just outputs two pages, 'Home' and 'About'. I added a nav bar using Bootstrap. Edited the nav bar where, depends
on what page the user is on, will make the title of the page in the nav bar bold and have other page titles dimmed. For example, if a user is on the 'Home' page, the 'Home' text on
the nav bar will be bolded and the 'About' text will be dimmed. If the user clicks on the 'About' link, then the 'About' text will be bolded and the 'Home' text will be dimmed. I also
added partials to the project. This was something I remmeber learning in my Web Dev course I took in college. It makes managing reccuring elements in a page easier. The first day does
not have much but it's a good start to the project.

Day 2 (Jan 26, 2026)
- Over the weekend, I worked on the Login and Register pages for the app. I also set up a SQLite database using SQLAlchemy for now. Later I would like to upgrade the database to Supabase or PostgreSQL. For now, I just wanted a simple DB to store the users. For the DB schema, I have a simple User table with username, email, and password_hash fields. For password security, I hash the passwords using werkzeug's password hashing before storing them in the database. During login, I compare the hashed password with the submitted password to authenticate users. I also integrated Flask-Login to manage user sessions, when a user is signed in, Flask-Login creates a session for them during their time on the app. When the session expires or they logout, the user is redirected back to the login page. I also added a .env file to store the secret key for Flask's session management. I used Python's secrets module to generate a secure random key. I then added the .env file to the .gitignore so the secret key won't be pushed to GitHub. I successfully fixed a bug where the login route had an indentation error that was preventing user authentication. Users can now register, login, and be redirected to the main homepage.
-Update: Fixed the routing bug. The issue was in the nav bar. when clicking on 'Home' it will take the user back to the sign-in page. Changed the route from 'home' to 'index' to take users to the main page.
