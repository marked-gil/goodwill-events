# TESTING

## TABLE OF CONTENTS    
* [**Manual Testing for User Stories**](#manual-testing-user-story-testing)
* [**Manual Testing for Javascript**](#manual-testing-for-javascript)
* [**Python Automated Testing**](#automated-testing-unittest)
* [**Validators**](#validators)     
    * [Python Linter](#ci-python-linter)
    * [JSHINT](#jshint)
    * [Markup Validator](#w3c-markup-validator)
    * [CSS Validator](#w3c-css-validator)
* [**Accessibility**](#accessibility)   
    * [Safari Accessibility Audit Results](#safari-accessibility-audit-results) 
    * [Color Contrast Accessibility Validator Results](#color-contrast-accessibility-validator-results) 
    * [WAVE - Web Accessibility Evaluation Tool](#wave---web-accessibility-evaluation-tool) 
* [**Lighthouse Testing**](#lighthouse-testing)
* [**Responsiveness**](#responsiveness)
    * [Mobile-Friendly Test](#mobile-friendly-test)
    * [Manual Testing for Responsiveness](#manual-testing-for-responsiveness)

### [>> **BACK TO README.MD**](https://github.com/marked-gil/goodwill-events#readme)

## MANUAL TESTING (User Story Testing)
These are the test cases for manual testing on the project's User Stories.

* **HOME Page**     
![Home Page Template test cases](docs/test_cases/test-cases-1.png)

* **FEATURED EVENTS**   
![Feature Events test cases](docs/test_cases/test-cases-2.png)

* **ALL EVENTS Page**
![All Events test cases](docs/test_cases/test-cases-3.png)

* **SPECIFIC EVENT Page**
![Specific Event Page test case](docs/test_cases/test-cases-4.png)

* **USER AUTHENTICATION**   
    Member Registration
    ![Member Registration test cases](docs/test_cases/test-cases-5.png)     
    Sign In & Sign Out      
    ![Sign In & Out test cases](docs/test_cases/test-cases-6.png)
    Editing Account Information     
    ![Editing Account Info test cases](docs/test_cases/test-cases-7.png)
    Change of Password      
    ![Chage of Password test cases](docs/test_cases//test-cases-8.png)
    Password Reset      
    ![Password Rest test cases](docs/test_cases/test-cases-9.png)

* **LIKES**
![Event Likes test cases](docs/test_cases/test-cases-10.png)

* **COMMENTS**
![Comments test cases](docs/test_cases/test-cases-11.png)

* **EVENT SEATS & RESERVATION**     
    SVG Seat Map's Panning & Zooming Feature
    ![SVG Seat Map test case](docs/test_cases/test-cases-12.png)    
    Seat Reservation
    ![Seat Reservation test cases](docs/test_cases/test-cases-13.png)     
    ![Seat Reservation test cases](docs/test_cases/test-cases-14.png)  
    Reservation Update & Cancellation
    ![Reservation Update & Cancellation test cases](docs/test_cases/test-cases-15.png)
    ![Reservation Update & Cancellation test cases](docs/test_cases/test-cases-16.png)  
    Seat Reservation Feature Restricted to Signed-In Users
    ![Seat Reservation Restriction test case](docs/test_cases/test-cases-17.png)  

* **RECYCLING EXPIRED EVENTS**
    ![Recyclign Expired Events test case](docs/test_cases/test-cases-18.png)    

* **FILTERING EVENTS BY MONTH**
    ![Filtering Events by Month test cases](docs/test_cases/test-cases-19.png)

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## MANUAL TESTING FOR JAVASCRIPT
The results of the manual tests on Javascript are shown below.

### Nav Bar Links
| Test Description | Achieved |
| ---------------- | -------- |
| Nav link is highlighted and disabled when its corresponding page is opened | Yes |

### Events Page (Upcoming Events)
| Test Description | Achieved |
| ---------------- | -------- |
| Current page's number in the pagination nav is highlighted and disabled | Yes |

### Event Details Page (Specific Event's Page)
| Test Description | Achieved |
| ---------------- | -------- |
| Character counter for the comment section tracks the number of characters left with a maximum of 250 characters | Yes |
| 'Post' button of the comment section is disabled when textarea is empty | Yes |
| Page reloads and stays on the comment section after user posted a comment | Yes |
| Page reloads and stays on the comment section after user deleted a comment | Yes |

### Member Account Page
| Test Description | Achieved |
| ---------------- | -------- |
| All input fields in the form are 'read-only' as their initial state | Yes |
| Edit button on each input field removes the 'read-only' status and allow editing of the field | Yes |
| Edit button is switched to 'X' button and vice versa when toggled | Yes |
| 'Update' button is enabled when input field value is changed, and disabled when no changes were made | Yes |

### Seat Reservation Page
| Test Description | Achieved |
| ---------------- | -------- |
| All available seats are clickable as evidence by its color change | Yes |
| All reserved seats are blocked/disabled | Yes |
| When event is fully booked, a message "This event is FULLY BOOKED" is displayed | Yes |
| User's selected seats are displayed at the footer of the page | Yes |
| The 'Reserve' and 'Update reservation' buttons are disabled by default and will only turn active when the user has selected a new seat from the seat map | Yes | 
| User's reserved seats for an event can be cancelled by clicking the 'X' button of the seat number, then the 'Update Reservation' button | Yes |
| When reserving or updating a seat/s by clicking the 'Reserve' button or 'Update Reservation' button, a loading animation shows up and all interactive elements are disabled until the saving process is complete | Yes |
| When all reserved seats are removed and the 'Update Reservation' button is clicked, an offcanvas lightbox shows up with the 'Confirm' button to delete the reservation for the event | Yes |
| Only a maximum of 2 seats can be booked per user per event | Yes |
| A feedback message stating "You've reached the 2 seats maximum per user" is displayed when the user attempts to select more thatn 2 seats per event | Yes |
| The seat map can be panned and zoomed | Yes |
| The seat map is initially blocked with pan and zoom functionality disabled when a user with reserved seats to the event visits the page | Yes |
| The initial seat map blocker can be removed by clicking the 'Edit Reservation' button | Yes |

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## PYTHON AUTOMATED TESTING (Unittest)
There are 18 automated tests created on this project and all of which ran successfully as shown in the image below. The tests checked the following:    
* the correct rendering of the templates/pages,
* the successful 'liking' and posting of comments,
* the creation of new events,
* the signing up, logging in and logging out of users,
* the site's response to very common passwords and invalid emails during signup, and 
* the site's response to incorrect login passwords  

These tests can be seen in the `tests.py` file in each of the apps.

![Unittest Result](docs/test_cases/automated-testing-result.png)

* **How to Run the Tests**
    * Use the **sqlite3 database**. This can be done by either:     
        * Temporarily commenting out the production database URL, and leaving the following code as the default:
            > DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
        * Or, temporarily comment out the DATABASE_URL in the `env` file.
    * Then, use the command "`python3 manage.py test`" to run the tests.

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## VALIDATORS

### **CI Python Linter**
All Python codes on this project were tested using the [CI Python Linter](https://pep8ci.herokuapp.com/), and all results were **"ALL CLEAR, NO ERRORS FOUND"**. See below for the result screenshots for each Python file.   

* [**goodwill_events/SETTINGS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/goodwill_events/settings.py)    
![Settings.py Linter Result](docs/testing_screenshots/python_linter/settings.png)   
* [**goodwill_events/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/goodwill_events/urls.py)    
![Urls.py Linter Result](docs/testing_screenshots/python_linter/main-urls.png)  
* [**events/ADMIN.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/admin.py)    
![events/admin.py Linter Result](docs/testing_screenshots/python_linter/events-admin.png)         
* [**events/FORMS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/forms.py)    
![events/forms.py Linter Result](docs/testing_screenshots/python_linter/events-forms.png)   
* [**events/TESTS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/tests.py)    
![events/tests.py Linter Result](docs/testing_screenshots/python_linter/events-tests.png)   
* [**events/MODELS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/models.py)  
![events/models.py Linter Result](docs/testing_screenshots/python_linter/events-models.png) 
* [**events/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/urls.py)  
![events/urls.py Linter Result](docs/testing_screenshots/python_linter/events-urls.png) 
* [**events/VIEWS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/views.py)    
![events/views.py Linter Result](docs/testing_screenshots/python_linter/events-views.png)
* [**member/FORMS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/member/forms.py)    
![member/forms.py Linter Result](docs/testing_screenshots/python_linter/member-forms.png)   
* [**member/TESTS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/member/tests.py)    
![member/tests.py Linter Result](docs/testing_screenshots/python_linter/member-tests.png)
* [**member/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/member/urls.py)  
![member/urls.py Linter Result](docs/testing_screenshots/python_linter/member-urls.png)     
* [**member/VIEWS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/member/views.py)    
![member/views.py Linter Result](docs/testing_screenshots/python_linter/member-views.png)   
* [**seating/ADMIN.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/admin.py)  
![seating/admin.py Linter Result](docs/testing_screenshots/python_linter/seating-admin.png) 
* [**seating/FORMS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/forms.py)  
![seating/forms.py Linter Result](docs/testing_screenshots/python_linter/seating-forms.png) 
* [**seating/MODELS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/models.py)    
![seating/models.py Linter Result](docs/testing_screenshots/python_linter/seating-models.png)   
* [**seating/TESTS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/tests.py)  
![seating/tests.py Linter Result](docs/testing_screenshots/python_linter/seating-tests.png)     
* [**seating/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/urls.py)    
![seating/urls.py Linter Result](docs/testing_screenshots/python_linter/seating-urls.png)   
* [**seating/VIEWS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/views.py)  
![seating/view.py Linter Result](docs/testing_screenshots/python_linter/seating-views.png)  

[<ins>Back to Table of Contents</ins>](#table-of-contents)

### **JSHint**  
The Javascript codes on this project were tested and validated by [JSHINT](https://jshint.com/), which is a tool analysis JS code for errors and potential problems. All the results from the JSHINT showed **NO ERROR** for this project.  
See individual result screenshot below. 

* [**script.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/script.js)  
![JSHINT result for script.js](docs/testing_screenshots/jshint/script-jshint-result.png)    
* [**seating_script.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/seating_script.js)  
![JSHINT result for seating_script.js](docs/testing_screenshots/jshint/seating_script-jshint-result.png)    
* [**seatmap_panzoom.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/seatmap_panzoom.js)    
![JSHINT result for seatmap_panzoom.js](docs/testing_screenshots/jshint/seatmap-panzoom-jshint-result.png)  

[<ins>Back to Table of Contents</ins>](#table-of-contents)

### **W3C MarkUp Validator**    
The HTML files on this project were tested and validated by [W3C Markup Validation Service](https://validator.w3.org/). **NO ERRORS OR WARNINGS** were shown on the results.

* **Home Page**  -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/home-html-validated.png)
* **Events (Upcoming Events) Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/events-page-html-validated.png)
* **Seat Map (Generic) Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/generic-seatmap-html-validated.png)   
* **Specific Event Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/specific-event-page-html-validated.png)  
* **Seat Reservation Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/seat-reservation-html-validated.png)    
* **Member Account Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/member-account-html-validated.png)
* **Sign In Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signin-html-validated.png)
* **Sign Up Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signup-validated.png) 
* **Sign Out Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signout-html-validated.png)    
* **Password Reset Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/password-reset-validated.png)  
* **Password Reset - Emailed Link** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/password-reset-emailed-html-validated.png)
* **Change Password Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-html-validated.png)     
* **Change Password via Link** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-via-link-html-validated.png) 
* **Change Password Done** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-done-html-validated.png) 

### **W3C CSS Validator**  
The CSS codes on this project were validated by the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). All results showed **"NO ERROR FOUND"**. See below for each result.
* [**style.css**](https://github.com/marked-gil/goodwill-events/blob/main/static/css/style.css)
![style.css validator result screenshot](docs/testing_screenshots/css_validator/style-css-validated.png)
* [**seating_style.css**](https://github.com/marked-gil/goodwill-events/blob/main/static/css/seating_style.css)
![seating_style.css validator result screenshot](docs/testing_screenshots/css_validator/seating_style_css_validated.png)

[<ins>Back to Table of Contents</ins>](#table-of-contents)

## ACCESSIBILITY

### **Safari Accessibility Audit Results**

Safari's Accessibility Audit inspects the site's pages for accessibility issues, and each page on this site is 100% accessible based on the results shown below.

* **Home Page**     
![Safari Audit Result for Home Page](docs/testing_screenshots/safari-audit/safari-audit-home.png)  
* **Events (Upcoming Events) Page**     
![Safari Audit Result for Events Page](docs/testing_screenshots/safari-audit/safari-audit-events.png)    
* **Seat Map (Generic) Page**    
![Safari Audit Result for Seat Map Page](docs/testing_screenshots/safari-audit/safari-audit-seatmap.png)  
* **Specific Event Page**   
![Safari Audit Result for Specific Event Page](docs/testing_screenshots/safari-audit/safari-audit-specific-event.png)    
* **Seat Reservation Page**    
![Safari Audit Result for Seat Reservation Page](docs/testing_screenshots/safari-audit/safari-audit-reservation.png)  
* **Member Account Page**   
![Safari Audit Result for Member Account Page](docs/testing_screenshots/safari-audit/safari-audit-member.png)    
* **Sign In Page**  
![Safari Audit Result for Sign In Page](docs/testing_screenshots/safari-audit/safari-audit-signin.png)
* **Sign Up Page**  
![Safari Audit Result for Sign Up Page](docs/testing_screenshots/safari-audit/safari-audit-signup.png)
* **Sign Out Page**     
![Safari Audit Result for Sign Out Page](docs/testing_screenshots/safari-audit/safari-audit-signout.png)  
* **Password Reset Page**   
![Safari Audit Result for Password Reset Page](docs/testing_screenshots/safari-audit/safari-audit-password-reset.png)    
* **Change Password Page**      
![Safari Audit Result for Change Password Page](docs/testing_screenshots/safari-audit/safari-audit-change-password.png)   

[Back to Table of Contents](#table-of-contents)


### **Color Contrast Accessibility Validator Results**      
Using the [a11Y's Color Contrast Accessibility Validator](https://color.a11y.com/), this site is validated to be compliant with website accessibilities regulations on colour contrast.
However, the pages that require logging in cannot be analysed by the validator, but their color contrast was validated by other tools such as the 'Safari Audit', 'WAVE', and 'Lighthouse'.

* **Home Page**     
![Color Contrast Validator Result for Home Page](docs/testing_screenshots/color_contrast_validator/color-contrast-home.png) 
* **Events (Upcoming Events) Page**     
![Color Contrast Validator Result for Events Page](docs/testing_screenshots/color_contrast_validator/color-contrast-events.png)      
* **Seat Map (Generic) Page**   
![Color Contrast Validator Result for Seat Map Page](docs/testing_screenshots/color_contrast_validator/color-contrast-seatmap.png)  
* **Specific Event Page**   
![Color Contrast Validator Result for Specific Event Page](docs/testing_screenshots/color_contrast_validator/color-contrast-specific-event.png)      
* **Sign In Page**  
![Color Contrast Validator Result for Sign In Page](docs/testing_screenshots/color_contrast_validator/color-contrast-signin.png)    
* **Sign Up Page**  
![Color Contrast Validator Result for Sign Up Page](docs/testing_screenshots/color_contrast_validator/color-contrast-signup.png)    
* **Password Reset Page**   
![Color Contrast Validator Result for Password Reset Page](docs/testing_screenshots/color_contrast_validator/color-contrast-password-reset.png) 

[<ins>Back to Table of Contents</ins>](#table-of-contents)


### **WAVE - Web Accessibility Evaluation Tool**
This project utilised the [WAVE - Web Accessibility Evaluation Tool](https://wave.webaim.org/) browser extension to ensure its accessibility.       
![WAVE](docs/testing_screenshots/wave/wave-screenshot.png)

### **LIGHTHOUSE TESTING**
* **Home Page**     
![Lighthouse Result for Home Page](docs/testing_screenshots/lighthouse/lighthouse-home.png)     
* **Events (Upcoming Events) Page**     
![Lighthouse Result for Events Page](docs/testing_screenshots/lighthouse/lighthouse-events.png)     
* **Seat Map (Generic) Page**    
![Lighthouse Result for Seat Map Page](docs/testing_screenshots/lighthouse/lighthouse-seatmap.png)  
* **Specific Event Page**   
![Lighthouse Result for Specific Event Page](docs/testing_screenshots/lighthouse/lighthouse-specific-event.png)  
* **Seat Reservation Page**    
![Lighthouse Result for Seat Reservation Page](docs/testing_screenshots/lighthouse/lighthouse-reservation.png)      
* **Member Account Page**   
![Lighthouse Result for Member Account Page](docs/testing_screenshots/lighthouse/lighthouse-member.png)     
* **Sign In Page**  
![Lighthouse Result for Sign In Page](docs/testing_screenshots/lighthouse/lighthouse-signin.png)         
* **Sign Up Page**  
![Lighthouse Result for Sign Up Page](docs/testing_screenshots/lighthouse/lighthouse-signup.png)         
* **Sign Out Page**     
![Lighthouse Result for Sign Out Page](docs/testing_screenshots/lighthouse/lighthouse-signout.png)  
* **Password Reset Page**   
![Lighthouse Result for Password Reset Page](docs/testing_screenshots/lighthouse/lighthouse-password-reset.png)     
* **Change Password Page**      
![Lighthouse Result for Change Password Page](docs/testing_screenshots/lighthouse/lighthouse-change-password.png)   

[<ins>Back to Table of Contents</ins>](#table-of-contents)


## RESPONSIVENESS

This website is designed to be fully responsive from a minimum screen size of 280px.

### **Mobile-Friendly Test**
The tool [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) validated the ease and friendliness of the site when used on small screens such as mobile devices.  
**Note:** The Mobile-Friendly Test tool could not detect the ability of the seat map to pan and zoom; thus, manual testing was used for the Seat Reservation page.

* **Home Page**     
![Mobile-Friendly Test Result for Home Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-home.png)    
* **Events (Upcoming Events) Page**   
![Mobile-Friendly Test Result for Events Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-events.png)    
* **Seat Map (Generic) Page**    
![Mobile-Friendly Test Result for Seat Map Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-seatmap.png)     
* **Specific Event Page**   
![Mobile-Friendly Test Result for Specific Event Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-specific-event.png)    
* **Member Account Page**   
![Mobile-Friendly Test Result for Member Account Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-member.png)    
* **Sign In Page**  
![Mobile-Friendly Test Result for Sign In Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-signin.png)   
* **Sign Up Page**  
![Mobile-Friendly Test Result for Sign Up Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-signup.png)   
* **Sign Out Page**     
![Mobile-Friendly Test Result for Sign Out Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-signout.png)     
* **Password Reset Page**   
![Mobile-Friendly Test Result for Password Reset Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-password-reset.png)    
* **Change Password Page**      
![Mobile-Friendly Test Result for Change Password Page](docs/testing_screenshots/mobile_friendly_test/mobile-friendly-change-password.png)      

[<ins>Back to Table of Contents</ins>](#table-of-contents)


### **Manual Testing for Responsiveness**

The web developer tools of the 4 main websites (Chrome, Firefox, Edge, and Safari) were used to manually test each page of this site for their responsiveness. Below are sample screenshots:

* **Chrome**    
![iphone 5 on Chrome developer tool](docs/testing_screenshots/manual_responsiveness_test/chrome-iphone5.png)    
* **Firefox**   
![Pixel 2 Android on Firefox developer tool](docs/testing_screenshots/manual_responsiveness_test/firefox-pixel2-android.png)    
* **Microsoft Edge**    
![Galaxy S9+ on Microsoft Edge developer tool](docs/testing_screenshots/manual_responsiveness_test/edge-galaxy-s8.png)  
* **Safari**    
![iPhone 8 Plus on Safari developer tool](docs/testing_screenshots/manual_responsiveness_test/safari-iphone8plus.png)     


[<ins>Back to Table of Contents</ins>](#table-of-contents)

### [>> **BACK TO README.MD**](https://github.com/marked-gil/goodwill-events#readme)