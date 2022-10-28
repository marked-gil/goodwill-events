window.onpageshow = function () {
    const reservedSeatsList = document.getElementById('data_seats').textContent;
    const seatsList = document.querySelectorAll('[data-seat-location]');
    for (let seat of seatsList) {
        const seat_loc = seat.getAttribute("data-seat-location")
        if (reservedSeatsList.includes(seat_loc)) {
            seat.style.fill = "blue";
        } else {
            seat.style.cursor = 'pointer'
            seat.addEventListener('click', function () {
                this.classList.toggle("booked");
                showSelectedSeat(this, seat_loc);
                removeDeselectedSeat(this, seat_loc);
            })
        }
    }
}

function showSelectedSeat(seat, seat_loc) {
    if (seat.classList.contains("booked")) {
        const li_elem = document.createElement("li");
        li_elem.innerText = seat_loc;
        document.getElementById("seats_selected_list").appendChild(li_elem)
        li_elem.setAttribute('id', seat_loc)
    }
}


function removeDeselectedSeat(seat, seat_loc) {
    if (!seat.classList.contains("booked")) {
        const li_elem = document.getElementById(seat_loc);
        li_elem.remove()
    }
}