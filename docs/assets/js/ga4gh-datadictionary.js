document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("ga4gh-dict-search");
  const tableBody = document.querySelector("#ga4gh-dict-table tbody");

  if (!input || !tableBody) return;

  fetch("../assets/datadictionary.csv")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      return response.text();
    })
    .then((text) => {
      const rows = parseCSV(text);

      if (!rows.length) {
        tableBody.innerHTML =
          "<tr><td colspan='3'>No data found.</td></tr>";
        return;
      }

      const headers = rows[0];
      const data = rows.slice(1).map((row) => {
        const obj = {};
        headers.forEach((h, i) => {
          obj[h] = row[i] || "";
        });
        return obj;
      });

      renderRows(data);

      input.addEventListener("input", function () {
        const q = input.value.toLowerCase().trim();
        const filtered = data.filter((row) =>
          Object.values(row).some((value) =>
            String(value).toLowerCase().includes(q)
          )
        );
        renderRows(filtered);
      });
    })
    .catch((error) => {
      tableBody.innerHTML =
        "<tr><td colspan='5'>Could not load data dictionary.</td></tr>";
      console.error("Data dictionary load error:", error);
    });

  function renderRows(rows) {
    if (!rows.length) {
      tableBody.innerHTML =
        "<tr><td colspan='3'>No matching rows.</td></tr>";
      return;
    }

    tableBody.innerHTML = rows
      .map(
        (row) => `
          <tr>
            <td>${escapeHtml(row["Sheet Name"] || "")}</td>
            <td>${escapeHtml(row["Variable Name"] || "")}</td>
            <td>${escapeHtml(row["Data Type"] || "")}</td>
          </tr>
        `
      )
      .join("");
  }

  function parseCSV(text) {
    const lines = [];
    let row = [];
    let value = "";
    let inQuotes = false;

    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      const next = text[i + 1];

      if (char === '"') {
        if (inQuotes && next === '"') {
          value += '"';
          i++;
        } else {
          inQuotes = !inQuotes;
        }
      } else if (char === "," && !inQuotes) {
        row.push(value);
        value = "";
      } else if ((char === "\n" || char === "\r") && !inQuotes) {
        if (char === "\r" && next === "\n") i++;
        row.push(value);
        if (row.some((cell) => cell !== "")) lines.push(row);
        row = [];
        value = "";
      } else {
        value += char;
      }
    }

    if (value.length || row.length) {
      row.push(value);
      lines.push(row);
    }

    return lines;
  }

  function escapeHtml(str) {
    return String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
});
