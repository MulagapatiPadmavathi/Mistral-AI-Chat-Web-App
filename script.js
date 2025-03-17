document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Display user message
        chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

        fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
            userInput.value = ""; // Clear input field
            chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
        })
        .catch(error => {
            console.error("Error:", error);
            chatBox.innerHTML += `<p style="color:red;">Error: Could not fetch response.</p>`;
        });
    }
});
