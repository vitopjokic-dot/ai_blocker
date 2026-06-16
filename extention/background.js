chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    console.log("got", msg);

    if (msg.type === "ANALYZE") {
        fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ text: msg.text })
        })
        .then(r => r.json())
        .then(d => {
            console.log("through");
            console.log("AIprob:", d.ai_score);
            sendResponse({ ai_score: d.ai_score });
        })
        .catch(e => {
            console.error("Backend error:", e);
            console.log("error");
            sendResponse({ ai_score: 0 });
        });
        return true;
    }
});