# SpringSpeegle 2024 Project Instructions

This README assumes that you have followed and setup the initialREADME.md project environment.
Additionally, the database assumes you have the SQLStart.bat and SQL.bat opened and running using the database setup instructions shown 
at https://cs.baylor.edu/~speegle/3335/install.html

## Instructions

1. Install Email Dependencies

You may have to install flask-mail and pyjwt for email and password functionality. This can be done as follows!
```bash
pip install flask-mail
pip install pyjwt
```

2. Setup SpringSpeegle Database

In the SQL.bat terminal, please first run the SQLInit.sql file. This will create the database schema and set it to use.
To populate this database, in the SQL.bat terminal, run the SpringSpeegle.sql file.
Both of these sql files are located in the Sql_Scripts directory

3. Apply Migrations

Apply the most up to date flask migrations for the project using the following command
```bash
flask db upgrade
```

4. Run Project

You can then start the project using the following command.

```bash
flask run
```
The results of the command should display a link to the domain where the website can be interacted with

# Admin Login
To login as an administrator, use the following login information
User: TheSpeegle
Password: BaseballRocks
This User can view admin information as already has their favorite team set to the Detroit Tigers for your leisure.

# Extra Credit Functionality List
* Error Control for User Login and Registration
* Navigation Bar UI
* Music and Baseball Design Theme
* Password Reset Request Functionality
* Email Functionality via Password Reset Request
* Favorite Team for a user being chosen, saved, and updated in real time in their Profile Page
* Team Logos being displayed for all current MLB teams (as of 2023)
* Routing Web Page Protection (A logged in User cannot access the registration page, a logged out user cannot access Teams, navigation bar updated in real time, etc.)
* Backend routing page interactivity (Rather than repeated sql calls, Data is queried once, saved, then passed between pages utilizing the Form Classes in Forms.py. See also routes.py and templates directory)
* Browser Tab Title and Description on Hover
* Creation of Sacred Speegle Tesseract on home page crafted by the finest of artisans




