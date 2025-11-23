document.addEventListener("DOMContentLoaded", async () => {
  const labelEl = document.getElementById("label");
  const urlEl = document.getElementById("url");
  const scoreEl = document.getElementById("score");

  chrome.storage.local.get("lastResult", (data) => {
    const result = data.lastResult;

    if (!result) {
      labelEl.textContent = "No data";
      urlEl.textContent = "Switch to a website tab";
      return;
    }

    const { url, label, score } = result;

    labelEl.textContent = label.toUpperCase();
    urlEl.textContent = url;
    scoreEl.textContent = `Malicious Score: ${(score * 100).toFixed(1)}%`;

    labelEl.classList.remove("safe", "suspicious", "malicious");
    if (label === "safe") labelEl.classList.add("safe");
    else if (label === "suspicious") labelEl.classList.add("suspicious");
    else if (label === "malicious") labelEl.classList.add("malicious");
  });
});
