function showModal(message) {
    document.getElementById('modal-text').innerText = message;
    document.getElementById('myModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
    // Redirect or handle session end
    if (document.getElementById('modal-text').innerText.includes('session')) {
        // Assume session end logic handled by Flask
    }
}

window.onclick = function(event) {
    if (event.target == document.getElementById('myModal')) {
        closeModal();
    }
}
