// --> NAV BAR [Start] <--
const homePage = document.getElementById('homepage-banner-container')
const eventsPage = document.getElementById('events-outer-container')
const signInPage = document.getElementById('sign-in-section')
const signUpPage = document.getElementById('sign-up-section')
const signOutPage = document.getElementById('sign-out-section')
const AccountPage = document.getElementById('member-account-outer-container')

// Highlights the nav link when corresponding page is opened
showActiveNavLink(homePage, 'home-link')
showActiveNavLink(eventsPage, 'events-link')
showActiveNavLink(signInPage, 'sign-in-link')
showActiveNavLink(signUpPage, 'sign-up-link')
showActiveNavLink(signOutPage, 'sign-out-link')
showActiveNavLink(AccountPage, 'user-acount-link')
// --> NAV BAR [End] <--


// --> EVENT DETAILS Page [Start] <--
if (document.getElementById('comment-form')) {
    MAX_COMMENT_CHARS = 250
    const comment_textarea = document.getElementById('comment-textarea')
    const char_counter_field = document.getElementById('char-counter')
    
    // Characters Counter for COMMENTS
    comment_textarea.addEventListener("keyup", (e) => {
        const comment_length = comment_textarea.value.length
        const chars_remaining = MAX_COMMENT_CHARS - comment_length

        if (comment_length <= MAX_COMMENT_CHARS) {
            let chars = chars_remaining > 1 ? "characters" : "character"
            char_counter_field.textContent = `${chars_remaining} ${chars} remaining`
        }
    })
}
// --> EVENT DETAILS Page [End] <--


// --> EVENTS Page [Start] <--
if (document.getElementById("events-outer-container")) {
    const pagination = document.getElementById('events-pagination')
    const pageNumber = pagination.getAttribute('data-page-number')
    const pageLinks = document.querySelectorAll('.page-link')

    // Highlights the page nunber in the pagination nav
    for (page of pageLinks) {
        if (page.textContent == pageNumber) {
            page.classList.add('active')
        }
    }
}
// --> EVENTS Page [End] <--


// --> MEMBER ACCOUNT Page [Start] <--
if (document.getElementById('member-account-outer-container')) {
    const firstName = document.getElementById('id_first_name')
    const lastName = document.getElementById('id_last_name')
    const email = document.getElementById('id_email')
    const fnameEditBtn = document.getElementById('fname_edit')
    const lnameEditBtn = document.getElementById('lname_edit')
    const emailEditBtn = document.getElementById('email_edit')
    const updateBtn = document.getElementById('update-account-btn')
    
    const originalFirstName = firstName.value
    const originalLastName = lastName.value
    const originalEmail =email.value

    // Initially set all input fields as readonly in Member's Account page
    member_info_fields = document.querySelectorAll('#member_account_form input')
    for (field of member_info_fields) {
        field.setAttribute('readonly', true)
        field.setAttribute('class', 'disabled-field')
    }

    // Event Listeners for edit buttons
    fnameEditBtn.addEventListener('click', (e) => {
        firstName.toggleAttribute('readonly')
        firstName.classList.toggle('disabled-field')
        toggleButtonText(fnameEditBtn)
        firstName.addEventListener('keyup', function() {
            fieldValueChanged(this, originalFirstName)
        })
    })
    lnameEditBtn.addEventListener('click', (e) => {
        lastName.toggleAttribute('readonly')
        lastName.classList.toggle('disabled-field')
        toggleButtonText(lnameEditBtn)
        lastName.addEventListener('keyup', function() {
            fieldValueChanged(this, originalLastName)
        })
    })
    emailEditBtn.addEventListener('click', (e) => {
        email.toggleAttribute('readonly')
        email.classList.toggle('disabled-field')
        toggleButtonText(emailEditBtn)
        email.addEventListener('keyup', function() {
            fieldValueChanged(this, originalEmail)
        })
    })

    /**
     * Toggles text content of the Edit button
     * @param {*} btn - The targeted button
     */
    function toggleButtonText(btn) {
        btn.textContent == 'Edit' ? btn.textContent = 'X' : btn.textContent = 'Edit'
    }

    /**
     * Enables the 'Update' button when field input is changed,
     * and disables it when no changes are made
     * @param {*} field 
     * @param {*} originalText 
     */
    function fieldValueChanged(field, originalText) {
        if (field.value != originalText) {
            updateBtn.classList.remove('disabled')
        } else {
            updateBtn.classList.add('disabled')
        }
    }
}
// --> MEMBER ACCOUNT Page [End] <--


// --> FUNCTION <--
/**
 * Highlights the nav link when page opened
 * @param {*} pageDOM - element specific to a page
 * @param {*} navID - ID of the nav link
 */
function showActiveNavLink(pageDOM, navID) {
    if (pageDOM) {
        const navLink = document.getElementById(navID)
        navLink.classList.add('active', 'disabled-link')
        navLink.setAttribute('aria-current', 'page')
    }
}