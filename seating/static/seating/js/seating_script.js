window.onpageshow = function () {
    const reservedSeatsList = document.getElementById('data_seats').textContent;
    const seatsList = document.querySelectorAll('[data-seat-location]');
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
                    if (seat.classList.contains("booked")) {
                        num_seats_chosen += toggleSeat(seat, seat_loc)
                    }
                }
            })
        }
    }
}

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
    const li_elem = document.getElementById(seat_loc);
    li_elem.remove()
}