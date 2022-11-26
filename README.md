# Goodwill Events
<!-- Screenshot here -->
**Goodwill Events** is a fictional charity organization that produces events, such as concerts, recitals, dance performances and the like for the purpose of entertainment and most especially for charity. And, this website is created to register new members to the organization, show upcoming events, and allow reservation of desired seats for an event by members. In addition, signed-in users of the website can also like and leave comments on individual event posts.

## TABLE OF CONTENTS
* [User Experience Design (UXD)](#)
    * [Strategy](#)
        * [Main Goal](#)
        * [Target Audience](#)
        * [EPICS](#)
        * [User Stories](#)
    * [Scope](#)
        * [Planned Features](#)
        * [Design Choice](#)
    * [Structure](#)
    	* [Interaction Design](#)
    * [Skeleton](#)
        * [Data Model](#)
    * [Surface](#)
* [Features](#)
* [Fixed Bugs](#)
* [Bugs Left To Fix](#b)
* [Testing](#)
	* [Test Cases](#)
    * [Pep8 Checker](#pep8-online-checker)
* [Deployment](#)
* [Technologies](#)
* [Credits](#)
* [Acknowledgment](#)


## User Experience Design (UXD)

### STRATEGY
#### **Main Goal:**

#### **Target Audience:**

#### **EPICS:**
1. [Initial Django Setup](https://github.com/marked-gil/goodwill-events/issues/1)
2. [Heroku Setup](https://github.com/marked-gil/goodwill-events/issues/2)
3. [Data Models](https://github.com/marked-gil/goodwill-events/issues/3)
4. [Initial Templates](https://github.com/marked-gil/goodwill-events/issues/4)
5. [User Membership](https://github.com/marked-gil/goodwill-events/issues/5)
6. [Events](https://github.com/marked-gil/goodwill-events/issues/6)
7. [Event Seating](https://github.com/marked-gil/goodwill-events/issues/7)
8. [Comments](https://github.com/marked-gil/goodwill-events/issues/8)
9. [Expired Events Management](https://github.com/marked-gil/goodwill-events/issues/9)


#### **User Stories:**
Iteration 1:    
* Initial Dependencies Installation ([Epic 1](https://github.com/marked-gil/goodwill-events/issues/1))
* Basic Skeletal Structure of the Project ([Epic 1](https://github.com/marked-gil/goodwill-events/issues/1))
* Initial Deployment to Heroku ([Epic 2](https://github.com/marked-gil/goodwill-events/issues/2))
* Basic Home Page Template ([Epic 4](https://github.com/marked-gil/goodwill-events/issues/4))
* Event Model ([Epic 3](https://github.com/marked-gil/goodwill-events/issues/15))
* Basic Base Template ([Epic 4](https://github.com/marked-gil/goodwill-events/issues/13))
* Featured Events List ([Epic 6](https://github.com/marked-gil/goodwill-events/issues/6))
* All Events Page ([Epic 6](https://github.com/marked-gil/goodwill-events/issues/6))
* Specific Event's Page ([Epic 6](https://github.com/marked-gil/goodwill-events/issues/6))

Iteration 2:    
* Sign In ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Sign Out ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Member Registration ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Seating Model ([Epic 3](https://github.com/marked-gil/goodwill-events/issues/16))
* Event Seats Page ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))
* Make Event Seat Reservation ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))

Iteration 3:    
* Submission of Selected Seats for a Particular Event ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))
* Restrict Seat Reservation to Signed-in Members Only ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))
* Cancellation Reserved Seats for an Event ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))
* Event Likes ([Epic 6](https://github.com/marked-gil/goodwill-events/issues/6))
* Comment Model ([Epic 3](https://github.com/marked-gil/goodwill-events/issues/16))
* Comments Control by Site Owner ([Epic 8](https://github.com/marked-gil/goodwill-events/issues/8))
* User Comments on Upcoming Events ([Epic 8](https://github.com/marked-gil/goodwill-events/issues/8))
* Deleting Comments on Upcoming Events ([Epic 8](https://github.com/marked-gil/goodwill-events/issues/8))

Iteration 4:    
* Create Member Account Page ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Allow logged in member to edit their provided personal information. ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Allow Change of Password ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* User can reset their password ([Epic 5](https://github.com/marked-gil/goodwill-events/issues/5))
* Recycling Expired Events ([Epic 9](https://github.com/marked-gil/goodwill-events/issues/9))
* Confirmation Email for Seat Reservation ([Epic 7](https://github.com/marked-gil/goodwill-events/issues/7))
* Modify User Model ([Epic 3](https://github.com/marked-gil/goodwill-events/issues/3))

### SCOPE

#### **Planned Features**

* User Story: **Initial Dependencies Installation**
    > As a Developer, I want the significant dependencies installed first so that I can focus on the functionalities of the site later on.

    * ACCEPTANCE CRITERIA:
        * Django, gunicorn, dj_database_url, psycopg2, and dj3 cloudinary storage are all successfully installed and added to the requirements.txt.
    * TASKS:    
        * Install Django and gunicorn
        * Install dj_database_url and psycopg2
        * Install dj3-cloudinary-storage
        * Add the dependencies to the requirements.txt     

* User Story: **Basic Skeletal Structure of the Project**
    > As a developer, I can see the basic skeletal structure of the project .

    * ACCEPTANCE CRITERIA:
        * The new django project and first app are created and migrated.
    * TASKS:
        * Create the new django project
        * Create initial apps - events
        * Add the apps to the installed apps in settings.py

* User Story: **Initial Deployment to Heroku**
    > As a developer, I can initially deploy the basic and skeletal structure of the project to Heroku so that I can check the initial successful connection to Heroku.

    * ACCEPTANCE CRITERIA:
        * Initial deployment of the project to Heroku is successful.
        * PostgreSQL and Cloudinary are set up.
    * TASKS:
        * Create a new Heroku app
        * Use PostgreSQL
        * Create and set up the env.py
        * Set up the Cloudinary
        * Update Heroku Config vars
        * Update the settings.py
        * Create the directories: media, static, templates
        * Create Procfile
        * Deploy to Heroku

* User Story: **Basic Base Template**
    > As a Developer, I can use an initial base template so that I connect it to other html pages and do initial testing.

    * ACCEPTANCE CRITERIA:
        * The base template is initially set up with header and footer.
    * TASKS:
        *  Create a base template.
        * Create a header with navbar and site name or logo
        * Create a footer that contains the site name, contact details, and social media links.

* User Story: **Basic Home Page Template**
    > As a Developer, I can use a basic home page for the initial creation of the site so that I can initially check if the base template can connect successfully to other pages.

    * ACCEPTANCE CRITERIA:
        * The basic home page template is initially set up and linked with the base template
    * TASKS:
        * Create a basic home page
        * Connect the base template to the basic home page


* User Story: **Event Model**
    > As a Developer, I can save new events into a database table so that I can use the data on the website.

    * ACCEPTANCE CRITERIA:
        * The event model is constructed with fields such as title, slug, blurb, event_date, event_time, content, featured_image, author, entered_by, created_on, updated_on, likes, and etc.
        * The Event model is available on the admin panel.
    * TASKS:
        * Create an Event Model with fields such as: title, slug, blurb, event_date, event_time, content, featured_image, author, entered_by, created_on, updated_on, likes, etc.
        * Modify the built-in string method of Django’s base Model class
        * Install Summernote and use it for the post_content on Event Model
        * Customize the admin interface for the Event class Model
        * Register the Event model in admin.py

* User Story: **Seating Model**
    > As a developer, I can save the seat reservation of a signed-in member on the database so that I can block the specific seat/s of the event for the specific member.

    * ACCEPTANCE CRITERIA:
        * The seating model is constructed with fields such as 'event', 'seat_location', 'reserved_on', and 'reserved_by'.
        * The Seating model is available on the admin panel.
    * TASKS:
        * Create Seating app
        * Create VenueSeat Model
        * Create EventSeating Model with fields such as event, seat_location, reserved_on, and reserved_by
        * Modify the built-in string method of Django’s base Model class
        * Register the VenueSeat and EventSeating models in admin.py

* User Story: **Comment Model**
    > As a developer, I can save the user’s comments into the database so that I can display it in its specific event post.

    * ACCEPTANCE CRITERIA:
        * The comment model is constructed with fields such as text_comment, author, event_post, and posted_on.
        * The Comment model is available on the admin panel
    * TASKS:
        * Create a Comment Model with fields such as text_comment, author, event, and posted_on
        * Modify the built-in string method of Django’s base Model class
        * Register the Comment model in admin.py

* User Story: **Member Registration**
    > As a user, I can sign-up on the website so that I can be a member and use the full functionality of the website.

    * ACCEPTANCE CRITERIA:
        * GIVEN that a registration template is made, WHEN it is opened THEN the registration form - which includes fields for the username, first name, last name, email address, and password - shows up.
        * GIVEN that the registration form is present, WHEN the form is submitted with invalid formats on any of the fields THEN the form is not submitted and a feedback message shows up.
        * GIVEN that the registration form is present, WHEN password is created by the user THEN it will be required to re-enter the same password before the form can be submitted.
        * GIVEN that the registration form is validly completed, WHEN the form is submitted, THEN the user is redirected to the home page.
    * TASKS:
        * Create a registration template
        * Create a form that includes fields for username, first name, last name, email address, and password
        * Validate the form when submitted; and if it is invalid, redirect to the same page and show a feedback message
        * Prevent the submission of the form when the password is not re-entered correctly, and show a feedback message to the user
        * Redirect the user to the home page when registration is validly submitted

* User Story: **Sign In**
    > As a user, I can sign in when I am registered so that I can access the full functionality of the website.

    * ACCEPTANCE CRITERIA:
        * GIVEN the ‘sign in’ form is created and the user is registered, WHEN the user signs in with the required valid username or email address and password THEN the user can access the full functionality of the website.
        * GIVEN the ‘sign in’ form is created, WHEN the user signs in with invalid credentials THEN feedback message is displayed and the form is not submitted.
    * TASKS:
        * Create a ‘sign-in’ page
        * Create a 'sign-in' form that requires the user’s username and password
        * Redirect the user to the home page when sign-in is successful
        * Flash feedback message when sign-in credentials are invalid

* User Story: **Sign Out**
    > As a user, I can sign out when I am already signed in so that I can protect my website account and prevent unauthorised persons from using it.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is signed in, WHEN the user clicks the sign-out button THEN the user’s session is ended and access to the site is limited to its content that is for general consumption.
        * GIVEN the user is redirected to the home page, WHEN client is signed out successfully THEN the user is redirected to the home page and a feedback message is shown.

    * TASKS:
        * Create a sign-out link on the navbar
        * Redirect to the home page when the sign-out link is clicked
        * Flash a feedback message on the home page when the user is signed out successfully

* User Story: **Featured Events List**
    > As a user, I can see the featured list of events on the home page so that immediately see the events that are coming up.

    * ACCEPTANCE CRITERIA:
        * GIVEN home page is created, WHEN the user visits the home page THEN they can see a list of the featured events.
        * GIVEN featured list of events is displayed, WHEN the user clicked a featured event THEN the full details of the event will be displayed on a separate page.
    * TASKS:
        * Display the upcoming 3 - 4 events on the home page
        * Show title, short description, date and time
        * Add a button for every featured event that redirects to the event's full detail page.

* User Story: **All Events Page**
    > As a user, I can See all the upcoming events so that I can decide which one interests me.

    * ACCEPTANCE CRITERIA:
        * GIVEN template for all events is created, WHEN user visits the ‘all events’ page THEN they can browse all the upcoming events
        * GIVEN the user is visiting the ‘all events’ page, WHEN user clicks an event THEN the site attempts to redirect to another page.
    * TASKS:
        *  Create a template for all the upcoming events
        * Display all the upcoming events in ascending order based on the date of the event
        * Make each event item a clickable element that redirects to another URL
        * Develop pagination

* User Story: **Specific Event’s Page**
    > As a user, I can view the full detail of the event so that I can learn more about the event.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is on the home page or ‘all events’ page, WHEN the user clicked an event THEN the full details of the event will be displayed on a separate page.
    * TASKS:
        *  Create event template
        * Display the featured banner image of the event
        * Display the description or writeup about the event
        * Display the date and time of the event
        * Add a ‘reserve seat’ button to the event’s page

* User Story: **Event Likes**
    > As a user, I can like an event post that interests me so that I can show my support for the event.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is signed in and visiting the event’s page, WHEN the user clicks the ‘like’ button THEN it will add to the number of likes of the event post.
        * GIVEN the user is signed in and visiting the event’s page, WHEN the user clicks again the ‘like’ button THEN it will remove their like of the post and update the displayed number of likes of the event post.
    * TASKS:
        * Create a ‘like’ toggle button on the event’s page
        * Display the number of likes of the event post
        * Add the user’s like to the total likes of the event and display it
        * Allow user to remove their ‘like’

* User Story: **Event Seats Page**
    > As a user, I can visit the seating page so that see the available seats I can reserve.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is signed in, WHEN the user visits the seating page THEN the seat map is displayed.
        * GIVEN the user is signed in, WHEN the user visits the seating page THEN the event’s title, date, and time are displayed.
    * TASKS:
        * Create ‘seating page’
        * Add the seat map on the ‘seating page’
        * Allow the seat map to pan and zoom
        * Display the event’s title, date, and time
        * Display the colour legend for the seat map

* User Story: **Restrict Seat Reservation to Signed-in Members Only**
    > As a user, I can register as a member and sign in so that I can reserve seats.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is not signed in, WHEN they visit the seating page THEN they are still able to see the seat map and the available seats.
        * GIVEN the user is not signed in, WHEN they attempt to make a reservation THEN they are redirected to the sign-in page with a flash feedback message.
        * GIVEN the un-signed-in user has been redirected to the ‘sign-in’ page from the seating page, WHEN the user signed in THEN the user is redirected back to the seating page.

    * TASKS:
        *  Redirect the user to the sign-in page when the un-signed-in user attempts to book a reservation
        * Flash a feedback message to the user to sign in when redirected to the sign-in page
        * Redirect the user back to the seating page after signing in

* User Story: **Make Event Seat Reservation**
    > As a user, I can reserve a seat so that I can choose the available seat I want and ensure I have a seat during the event.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is signed in, WHEN I clicked on the available seat on the map THEN it shows on the screen that the user has selected it.
        * GIVEN the user has selected a seat/s, WHEN the user clicks or toggles again on the selected seat/s on the seat map THEN the seats are de-selected.
    * TASKS:
        * Make all available seats active on the seat map and can be toggled
        * Display all unavailable seats as inactive items on the seat map
        * Allow only 2 seats to be reserved per member
        * List all selected seats on the screen
        * Allow de-selection of the seat

* User Story: **Submission of Selected Seats for a Particular Event**
    > As a user, I can submit the selected seat/s so that I can ensure that it is reserved.

    * ACCEPTANCE CRITERIA:
        * GIVEN the signed-in user has selected a seat/s, WHEN I click on the ‘reserve’ button THEN the seats are saved to the database and reserved.
    * TASKS:
        * Add a ‘reserve’ button to proceed with the reservation
        * Save selected seats in database
        * Display a flash message on the seating page when a seat is successfully reserved

* User Story: **Cancellation of Reserved Seats for an Event**
    > As a user, I can cancel my reserved seats so that other users can reserve the seats.

    * ACCEPTANCE CRITERIA:
        * GIVEN the signed-in user has selected a seat/s, WHEN I click on the ‘cancel’ button THEN the selected seat/s are de-selected on the map.
        * GIVEN the user has already reserved a seat/s for an event, WHEN the user visits the event’s seating page THEN the selected seats are displayed.
        * GIVEN the user has already reserved a seat/s for an event, WHEN the user clicks on the ‘Update my reservation’ button THEN the reserved seats can be cancelled and/or replaced.
    * TASKS:
        * Add a ‘cancel’ button to remove the selected seat/s
        * Add an ‘Update my reservation’ button’ to allow the cancellation and/or replacement of the reserved seats.
        * Remove the ‘reserve’ button when the user already has reserved seat/s, and show the list of seats reserved.
        * Allow reserved seats to be cancelled
        * Add an ‘update reservation’ button is clicked.
        * When the ‘update’ button is clicked, the 'seating' database is updated and a feedback message is flashed

* User Story: **User Comments on Upcoming Events**
    > As a user, I can leave a comment on the event page so that I can share my thoughts with the public about a particular event.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is signed-in, WHEN I add a comment on an event page THEN it will be saved in the database.
        * GIVEN the number of text characters for each comment is limited, WHEN the user adds a comment on an event page THEN the number of characters left is displayed in real-time.
        * GIVEN the user is visiting an event's page, WHEN the user scrolls down to the comment section THEN they can see the comments from members.
    * TASKS:
        * Create a form for comments on each page
        * Limit the comment length to 250 characters
        * Show realtime character counter for comments
        * Save the comment to the database when the ‘submit’ button is clicked
        * Display the comments on the event’s page along with the author's first name and initial of their last name, and the date and time of posting

* User Story: **Deleting Comments on Upcoming Events**
    > As a user, I can delete my comments on a particular event so that they are no longer visible to the public.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user has posted a comment, WHEN the author of the comment is signed-in THEN they are allowed to delete their comments.
    * TASKS:
        * Add a ‘delete’ button on the user’s comment when signed-in
        * Delete the comment when the ‘delete’ button is clicked

* User Story: **Comments Control by Site Owner**
    > As a site owner, I can delete the comments of members so that the site is kept friendly and safe for all users.

    * ACCEPTANCE CRITERIA:
        * GIVEN an inappropriate comment is posted by a user, THEN the site owner can deliberately delete the comment without notice.
    * TASKS:
        *  Delete an inappropriate comment through the admin panel

* User Story: **Recycling Expired Events**
    > As a site owner, I can set an expired event to automatically be recycled to a new scheduled date so that the site can perpetuate despite its contents not being monitored and updated manually.

    * ACCEPTANCE CRITERIA:
        * GIVEN that this site is for educational purposes only and the events may not be monitored or updated regularly, WHEN an event has gone past its schedule THEN it will automatically be rescheduled to a future date.
        * GIVEN that the event has gone past its schedule, WHEN the event is automatically recycled with a new date THEN it is re-displayed with all the other events in the order of their dates.
        * GIVEN that the event has gone past its schedule, WHEN the event is automatically recycled with a new date THEN all its previously reserved seats are deleted for a new start.
    * TASKS:
        * Automatically update the schedule of the event in the database to the following year as soon as it expires
        * Re-display the recycled event with the new schedule
        * Delete all reserved seats for the expired and recycled events

* User Story: **Create Member Account Page**
    > As a User, I can view all of my personal information/data as a registered member so that I review them as needed.
    
    * ACCEPTANCE CRITERIA:
        * GIVEN that I am registered to the site, WHEN I log in THEN I can view all my personal information/data that I have provided to the site.
        * GIVEN that I am registered to the site, WHEN I click on the Member Account Page THEN I will be able to see my registered username, first name, last name, and email
    * TASKS:
        * Create A Member's Account page
        * In the Member's Account page, display the username, first name, last name, and email of the user.

* User Story: **Allow logged in member to edit their provided personal information**
    > As a User, I can edit my personal information/data such as first name, last name, and email address so that I can update them easily as necessary.

    * ACCEPTANCE CRITERIA:
        * GIVEN the user is logged in and inside the Member's Account page, WHEN I edit my personal information/data THEN they are allowed to edit their provided personal information as they see fit.
        * GIVEN the user has edited a specific personal information (eg, first name), WHEN I click save THEN the specific field will be updated in the database.
    * TASKS:
        * Create an edit button for each personal info field
        * Update the database when an edited personal info is saved
        * Do not allow username to be changed.

* User Story: **Allow Change of Password**
    > As a User, I can change my password so that I can maintain the security of my account.
    
    * ACCEPTANCE CRITERIA:
        * GIVEN the user is a logged in member, WHEN they click on 'Change Password' inside the Member's Account page THEN it will allow them to change their password.
        * GIVEN the user has entered a new and verified password, WHEN they click 'save' THEN the database will be updated.
    * TASKS:
        * Create a 'Change Password' button inside the Member's Account page
        * Verify the new password the user entered by asking them to re-enter the same password.
        * Update the database when the new password is verified and saved.

* User Story: **User Can Reset their Password**
    > As a User, I can reset my password so that I can either keep my account secured or keep using my account when I have forgotten my password.

    * ACCEPTANCE CRITERIA:
        * GIVEN that the user is logged in and has provided a valid email address, WHEN they visit the Member's Account page and click on the 'change my password' link an email will be sent to the user to enable them to change his password.
        * GIVEN that the user has previously registered and has provided a valid email address, WHEN they click on 'forgot password?' link inside the Sign In page THEN an email will be sent to user to enable them to change their password.
    * TASKS:
        * Add a 'change my password' link inside the Member's Account page and redirect it to the password reset page
        * Add a 'forgot my password?' link inside the Sign In page and redirect it to the password reset page
        * Send an email to the user with a link to enable them to change their password

* User Story: **Confirmation Email for Seat Reservation** [NOT IMPLEMENTED]
    > As a user, I can receive a confirmation email for my seat reservation so that I can ensure that my seat reservation to an event is confirmed.

    * ACCEPTANCE CRITERIA:
        * GIVEN that the user has selected their seat/s, WHEN they click the ‘reserve’ button THEN an automatic email will be sent to the user as confirmation.
        * Set up automatic email function
        * Display a flash message to the user that a confirmation has been sent to his email
    * TASKS:
        * Set up automatic email function
        * Display a flash message to the user that a confirmation has been sent to his email

* User Story: **Modify User Model** [NOT IMPLEMENTED]
    > As a developer, I can add other fields in the User model in addition to those that are built-in so that customize the sign-up and sign-in feature of the site.

    * ACCEPTANCE CRITERIA:
        * The User modal is modified to include the telephone_number field, etc.
        * All the fields in the User Model cannot be left blank and will raise a validator error if attempted.
        * The added fields to the User model are available on the admin panel.
    * TASKS:
        * Modify the User model to include: telephone_number, and/or etc
        * Require all fields in the User Model

#### **Design Choice**

## Features

## Fixed Bugs

## Bugs Left To Fix

## Testing

## Deployment

## Technologies

## Credits

## Acknowledgment