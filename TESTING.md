# TESTING

## TABLE OF CONTENTS    
* [**Test Cases**](#test-cases-user-story-testing)
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


## TEST CASES (User Story Testing)

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
    ![](docs/test_cases/test-cases-13.png)     
    ![](docs/test_cases/test-cases-14.png)  
    Reservation Update & Cancellation
    ![](docs/test_cases/test-cases-15.png)
    ![](docs/test_cases/test-cases-16.png)  
    Seat Reservation Feature Restricted to Signed-In Users
    ![](docs/test_cases/test-cases-17.png)  

* **RECYCLING EXPIRED EVENTS**
    ![](docs/test_cases/test-cases-18.png)


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
* [**events/MODELS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/models.py)  
![events/models.py Linter Result](docs/testing_screenshots/python_linter/events-models.png) 
* [**events/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/urls.py)  
![events/urls.py Linter Result](docs/testing_screenshots/python_linter/events-urls.png) 
* [**events/VIEWS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/events/views.py)    
![events/views.py Linter Result](docs/testing_screenshots/python_linter/events-views.png)
* [**member/FORMS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/member/forms.py)    
![member/forms.py Linter Result](docs/testing_screenshots/python_linter/member-forms.png)   
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
* [**seating/URLS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/urls.py)    
![seating/urls.py Linter Result](docs/testing_screenshots/python_linter/seating-urls.png)   
* [**seating/VIEWS.PY**](https://github.com/marked-gil/goodwill-events/blob/main/seating/views.py)  
![seating/view.py Linter Result](docs/testing_screenshots/python_linter/seating-views.png)  

### **JSHint**  
The Javascript codes on this project were tested and validated by [JSHINT](https://jshint.com/), which is a tool analysis JS code for errors and potential problems. All the results from the JSHINT showed **NO ERROR** for this project.  
See individual result screenshot below. 

* [**script.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/script.js)  
![JSHINT result for script.js](docs/testing_screenshots/jshint/script-jshint-result.png)    
* [**seating_script.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/seating_script.js)  
![JSHINT result for seating_script.js](docs/testing_screenshots/jshint/seating_script-jshint-result.png)    
* [**seatmap_panzoom.js**](https://github.com/marked-gil/goodwill-events/blob/main/static/js/seatmap_panzoom.js)    
![JSHINT result for seatmap_panzoom.js](docs/testing_screenshots/jshint/seatmap_panzoom-jshint-result.png)  

### **W3C MarkUp Validator**    
The HTML files on this project were tested and validated by [W3C Markup Validation Service](https://validator.w3.org/). **NO ERRORS OR WARNINGS** were shown on the results.    

* **Home Page**  -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/home-html-validated.png)
* **Events (Upcoming Events) Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/events-page-html-validated.png)
* **Seat Map (Generic) Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/generic-seatmap-html-validated.png)   
* **Specific Event Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/specific-event-page-html-validated.png)  
* **Seat Reservation Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/seat-reservation-html-validated.png)    
* **Member Account Page** -- [Click for Result]()
* **Sign In Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signin-html-validated.png)
* **Sign Up Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signup-validated.png) 
* **Sign Out Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/signout-html-validated.png)    
* **Password Reset Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/password-reset-validated.png)  
* **Password Reset - Emailed Link** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/password-reset-emailed-html-validated.png)
* **Change Password Page** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-html-validated.png)     
* **Change Password via Link** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-via-link-html-validated.png) 
* **Change Password Done** -- [Click for Result](https://github.com/marked-gil/goodwill-events/blob/main/docs/testing_screenshots/html_validator/change-password-done-html-validated.png) 

### **W3C CSS Validator **  
The CSS codes on this project were validated by the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). All results showed **"NO ERROR FOUND"**. See below for each result.
* [**style.css**](https://github.com/marked-gil/goodwill-events/blob/main/static/css/style.css)
![style.css validator result screenshot](docs/testing_screenshots/css_validator/style-css-validated.png)
* [**seating_style.css**](https://github.com/marked-gil/goodwill-events/blob/main/static/css/seating_style.css)
![seating_style.css validator result screenshot](docs/testing_screenshots/css_validator/seating_style_css_validated.png)

## ACCESSIBILITY

### **Safari Accessibility Audit Results**
### **Color Contrast Accessibility Validator Results**
### **WAVE - Web Accessibility Evaluation Tool**

## LIGHTHOUSE TESTING
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

## RESPONSIVENESS