/**
 * The following templates utilize this custom JS file:
 *   'reserve-seats.html' template, 
 *   'view_seatmap.html' template, and
 *   'seatmap.html'
 */

// --> SEAT RESERVATION Page <--
if (document.getElementById('seat-reservation-section')) {
    const TOTAL_EVENT_SEATS = 142;
    const string_reserved_seats = document.getElementById('data-seats').textContent;
    let list_reserved_seats = string_reserved_seats.replace(/[^a-zA-Z0-9_,]/g, '').split(",");
    const userBookedSeats = getSelectedSeats();

    /** 
     * Blocks all reserved seats, and makes all available seats clickable
     */
    window.onpageshow = function () {
        const svg_seats_list = document.querySelectorAll('[data-seat-location]');
        for (let svg_seat of svg_seats_list) {
            const seat_loc = svg_seat.getAttribute("data-seat-location");
            blockReservedSeats(svg_seat, seat_loc, list_reserved_seats);
            makeAllFreeSeatsClickable(svg_seat, seat_loc, userBookedSeats);
        }

        // Changes seat map's instruction message when FULLY BOOKED
        if (list_reserved_seats.length === TOTAL_EVENT_SEATS) {
            const select_box_text = document.getElementById("select-box-instruction");
            select_box_text.innerHTML = "<i class='fa-solid fa-hand'></i> This event is FULLY BOOKED.";
            select_box_text.style.color = "red";
        }
    };
    
    // EventListener to Remove Reserved Seat via Cancel Button
    if (document.getElementsByClassName("btn-cancel-seat")) {
        const cancel_seat_buttons = document.querySelectorAll(".btn-cancel-seat");
        for (let btn of cancel_seat_buttons) {
            cancelSeat(btn, userBookedSeats);
        }
    }

    // EventListener to Create Reservation
    if (document.getElementById("submit-reservation")) {
        const reserve_button = document.getElementById("submit-reservation");
        reserve_button.addEventListener('click', submitSeatReservation);
    }

    // EventListener to Update Reservation
    if (document.getElementById("update-reservation")) {
        const update_button = document.getElementById("update-reservation");
        update_button.addEventListener('click', submitSeatReservation);
    }
    
    // EventListener to Allow Editing of Reserved Seats
    if (document.getElementById("edit-reservation")) {
        const seatMapBlocker = document.getElementById("seatmap-blocker");
        const editReservationBtn = document.getElementById("edit-reservation");
        seatMapBlocker.classList.remove("d-none");
        editReservationBtn.addEventListener('click', allowEditingReservation);
    }

    // EventListener to Delete Reservation
    if (document.getElementById("confirm-delete")) {
        const deleteReservationForm = document.getElementById("delete-reservation-form");
        const confirmDeleteBtn = document.getElementById("delete-reservation-button");
        confirmDeleteBtn.addEventListener('click', function() {
            displayLoadingAnimation();
            deleteReservationForm.submit();
            disableAllInteractiveElements();
        });
    }
}

// --> FUNCTIONS [Start] <--
/**
 * Blocks seats that are already reserved.
 * @param {Element} svg_seat 
 * @param {String} seat_loc
 * @param {Array} list_reserved_seats
 */
function blockReservedSeats(svg_seat, seat_loc, list_reserved_seats) {
    if (list_reserved_seats.includes(seat_loc)) {
        svg_seat.classList.add("booked");
    }
}

/**
 * Transforms SVG boxes (seats) into clickable elements;
 * Enables or disables the button to reserve or update the seats;
 * Displays feedback if user tries to select more than 2 seats
 * @param {Element} svg_seat
 * @param {String} seat_loc
 * @param {Array} currentSeatsBooked
 */
function makeAllFreeSeatsClickable(svg_seat, seat_loc, currentSeatsBooked) {
    const ALLOWED_SEATS_PER_USER = 2;
    svg_seat.style.cursor = 'pointer';
    svg_seat.addEventListener('click', function () {
        if (SelectedSeatsByUser().length < ALLOWED_SEATS_PER_USER) {
            toggleSeat(this, seat_loc);
            toggleReserveUpdateButton(currentSeatsBooked);
        } else {
            if (this.classList.contains("user-selected")) {
                toggleSeat(this, seat_loc);
                toggleReserveUpdateButton(currentSeatsBooked);
            } else {
                // Displays feedback that 2 seats already booked by user
                const message = "You've reached the 2 seats maximum per user.";
                showFeedBackMsg(message);
            }
        }
    });
}

/**
 * Toggles between displaying the selected seat location and removing it
 * @param {Element} seat - svg seat
 * @param {String} seat_loc - seat location
 */
function toggleSeat(seat, seat_loc) {
    seat.classList.toggle("user-selected");
    if (seat.classList.contains("user-selected")) {
        showSelectedSeat(seat_loc);
    } else {
        removeDeselectedSeat(seat_loc);
    }
}

/**
 * Displays the seat location name
 * @param {String} seat_loc - seat location
 */
function showSelectedSeat(seat_loc) {
    const li_elem = document.createElement("li");
    li_elem.innerText = seat_loc;
    document.getElementById("seats-selected-list").appendChild(li_elem);
    li_elem.setAttribute('id', seat_loc);
    li_elem.setAttribute('class', 'd-flex align-items-center me-4');
}

/**
 * Removes the displayed seat location name
 * @param {*} seat_loc - seat location
 */
function removeDeselectedSeat(seat_loc) {
    if (typeof seat_loc == "string") {
        const li_elem = document.getElementById(seat_loc);
        li_elem.remove();
    } else if (typeof seat_loc == "object") {
        seat_loc.remove();
    }
}

/**
 * Returns the selected seats by the user
 */
function SelectedSeatsByUser() {
    const user_reserved_seats = document.querySelectorAll("#seats-selected-list > li");
    return user_reserved_seats;
}

/**
 * Cancels reserved seat by unblocking the SVG seat box
 * and removing the display of seat's location.
 * Also enables or disables the button to reserve or update the seats
 * @param {Element} btn - button
 * @param {Array} currentSeatsBooked
 */
function cancelSeat(btn, currentSeatsBooked) {
    const svg_seats_list = document.querySelectorAll('[data-seat-location]');
    const string_reserved_seats = document.getElementById('data-seats').textContent;
    let list_reserved_seats = string_reserved_seats.replace(/[^a-zA-Z0-9_,]/g, '').split(",");
    btn.addEventListener('click', function () {
        let seat = this.parentElement;
        for (let svg_seat of svg_seats_list) {
            let seat_location = svg_seat.getAttribute("data-seat-location");
            if (seat_location == seat.getAttribute("id")) {
                const seat_index = list_reserved_seats.indexOf(seat_location);
                list_reserved_seats.splice(seat_index, 1);
                svg_seat.classList.remove("booked");
                removeDeselectedSeat(seat);
            }
        }
        toggleReserveUpdateButton(currentSeatsBooked);
    });
}

/**
 * Fills the reservation form with the user's selected seats
 * Returns 'true' if the user has selected a seat/s, and 'false' if not.
 * @returns a Boolean
 */
function fillSeatReservationForm() {
    const selected_seats_list = document.querySelectorAll("#seats-selected-list>li");
    if (selected_seats_list.length != 0) {
        const limit_reached = document.getElementById("id_user_limit_reached");
        const select_seat_1 = document.querySelector("#id_seat_location_1");
        const select_seat_2 = document.querySelector("#id_seat_location_2");

        for (let i = 0; i < selected_seats_list.length; i++) {
            const seat_text = selected_seats_list[i].innerText.split(" ")[0];
            let seat_field = i == 0 ? select_seat_1 : select_seat_2;
            const options_list = Array.from(seat_field.options);
            const option_selected = options_list.filter(item => item.text == seat_text);
            seat_field.value = option_selected[0].value;
        }

        if (selected_seats_list.length == 2) {
            limit_reached.checked = true;
        } else {
            limit_reached.checked = false;
        }
        return true;
    } else {
        return false;
    }
}

/**
 * Displays a feedback message
 * @param {String} message 
 */
function showFeedBackMsg(message) {
    const feedbackBody = document.querySelector(".toast-body");
    const feedback = document.getElementById("feedbackToast");
    feedbackBody.textContent = message;
    const feedbackMessage = new bootstrap.Toast(feedback);
    feedbackMessage.show();
}

/**
 * Submits the user's newly selected seats, or deletes previously booked seats.
 * Also displays the loading SVG animation, and disables all buttons and links
 * while waiting for the reservation processing to complete.
 */
function submitSeatReservation() {
    if (fillSeatReservationForm()) {
        displayLoadingAnimation();
        disableAllInteractiveElements();
        const seat_form = document.getElementById("reserve-seat-form");
        seat_form.submit();
    } else {
        if (document.getElementById('update-reservation')) {
            const confirm_delete_btn = document.getElementById('confirm-delete');
            confirm_delete_btn.click();
        }
    }
}

/**
 * Gets the user's reserved or selected seats
 * @returns array of selected seats
 */
function getSelectedSeats() {
    const seatChoices = document.querySelectorAll('#seats-selected-list>li');
    const seatsArray = [];
    for (let seat of seatChoices) {
        seatsArray.push(seat.getAttribute('id'));
    }
    return seatsArray;
}

/**
 * Checks if the selected seats are the same as those already reserved by the user
 * @param {Array} currentSeatBooked
 * @returns a Boolean
 */
function sameSeatsAsOriginal(currentSeatBooked) {
    const newSeatChoices = getSelectedSeats();
    if (newSeatChoices.length === currentSeatBooked.length) {
        if (newSeatChoices.sort().join(',') === currentSeatBooked.sort().join(',')) {
            return true;
        }
        return false;
    }
    return false;
}

/**
 * Toggles the Reserve (or Update) Button on the Seat Reservation page
 * between enabling and disabling depending on the changes made by the user
 * on seat selection
 * @param {Array} currentSeatsBooked
 */
function toggleReserveUpdateButton(currentSeatsBooked) {
    if (!sameSeatsAsOriginal(currentSeatsBooked)) {
        enableReserveBtn();
    } else {
        disableReserveBtn();
    }
}

/**
 * Enables the 'Reserve' or 'Update button
 */
function enableReserveBtn() {
    const btn = document.querySelector('.reserve-btn');
    btn.classList.remove('disabled-btn');
}

/**
 * Disables the 'Reserve' or 'Update' button
 */
function disableReserveBtn() {
    const btn = document.querySelector('.reserve-btn');
    btn.classList.add('disabled-btn');
}

/**
 * Allow the Editing of Reserved Seats
 */
function allowEditingReservation() {
    const seatsBoxHeader = document.querySelector("#selected-seats-container>h3");
    const seatsBox = document.getElementById("selected-seats-inner-wrapper");
    const updateReservationBtn = document.getElementById("update-reservation");
    const seatsList = document.querySelectorAll("#seats-selected-list button");
    const seatMapBlocker = document.getElementById("seatmap-blocker");

    seatsBox.classList.remove("locked-style");

    seatsList.forEach( (btn) => {
        btn.classList.remove("disabled-btn");
        btn.removeAttribute("tabindex");
    });

    updateReservationBtn.classList.remove("d-none");
    this.classList.add("d-none");
    seatsBoxHeader.textContent = "Edit Your Reservation";
    seatMapBlocker.classList.add("d-none");
}

/**
 * Displays the loading SVG animation
 */
function displayLoadingAnimation() {
    const loadingSVGContainer = document.getElementById("loading-svg-container");
    loadingSVGContainer.style.display = "flex";
}

/**
 * Disables all the buttons and anchor tags in the page
 */
function disableAllInteractiveElements() {
    const buttonsLinks = document.querySelectorAll("button, a");
    buttonsLinks.forEach(function(elem) {
        if(elem.tagName === 'A') {
            elem.removeAttribute("href");
        } else {
            elem.disabled = true;
        }
    });
}
// --> FUNCTIONS [End] <--
