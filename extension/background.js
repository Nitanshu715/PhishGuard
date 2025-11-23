// background.js

async function analyzeCurrentTab(tabId) {
  const tab = await chrome.tabs.get(tabId);
  const url = tab.url;

  // Validate URL
  if (!url || !url.includes(".")) {
    chrome.action.setBadgeText({ text: "-" });
    chrome.storage.local.set({ lastResult: null });
    return;
  }

  let data;

  try {
    const response = await fetch("http://127.0.0.1:5000/check_url", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const raw = await response.text();

    try {
      data = JSON.parse(raw);
    } catch {
      console.error("Backend did not return JSON:", raw);
      return;
    }

  } catch (err) {
    console.error("Network error:", err);
    return;
  }

  // Save result for popup
  chrome.storage.local.set({ lastResult: data });

  // Badge update
  let text = "?";
  let color = "#777777";

  if (data.label === "safe") {
    text = "OK";
    color = "#00FF00";
  } else if (data.label === "suspicious") {
    text = "??";
    color = "#FFA500";
  } else if (data.label === "malicious") {
    text = "X";
    color = "#FF0000";
  }

  chrome.action.setBadgeText({ text });
  chrome.action.setBadgeBackgroundColor({ color });
}

// Auto scan
chrome.tabs.onActivated.addListener(info => analyzeCurrentTab(info.tabId));
chrome.tabs.onUpdated.addListener((tabId, changeInfo) => {
  if (changeInfo.status === "complete") analyzeCurrentTab(tabId);
});
