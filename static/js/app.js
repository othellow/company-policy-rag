async function askQuestion() {

    const questionInput = document.getElementById("question");
    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    const chatHistory = document.getElementById("chat-history");

    chatHistory.innerHTML += `
        <div class="user-message">
            <div class="message-label">👤 You</div>
            <div>${question}</div>
        </div>
    `;

    const loadingId = `loading-${Date.now()}`;

    chatHistory.innerHTML += `
        <div id="${loadingId}" class="loading">
            🤖 Othellow AI is searching company policies...
        </div>
    `;

    questionInput.value = "";
    questionInput.focus();

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });

    const data = await response.json();

    let sourcesHtml = "";

    if (data.sources && data.sources.length > 0) {
        sourcesHtml = "<div class='sources'><strong>Sources</strong><ul>";

        data.sources.forEach(source => {
            sourcesHtml += `<li>${source}</li>`;
        });

        sourcesHtml += "</ul></div>";
    }

    const answerHtml = `
        <div class="ai-message">
            <div class="message-label">🤖 Othellow AI</div>
            <div>${data.answer}</div>
            ${sourcesHtml}
        </div>
    `;

    const loadingElement = document.getElementById(loadingId);

    if (loadingElement) {
        loadingElement.outerHTML = answerHtml;
    }

    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });
}
