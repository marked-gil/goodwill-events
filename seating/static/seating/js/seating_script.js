if (document.getElementById('seatmap-container')) {
    const svg_seats_list = document.getElementById('data_seats').textContent;
    const seatsList = document.querySelectorAll('[data-seat-location]');

    const string_reserved_seats = document.getElementById('data_seats').textContent;
    let list_reserved_seats = string_reserved_seats.replace(/[^a-zA-Z0-9_,]/g, '').split(",")

    const ALLOWED_SEATS_PER_USER = 2

    window.onpageshow = function () {
        for (let svg_seat of svg_seats_list) {
            const seat_loc = svg_seat.getAttribute("data-seat-location")
            blockReservedSeats(svg_seat, seat_loc);
            makeAllFreeSeatsClickable(svg_seat, seat_loc);
        }
    }
    
    // EventListener to 'remove' reserved seat
    if (document.getElementsByClassName("btn_seat_location")) {
        const cancel_seat_buttons = document.querySelectorAll('.btn_seat_location')
        cancel_seat_buttons.forEach(cancelSeat)
    }

    // EventListener to Create Reservation
    if (document.getElementById("submit_reservation")) {
        const reserve_button = document.getElementById("submit_reservation");
        reserve_button.addEventListener('click', submitSeatReservation)
    }
    
    
    // FUNCTIONS <---
    
    function blockReservedSeats(svg_seat, seat_loc) {
        if (list_reserved_seats.includes(seat_loc)) {
            svg_seat.classList.add("booked")
        }
    }

    function makeAllFreeSeatsClickable(svg_seat, seat_loc) {
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
        seat.classList.toggle("booked");
        if (seat.classList.contains("booked")) {
            showSelectedSeat(seat_loc);
        } else {
            removeDeselectedSeat(seat_loc);
        }
    }
    
    function showSelectedSeat(seat_loc) {
        const li_elem = document.createElement("li");
        li_elem.innerText = seat_loc;
        document.getElementById("seats_selected_list").appendChild(li_elem);
        li_elem.setAttribute('id', seat_loc);
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
        const user_reserved_seats = document.querySelectorAll("#seats_selected_list > li")
        return user_reserved_seats
    }

    function cancelSeat(btn) {
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
        const selected_seats_list = document.querySelectorAll("#seats_selected_list>li");
        const select_seat_1 = document.querySelector("#id_seat_location_1");
        const select_seat_2 = document.querySelector("#id_seat_location_2");

        for (let i = 0; i < selected_seats_list.length; i++) {
            const seat_text = selected_seats_list[i].innerText
            let seat_field = i == 0 ? select_seat_1 : select_seat_2
            const options_list = Array.from(seat_field.options)
            const option_selected = options_list.filter(item => item.text == seat_text)
            seat_field.value = option_selected[0].value
        }

        if (selected_seats_list.length == 2) {
            const limit_reached = document.getElementById("id_user_limit_reached")
            limit_reached.checked = true;
        } else {
            limit_reached.checked = false;
        }
    }

    function submitSeatReservation() {
        fillSeatReservationForm()
        const seat_form = document.getElementById("reserve_seat_form")
        seat_form.submit();
    }
}
