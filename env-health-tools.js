/*
  Environmental data hubs and mapping tools table (Mapping tab).

  Reads assets/env-health-tools.csv and renders a filterable table.
  Columns expected: Scale, State, Tool/Hub Name, Organization, Type, URL, Notes.
  Safe to load on every page: it exits quietly when its markup is absent.
*/
/* Resolve the CSV relative to this script's own URL, so the page works
   both at the site root (mkdocs serve) and in a subdirectory such as
   the GitHub Pages path /ALS-RWE/. Must run at top level, because
   document.currentScript is null inside the DOMContentLoaded callback. */
const EHT_CSV_URL = (function () {
  const self = document.currentScript && document.currentScript.src;
  if (self) return new URL("../env-health-tools.csv", self).href;
  return "assets/env-health-tools.csv";
})();

document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("eht-search");
  const tableBody = document.querySelector("#eht-table tbody");
  const countEl = document.getElementById("eht-count");
  const scaleButtons = document.querySelectorAll(".eht-scale-btn");

  if (!input || !tableBody) return;

  const COLSPAN = 3;
  let data = [];
  let activeScale = "all";

  setMessage("Loading list...");

  fetch(EHT_CSV_URL)
    .then((response) => {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.text();
    })
    .then((text) => {
      const rows = parseCSV(text);
      if (!rows.length) {
        setMessage("No data found.");
        return;
      }

      const headers = rows[0].map((h) => h.replace(/^\uFEFF/, "").trim());
      data = rows.slice(1).map((row) => {
        const obj = {};
        headers.forEach((h, i) => {
          obj[h] = (row[i] || "").trim();
        });
        return obj;
      });

      input.addEventListener("input", render);
      scaleButtons.forEach((btn) => {
        btn.addEventListener("click", function () {
          scaleButtons.forEach((b) => b.classList.remove("active"));
          btn.classList.add("active");
          activeScale = btn.dataset.scale;
          render();
        });
      });

      render();
    })
    .catch((error) => {
      setMessage("Could not load the list.");
      console.error("Environmental data hubs load error:", error);
    });

  function render() {
    const q = input.value.toLowerCase().trim();

    const filtered = data.filter((row) => {
      if (activeScale !== "all" && (row["Scale"] || "").toLowerCase() !== activeScale) {
        return false;
      }
      if (!q) return true;
      return ["Tool/Hub Name", "Organization", "State", "Scale", "Type", "Notes"].some(
        (key) => String(row[key] || "").toLowerCase().includes(q)
      );
    });

    if (countEl) {
      countEl.textContent =
        filtered.length + (filtered.length === 1 ? " entry" : " entries");
    }

    if (!filtered.length) {
      setMessage("No entries match that search.");
      return;
    }

    tableBody.innerHTML = filtered.map(renderRow).join("");
  }

  function renderRow(row) {
    const place = row["State"] || "National";
    const name = escapeHtml(row["Tool/Hub Name"]);
    const url = row["URL"] || "";
    const isLink = /^https?:\/\//i.test(url);
    const link = isLink
      ? '<a href="' + escapeHtml(url) + '" target="_blank" rel="noopener">' + name + "</a>"
      : name;

    const note = row["Notes"]
      ? '<div class="eht-note">' + escapeHtml(row["Notes"]) + "</div>"
      : "";

    return (
      "<tr>" +
      "<td><strong>" + link + "</strong>" +
      '<div class="eht-org">' + escapeHtml(row["Organization"]) + "</div>" + note + "</td>" +
      "<td>" + escapeHtml(place) + "</td>" +
      "<td>" + escapeHtml(row["Type"]) + "</td>" +
      "</tr>"
    );
  }

  function setMessage(msg) {
    tableBody.innerHTML =
      '<tr><td colspan="' + COLSPAN + '" class="eht-loading">' + escapeHtml(msg) + "</td></tr>";
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
