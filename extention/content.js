console.log("AI BLOCKER LOADED");

const seen = new Set();

function applyFilter(element, score) {
    element.style.filter = "blur(8px)";
    element.style.opacity = "0.4";
    element.style.cursor = "pointer";
    element.onmouseenter = () => { element.style.filter = "none"; element.style.opacity = "1"; };
    element.onmouseleave = () => { element.style.filter = "blur(8px)"; element.style.opacity = "0.4"; };
    
    console.log(`Blurred-AIprob: ${(score * 100).toFixed(1)}%`);
}

function scan() {
    const posts = document.querySelectorAll("shreddit-post");

    console.log("posts found:", posts.length);

    posts.forEach(post => {

        const text = post.innerText;

        if (!text || seen.has(text)) return;

        seen.add(text);

        console.log("to flask:", text.slice(0, 50));

        chrome.runtime.sendMessage({
            type: "ANALYZE",
            text
        }, (response) => {
            console.log("AIprob:", response.ai_score);
            if (response && response.ai_score >= 0.8) {
                applyFilter(post, response.ai_score);
            }
        });
    });
}

const observer = new MutationObserver(() => {
    scan();
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});

scan();

