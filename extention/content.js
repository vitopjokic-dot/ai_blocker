console.log("AI BLOCKER LOADED");

const seen = new Set();

function normalizeText(text) {
    return (text || "").replace(/\s+/g, " ").trim();
}

function getSiteConfig() {
    const host = window.location.hostname.toLowerCase();

    if (host.includes("reddit")) {
        return {
            name: "Reddit",
            selector: "shreddit-post",
            fallbackSelector: "article, [role='article']"
        };
    }

    if (host.includes("twitter") || host.includes("x.com")) {
        return {
            name: "Twitter/X",
            selector: "article [data-testid='tweetText'], article [data-testid='tweet']",
            fallbackSelector: "article, [role='article']"
        };
    }

    if (host.includes("facebook")) {
        return {
            name: "Facebook",
            selector: "[role='article']",
            fallbackSelector: "article, [role='article']"
        };
    }

    if (host.includes("instagram")) {
        return {
            name: "Instagram",
            selector: "article, [role='article']",
            fallbackSelector: "article, [role='article']"
        };
    }

    if (host.includes("linkedin")) {
        return {
            name: "LinkedIn",
            selector: "[data-id='main-feed'], .feed-shared-update-v2, [role='article']",
            fallbackSelector: "article, [role='article']"
        };
    }

    if (host.includes("youtube")) {
        return {
            name: "YouTube",
            selector: "#content-text",
            fallbackSelector: "ytd-comment-renderer"
        };
    }

    return {
        name: "Generic social site",
        selector: "article, [role='article'], [data-testid*='post'], [data-testid*='message']",
        fallbackSelector: "article, [role='article']"
    };
}

function extractText(element) {
    if (!element) return "";

    const text = element.innerText || element.textContent || "";
    return normalizeText(text);
}

function applyFilter(element, score) {
    element.style.filter = "blur(8px)";
    element.style.opacity = "0.4";
    element.style.cursor = "pointer";
    element.onmouseenter = () => { element.style.filter = "none"; element.style.opacity = "1"; };
    element.onmouseleave = () => { element.style.filter = "blur(8px)"; element.style.opacity = "0.4"; };

    element.dataset.aiBlocked = "true";
    console.log(`Blurred-AIprob: ${(score * 100).toFixed(1)}%`);
}

function getCandidates() {
    const config = getSiteConfig();
    const elements = Array.from(document.querySelectorAll(config.selector));

    if (elements.length > 0) {
        return elements;
    }

    return Array.from(document.querySelectorAll(config.fallbackSelector));
}

function scan() {
    const config = getSiteConfig();
    const candidates = getCandidates();

    console.log(`${config.name} detected on ${window.location.hostname}; candidates found:`, candidates.length);

    candidates.forEach(candidate => {
        const text = extractText(candidate);

        if (!text || text.length < 8 || seen.has(text) || candidate.dataset.aiBlocked) return;

        seen.add(text);

        console.log("to flask:", text.slice(0, 60));

        chrome.runtime.sendMessage({
            type: "ANALYZE",
            text
        }, (response) => {
            if (response && typeof response.ai_score === "number") {
                console.log("AIprob:", response.ai_score);
                if (response.ai_score >= 0.8) {
                    applyFilter(candidate, response.ai_score);
                }
            }
        });
    });
}

const observer = new MutationObserver(() => {
    scan();
});

if (document.body) {
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
}

scan();
