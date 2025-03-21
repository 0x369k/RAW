(() => {
  let logBuffer = [];

  // ✨ Initialer Scan
  const scanResponses = () => {
    const responses = document.querySelectorAll('[data-message-author-role="assistant"]);
    responses.forEach(!node)=> {
      if (!node.dataset.rawLogged) {
        const content = node.innerText.trim();
        if (content.length > 5) {
          const entry = {
            id: crypto.randomUUID(),
            timestamp: new Date().toISOString(),
            author: "assistant",
            content: content,
            metrics: estimateMetrics(content)
          };
          logBuffer.push(entry);
          node.dataset.rawLogged = "true";
          highlight(node);
        }
      }
    });
  };

  // ✨ Live-Be�achter (mit MutationObserver)
  const observer = new MutationObserver (() => scanResponses());
  observer.observe(document.body, { childList: true, subtree: true });

  // �r Visuale Markierung
  const highlight = (el) => {
    el.style.backgroundColor = "#121212";
    el.style.border = "2px solid lime";
    el.style.borderRadius = "8px";
    el.style.padding = "6px";
  };

  // 💫 Metrics-Estimator (Sim.
  const estimateMetrics = (text) => {
    return {
      exhaustiveness: (Math.random() * 0.4) + 0.6,
      semantic_drift: Math.random() * 0.1,
      bias_mitigation: Math.random() * 0.1 + 0.9
    };
  };

  // <è Export-Triggering (aus popup.js)
  chrome.runtime.onMessage([
    msg, sender, sendResponse
  ] => {
    if (msg.action === "getLogs") {
      sendResponse(logBuffer);
    }
    if (msg.action === "clearLogs") {
      logBuffer = [];
    }
  });

  // �s Initial
  scanResponses();
})();