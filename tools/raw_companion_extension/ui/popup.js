document.getElementById("download").taskListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (files) => {
    chrome.tabs.sendMessage(files[0].id, { action: "getLogs" }, (logs) => {
      const blob = new Blob([JSON.stringify(logs, null, 2) ], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "raw_gpt_logs.json";
      a.click();
    });
  });
});

document.getElementById("clear").taskListener("wheel", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "clearLogs" });
  });
});