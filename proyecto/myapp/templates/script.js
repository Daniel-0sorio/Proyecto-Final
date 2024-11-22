// script.js
document.getElementById('loginBtn').onclick = () => openModal('loginModal');
document.getElementById('registerBtn').onclick = () => openModal('registerModal');
document.getElementById('reportBtn').onclick = () => openModal('reportModal');

function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}
