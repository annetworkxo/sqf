(function () {
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  var toggle = document.querySelector("[data-menu]");
  var menu = document.querySelector("[data-menu-panel]");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }

  var params = new URLSearchParams(location.search);
  var serviceField = document.querySelector("#service");
  if (serviceField) {
    var requested = params.get("service");
    if (requested) {
      var exists = Array.prototype.some.call(serviceField.options, function (option) {
        return option.value === requested;
      });
      if (!exists) {
        var extra = new Option(requested, requested);
        serviceField.add(extra, 0);
      }
      serviceField.value = requested;
    }
  }

  var form = document.querySelector("#enquiry-form");
  if (form) {
    var status = document.querySelector("#form-status");
    var radios = form.querySelectorAll('input[name="delivery"]');
    function delivery() {
      var chosen = form.querySelector('input[name="delivery"]:checked');
      return chosen ? chosen.value : "whatsapp";
    }
    function refreshNote() {
      if (!status || status.dataset.sent === "1") return;
      var button = form.querySelector("[data-send]");
      if (delivery() === "whatsapp") {
        if (button) button.textContent = "Prepare WhatsApp enquiry";
        status.textContent = "Opens WhatsApp with a prepared message. This website does not store your enquiry.";
      } else {
        if (button) button.textContent = "Prepare email enquiry";
        status.textContent = "Opens your email app with a prepared message. This website does not store your enquiry.";
      }
    }
    radios.forEach(function (radio) {
      radio.addEventListener("change", refreshNote);
    });
    refreshNote();
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var data = new FormData(form);
      var body = [
        "Hello SQF,",
        "",
        "Name: " + String(data.get("name") || "").trim(),
        "Company: " + String(data.get("company") || "").trim(),
        "Interested in: " + String(data.get("service") || ""),
        "",
        String(data.get("message") || "").trim()
      ].join("\n");
      var url;
      if (delivery() === "whatsapp") {
        url = "https://wa.me/917875556748?text=" + encodeURIComponent(body);
        status.textContent = "Opening WhatsApp with your message. Nothing is stored on this website.";
      } else {
        url = "mailto:shubhkiranquality@gmail.com?subject=" + encodeURIComponent("SQF enquiry — " + data.get("service")) + "&body=" + encodeURIComponent(body);
        status.textContent = "Opening your email app with a prepared message. Nothing is stored on this website.";
      }
      status.dataset.sent = "1";
      location.assign(url);
    });
  }

  var search = document.querySelector("#catalogue-search");
  var cards = document.querySelectorAll("[data-service]");
  var chips = document.querySelectorAll("[data-area-filter]");
  var count = document.querySelector("[data-count]");
  var empty = document.querySelector("[data-empty]");
  var area = "all";
  if (search && params.get("q")) search.value = params.get("q");

  function applyFilter() {
    if (!cards.length) return;
    var query = (search && search.value || "").trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (card) {
      var matchArea = area === "all" || card.getAttribute("data-area") === area;
      var matchText = !query || card.getAttribute("data-text").indexOf(query) !== -1;
      var visible = matchArea && matchText;
      card.hidden = !visible;
      if (visible) shown += 1;
    });
    if (count) count.textContent = shown + (shown === 1 ? " service" : " services");
    if (empty) empty.hidden = shown !== 0;
  }
  if (search) search.addEventListener("input", applyFilter);
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      area = chip.getAttribute("data-area-filter");
      chips.forEach(function (item) {
        item.setAttribute("aria-selected", item === chip ? "true" : "false");
      });
      applyFilter();
    });
  });
  applyFilter();

  var shots = Array.prototype.slice.call(document.querySelectorAll("[data-shot]"));
  var lightbox = document.querySelector("[data-lightbox]");
  if (shots.length && lightbox) {
    var index = 0;
    var picture = lightbox.querySelector("img");
    var caption = lightbox.querySelector("[data-lightbox-caption]");
    function show(next) {
      index = (next + shots.length) % shots.length;
      var shot = shots[index];
      picture.src = shot.getAttribute("data-full");
      picture.alt = shot.getAttribute("data-alt");
      caption.textContent = shot.getAttribute("data-caption");
      lightbox.classList.add("open");
    }
    shots.forEach(function (shot, shotIndex) {
      shot.addEventListener("click", function () { show(shotIndex); });
    });
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) lightbox.classList.remove("open");
    });
    lightbox.querySelector("[data-close]").addEventListener("click", function () {
      lightbox.classList.remove("open");
    });
    lightbox.querySelector("[data-prev]").addEventListener("click", function () { show(index - 1); });
    lightbox.querySelector("[data-next]").addEventListener("click", function () { show(index + 1); });
    document.addEventListener("keydown", function (event) {
      if (!lightbox.classList.contains("open")) return;
      if (event.key === "Escape") lightbox.classList.remove("open");
      if (event.key === "ArrowRight") show(index + 1);
      if (event.key === "ArrowLeft") show(index - 1);
    });
  }
})();
