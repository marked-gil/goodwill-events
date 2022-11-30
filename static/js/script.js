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
    const first_name = document.getElementById('id_first_name')
    const last_name = document.getElementById('id_last_name')
    const email = document.getElementById('id_email')
    const fname_edit_btn = document.getElementById('fname_edit')
    const lname_edit_btn = document.getElementById('lname_edit')
    const email_edit_btn = document.getElementById('email_edit')
    const updateBtn = document.getElementById('update-account-btn')

    // Initially set all input fields as readonly in Member's Account page
    member_info_fields = document.querySelectorAll('#member_account_form input')
    for (field of member_info_fields) {
        field.setAttribute('readonly', true)
        field.setAttribute('class', 'disabled-field')
    }

    // Event Listeners for edit buttons
    fname_edit_btn.addEventListener('click', (e) => {
        first_name.toggleAttribute('readonly')
        first_name.classList.toggle('disabled-field')
        updateBtn.classList.remove('disabled')
        toggleButtonText(fname_edit_btn)
    })
    lname_edit_btn.addEventListener('click', (e) => {
        last_name.toggleAttribute('readonly')
        last_name.classList.toggle('disabled-field')
        updateBtn.classList.remove('disabled')
        toggleButtonText(lname_edit_btn)
    })
    email_edit_btn.addEventListener('click', (e) => {
        email.toggleAttribute('readonly')
        email.classList.toggle('disabled-field')
        updateBtn.classList.remove('disabled')
        toggleButtonText(email_edit_btn)
    })

    /**
     * Toggles text content of the Edit button
     * @param {*} btn - The targeted button
     */
    function toggleButtonText(btn) {
        btn.textContent == 'Edit' ? btn.textContent = 'X' : btn.textContent = 'Edit'
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