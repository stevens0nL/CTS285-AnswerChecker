function showModal(message) {
    document.getElementById('modal-text').innerText = message;
    document.getElementById('myModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('myModal')) {
        closeModal();
    }
}

// Timer for practice session
let timerInterval;
function startTimer() {
    let timeLeft = 15 * 60; // 15 minutes in seconds
    timerInterval = setInterval(() => {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        document.getElementById('timer').innerText = `Time left: ${minutes}:${seconds < 10 ? '0' : ''