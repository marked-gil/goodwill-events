// --> NAV BAR [Start] <--
const homePage = document.getElementById('homepage-banner-container');
const eventsPage = document.getElementById('events-outer-container');
const viewSeatMapPage = document.getElementById('view-seatmap-section');
const signInPage = document.getElementById('sign-in-section');
const signUpPage = document.getElementById('sign-up-section');
const signOutPage = document.getElementById('sign-out-section');
const accountPage = document.getElementById('member-account-outer-container');

// Highlights & disables the nav link when corresponding page is opened
showActiveNavLink(homePage, 'home-link');
showActiveNavLink(eventsPage, 'events-link');
showActiveNavLink(viewSeatMapPage,'view-seatmap-link');
showActiveNavLink(signInPage, 'sign-in-link');
showActiveNavLink(signUpPage, 'sign-up-link');
showActiveNavLink(signOutPage, 'sign-out-link');
showActiveNavLink(accountPage, 'user-acount-link');
// --> NAV BAR [End] <--


// --> EVENT DETAILS Page [Start] <--
if (document.getElementById('comment-form')) {
    const MAX_COMMENT_CHARS = 250;
    const commentTextarea = document.getElementById('comment-textarea');
    const charCounterField = document.getElementById('char-counter');
    const postCommentButton = document.querySelector('#comment-form button');
    
    // Characters Counter for COMMENTS
    commentTextarea.addEventListener("keyup", (e) => {
        const commentContent = commentTextarea.value;
        const commentLength = commentTextarea.value.length;
        const charRemaining = MAX_COMMENT_CHARS - commentLength;

        // Grammar Consideration
        if (commentLength <= MAX_COMMENT_CHARS) {
            let chars = charRemaining > 1 ? "characters" : "character";
            charCounterField.textContent = `${charRemaining} ${chars} remaining`;
        }

        // Disables POST button when textarea is empty
        if (charRemaining != MAX_COMMENT_CHARS && !containsOnlySpaces(commentContent)) {
            postCommentButton.classList.remove('disabled');
        } else {
             postCommentButton.classList.add('disabled');
        }
    });

    // Post User's Comment using AJAX
    /** 
     * Code idea was taken from Stackoverflow & Plus Geek's Youtube Channel
     * (See Credits Section in README.md)
     */
    $("#comment-form").submit(function (e) {
        e.preventDefault();
        const baseURL = window.location.origin;
        const slug = window.location.pathname;
        $.ajax({
            type: "POST",
            url: baseURL + "/comment" + slug,
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                text_comment: $('#comment-textarea').val(),
            },
            success: function (response) {
                if (response.message === "success") {
                    location.reload();
                } else {
                    $(this).after(`<p class="text-center">**${response.message}**</p>`);
                }
            },
            error: function () {
                $(this).after(`<p class="text-center">**Something went wrong.**</p>`);
            },
        });
    });

    // Prevents multiple clicking of the 'Post' button for comment
    const commentPostBtn = document.querySelector("#comment-form button");
    disableBtn(commentPostBtn);

    // Delete User's Comment using AJAX
    /** 
     * Code idea was taken from Stackoverflow & Plus Geek's Youtube Channel
     * (See Credits Section in README.md)
     */
    $(".delete-comment-form").submit(function (e) {
        e.preventDefault();
        const form = $(this);
        $.ajax({
            type: "POST",
            url: form.data("url"),
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                if (response.message === 'success') {
                    location.reload();
                }
            },
        });
    });

    // Prevents multiple clicking of the 'Delete' button for comment
    const commentDeleteBtns = document.querySelectorAll(".delete-comment-form button");
    if (commentDeleteBtns) {
        commentDeleteBtns.forEach(function(btn) {
            disableBtn(btn);
        });
    }
}
// --> EVENT DETAILS Page [End] <--


// --> EVENTS Page (Pagination Nav) [Start] <--
if (document.getElementById("pagination-nav")) {
    const pagination = document.getElementById('events-pagination');
    const pageNumber = pagination.getAttribute('data-page-number');
    const pageLinks = document.querySelectorAll('.page-link');

    // Highlights the page nunber in the pagination nav
    for (let page of pageLinks) {
        if (page.textContent == pageNumber) {
            page.classList.add('active', 'disabled-link');
            page.setAttribute('tabindex', '-1');
        }
    }
}
// --> EVENTS Page [End] <--


// --> MEMBER ACCOUNT Page [Start] <--
if (document.getElementById('member-account-outer-container')) {
    const firstName = document.getElementById('id_first_name');
    const lastName = document.getElementById('id_last_name');
    const email = document.getElementById('id_email');
    const fnameEditBtn = document.getElementById('fname_edit');
    const lnameEditBtn = document.getElementById('lname_edit');
    const emailEditBtn = document.getElementById('email_edit');
    
    const originalFirstName = firstName.value;
    const originalLastName = lastName.value;
    const originalEmail =email.value;

    // Initially set all input fields as readonly in Member's Account page
    const member_info_fields = document.querySelectorAll('#member_account_form input');
    for (let field of member_info_fields) {
        field.setAttribute('readonly', true);
        field.setAttribute('class', 'disabled-field');
        field.setAttribute('tabindex', '-1');
    }

    // Event Listeners for EDIT buttons
    fnameEditBtn.addEventListener('click', (e) => {
        firstName.toggleAttribute('readonly');
        firstName.classList.toggle('disabled-field');
        toggleButtonText(fnameEditBtn);
        firstName.addEventListener('keyup', function() {
            fieldValueChanged(this, originalFirstName);
        });
    });
    lnameEditBtn.addEventListener('click', (e) => {
        lastName.toggleAttribute('readonly');
        lastName.classList.toggle('disabled-field');
        toggleButtonText(lnameEditBtn);
        lastName.addEventListener('keyup', function() {
            fieldValueChanged(this, originalLastName);
        });
    });
    emailEditBtn.addEventListener('click', (e) => {
        email.toggleAttribute('readonly');
        email.classList.toggle('disabled-field');
        toggleButtonText(emailEditBtn);
        email.addEventListener('keyup', function() {
            fieldValueChanged(this, originalEmail);
        });
    });
}
// --> MEMBER ACCOUNT Page [End] <--


// --> FUNCTIONS <--
/**
 * Highlights and disables the corresponding nav link of the current page
 * @param {Element} pageDOM - element specific to a page
 * @param {String} navID - ID of the nav link
 */
function showActiveNavLink(pageDOM, navID) {
    if (pageDOM) {
        const navLink = document.getElementById(navID);
        navLink.classList.add('active', 'disabled-link');
        navLink.setAttribute('aria-current', 'page');
        navLink.setAttribute('tabindex', '-1');
    }
}

/**
 * Toggles text content of the Edit button
 * @param {Element} btn - The targeted button
 */
function toggleButtonText(btn) {
    return btn.textContent == 'Edit' ? btn.textContent = 'X' : btn.textContent = 'Edit';
}

/**
 * Enables the 'Update' button when field input is changed,
 * and disables it when no changes are made
 * @param {Element} field - input field
 * @param {String} originalText 
 */
function fieldValueChanged(field, originalText) {
    const updateBtn = document.getElementById('update-account-btn');
    if (field.value.trim() != originalText) {
        updateBtn.classList.remove('disabled');
        updateBtn.removeAttribute("tabindex");
        updateBtn.setAttribute('type', 'submit');
    } else {
        updateBtn.classList.add('disabled');
        updateBtn.setAttribute("tabindex", "-1");
        updateBtn.setAttribute('type', 'button');
    }
}

/**
 * Disables a button
 * @param {Element} button - The target button
 */
function disableBtn(button) {
    button.addEventListener('click', function() {
        this.classList.add("disabled");
    });
}

/**
 * Checks if a string only contains spaces
 * Code taken from bobbyhadz blog (See Credit Section on README.md)
 * @param {String} str - a string of characters
 * @returns a Boolean
 */
function containsOnlySpaces(str) {
    return /^\s*$/.test(str);
}