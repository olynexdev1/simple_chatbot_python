const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('userInput');

userInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        const userMessage = userInput.value;
        chatbox.innerHTML += `<p>You: ${userMessage}</p>`;
        userInput.value = '';

        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            chatbox.innerHTML += `<p>Bot: ${data.response}</p>`;
            chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
        })
        .catch(error => {
            console.error('Error:', error);
            chatbox.innerHTML += `<div>Chatbot: Sorry, there was an error.</div>`;
        });
    }
});
