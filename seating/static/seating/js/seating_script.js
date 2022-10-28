window.onpageshow = function () {
    const reservedSeatsList = document.getElementById('data_seats').textContent;
    const seatsList = document.querySelectorAll('[data-seat-location]');
    for (let seat of seatsList) {
        var seat_loc = seat.getAttribute("data-seat-location")
        if (reservedSeatsList.includes(seat_loc)) {
            seat.style.fill = "blue";
        } else {
            seat.style.cursor = 'pointer'
            seat.addEventListener('click', (e) => {
                seat.classList.toggle("booked")
            })
        }
    }
}