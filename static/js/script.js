document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const chatWindow = document.getElementById('chat-window');
        
        const userMessageDiv = document.createElement('div');
        userMessageDiv.classList.add('user-message');
        const userMessageContent = document.createElement('div');
        userMessageContent.textContent = userInput;
        userMessageDiv.appendChild(userMessageContent);
        chatWindow.appendChild(userMessageDiv);

        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('bot-message');
        const botMessageContent = document.createElement('div');
        botMessageContent.textContent = data.response;
        botMessageDiv.appendChild(botMessageContent);
        chatWindow.appendChild(botMessageDiv);

        // Show alert with the response
        alert(`Response from server: ${data.response}`);

        document.getElementById('user-input').value = '';
        chatWindow.scrollTop = chatWindow.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}

// Initiate conversation when the chat page loads
window.onload = function() {
    const chatWindow = document.getElementById('chat-window');
    const botMessageDiv = document.createElement('div');
    botMessageDiv.classList.add('bot-message');
    const botMessageContent = document.createElement('div');
    botMessageContent.textContent = "Hello! How can I assist you today? You can ask me about admissions, programs, fees, facilities, placements, or contact information.";
    botMessageDiv.appendChild(botMessageContent);
    chatWindow.appendChild(botMessageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
