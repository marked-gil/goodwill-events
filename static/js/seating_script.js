if (document.getElementById('seatmap-container')) {
    const string_reserved_seats = document.getElementById('data-seats').textContent;
    let list_reserved_seats = string_reserved_seats.replace(/[^a-zA-Z0-9_,]/g, '').split(",");

    window.onpageshow = function () {
        const svg_seats_list = document.querySelectorAll('[data-seat-location]');
        for (let svg_seat of svg_seats_list) {
            const seat_loc = svg_seat.getAttribute("data-seat-location");
            blockReservedSeats(svg_seat, seat_loc, list_reserved_seats);
            makeAllFreeSeatsClickable(svg_seat, seat_loc);
        }
    }
    
    // EventListener to 'remove' reserved seat
    if (document.getElementsByClassName("btn-seat-location")) {
        const cancel_seat_buttons = document.querySelectorAll('.btn-seat-location');
        cancel_seat_buttons.forEach(cancelSeat);
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
    

    // ---> FUNCTIONS <---
    
    function blockReservedSeats(svg_seat, seat_loc, list_reserved_seats) {
        if (list_reserved_seats.includes(seat_loc)) {
            svg_seat.classList.add("booked")
        }
    }

    function makeAllFreeSeatsClickable(svg_seat, seat_loc) {
        const ALLOWED_SEATS_PER_USER = 2
        svg_seat.style.cursor = 'pointer'
        svg_seat.addEventListener('click', function () {
            if (SelectedSeatsByUser().length < ALLOWED_SEATS_PER_USER) {
                toggleSeat(this, seat_loc)
            } else {
                if (this.classList.contains("user-selected")) {
                    toggleSeat(this, seat_loc)
                }
            }
        })
    }

    function toggleSeat(seat, seat_loc) {
        seat.classList.toggle("user-selected");
        if (seat.classList.contains("user-selected")) {
            showSelectedSeat(seat_loc);
        } else {
            removeDeselectedSeat(seat_loc);
        }
    }
    
    function showSelectedSeat(seat_loc) {
        const li_elem = document.createElement("li");
        li_elem.innerText = seat_loc;
        document.getElementById("seats-selected-list").appendChild(li_elem);
        li_elem.setAttribute('id', seat_loc);
        li_elem.setAttribute('class', 'd-flex align-items-center me-4')
    }
    
    function removeDeselectedSeat(seat_loc) {
        if (typeof seat_loc == "string") {
            const li_elem = document.getElementById(seat_loc)
            li_elem.remove()
        } else if (typeof seat_loc == "object") {
            seat_loc.remove()
        }
    }

    function SelectedSeatsByUser() {
        const user_reserved_seats = document.querySelectorAll("#seats-selected-list > li")
        return user_reserved_seats
    }

    function cancelSeat(btn) {
        const svg_seats_list = document.querySelectorAll('[data-seat-location]');
        const string_reserved_seats = document.getElementById('data-seats').textContent;
        let list_reserved_seats = string_reserved_seats.replace(/[^a-zA-Z0-9_,]/g, '').split(",");
        btn.addEventListener('click', function () {
            seat = this.parentElement
            for (svg_seat of svg_seats_list) {
                seat_location = svg_seat.getAttribute("data-seat-location")
                if (seat_location == seat.getAttribute("id")) {
                    const seat_index = list_reserved_seats.indexOf(seat_location)
                    list_reserved_seats.splice(seat_index, 1)
                    svg_seat.classList.remove("booked")
                    removeDeselectedSeat(seat);
                }
            }
        })
    }

    function fillSeatReservationForm() {
        const selected_seats_list = document.querySelectorAll("#seats-selected-list>li")
        if (selected_seats_list.length != 0) {
            const limit_reached = document.getElementById("id_user_limit_reached")
            const select_seat_1 = document.querySelector("#id_seat_location_1")
            const select_seat_2 = document.querySelector("#id_seat_location_2")
    
            for (let i = 0; i < selected_seats_list.length; i++) {
                const seat_text = selected_seats_list[i].innerText.split(" ")[0]
                let seat_field = i == 0 ? select_seat_1 : select_seat_2
                const options_list = Array.from(seat_field.options)
                const option_selected = options_list.filter(item => item.text == seat_text)
                seat_field.value = option_selected[0].value
            }
    
            if (selected_seats_list.length == 2) {
                limit_reached.checked = true;
            } else {
                limit_reached.checked = false;
            }
            return true
        } else {
            return false
        }
        
    }

    function submitSeatReservation() {
        if (fillSeatReservationForm()) {
            const seat_form = document.getElementById("reserve-seat-form")
            seat_form.submit();
        } else {
            if (document.getElementById('update-reservation')) {
                const confirm_delete_btn = document.getElementById('confirm-delete')
                confirm_delete_btn.click()
            }
        }
    }
}
