// Leaflet Map Setup
var map = L.map('map').setView([39.945088, 262.421494], 3.5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function onMapClick(e) {
    alert( e.latlng);
}

map.on('click', onMapClick);

var marker = L.marker([39.945088, 262.421494]).addTo(map);

// Chatbot Functionality
function toggleChat() {
    const chatbox = document.getElementById("chatbox");
    chatbox.style.display = chatbox.style.display === "none" ? "block" : "none";
}

async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");
    const userMessage = inputField.value.trim();

    if (!userMessage) return;

    chatMessages.innerHTML += `<div class="user-message">${userMessage}</div>`;
    inputField.value = "";

    try {
        const response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
            mode: "no-cors"  // This will bypass CORS but you won't get a readable response
        });
        

        const data = await response.json();

        if (data.response) {
            chatMessages.innerHTML += `<div class="bot-message">${data.response}</div>`;
        } else {
            chatMessages.innerHTML += `<div class="bot-message">Error: ${data.error}</div>`;
        }
    } catch (error) {
        chatMessages.innerHTML += `<div class="bot-message">Error: Unable to reach server</div>`;
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
}



