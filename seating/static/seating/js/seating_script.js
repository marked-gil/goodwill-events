if (document.getElementById('seatmap-container')) {
    const reservedSeatsList = document.getElementById('data_seats').textContent;
    const seatsList = document.querySelectorAll('[data-seat-location]');

    window.onpageshow = function () {
        ALLOWED_SEATS_PER_USER = 2
        num_seats_chosen = 0
        for (let seat of seatsList) {
            const seat_loc = seat.getAttribute("data-seat-location");
            if (reservedSeatsList.includes(seat_loc)) {
                seat.style.fill = "blue";
            } else {
                seat.style.cursor = 'pointer'
                seat.addEventListener('click', function () {
                    if (num_seats_chosen < ALLOWED_SEATS_PER_USER) {
                        num_seats_chosen += toggleSeat(this, seat_loc);
                    } else {
                        if (this.classList.contains("booked")) {
                            num_seats_chosen += toggleSeat(this, seat_loc)
                        }
                    }
                })
            }
        }
    }
    
    // EventListener for form submission
    if (document.getElementById("submit_reservation")) {
        const reserve_button = document.getElementById("submit_reservation");
        reserve_button.addEventListener('click', submitSeatReservation)
    }

    // EventListener for 'remove' reserved seat button
    if (document.getElementsByClassName("btn_seat_location")) {
        const remove_seat_buttons = document.querySelectorAll('.btn_seat_location')
        remove_seat_buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
                seat = this.parentElement
                removeDeselectedSeat(seat);

                for (seat_box of seatsList) {
                    seat_location = seat_box.getAttribute("data-seat-location")
                    if (seat_location == seat.getAttribute("id")) {
                        seat_box.style.fill = ""
                    }
                }

            })
        })
    }

    
    // FUNCTIONS <---
    
    function toggleSeat(seat, seat_loc) {
        seat.classList.toggle("booked");
        if (seat.classList.contains("booked")) {
            showSelectedSeat(seat_loc);
            return 1
        } else {
            removeDeselectedSeat(seat_loc);
            return -1
        }
    }
    
    function showSelectedSeat(seat_loc) {
        const li_elem = document.createElement("li");
        li_elem.innerText = seat_loc;
        document.getElementById("seats_selected_list").appendChild(li_elem)
        li_elem.setAttribute('id', seat_loc)
    }
    
    function removeDeselectedSeat(seat_loc) {
        if (typeof seat_loc == "string") {
            const li_elem = document.getElementById(seat_loc)
            li_elem.remove()
        } else if (typeof seat_loc == "object") {
            seat_loc.remove()
        }
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
    }

    function submitSeatReservation() {
        fillSeatReservationForm()
        // submit form
        const seat_form = document.getElementById("reserve_seat_form")
        seat_form.submit();
    }
}
