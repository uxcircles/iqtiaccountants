/* IQTi Accountants — header, menu, reveal, fee estimator, MTD checker, Stamp Duty calculator, quote form */
(function () {
  "use strict";
  var T = window.IQTI || {};
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var gbp = function (n) { return Math.round(n).toLocaleString("en-GB"); };
  var num = function (v) { return parseFloat(String(v || "").replace(/[^\d.]/g, "")) || 0; };

  // year
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  // header shadow on scroll
  var header = $("[data-header]");
  var onScroll = function () { if (header) header.classList.toggle("scrolled", window.scrollY > 8); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // mobile menu
  var btn = $(".menu-btn"), menu = $("#menu");
  function setMenu(open) {
    btn.setAttribute("aria-expanded", String(open));
    menu.hidden = !open;
    document.body.classList.toggle("menu-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { var first = $("a", menu); if (first) first.focus(); }
  }
  if (btn && menu) {
    btn.addEventListener("click", function () { setMenu(btn.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !menu.hidden) { setMenu(false); btn.focus(); } });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    window.addEventListener("resize", function () { if (window.innerWidth > 1100 && !menu.hidden) setMenu(false); });
  }

  // reveal on scroll
  var items = $$(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + "ms";
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // number inputs: format with thousands separators as you type
  $$("input[inputmode=numeric]").forEach(function (inp) {
    inp.addEventListener("input", function () {
      var n = String(inp.value).replace(/[^\d]/g, "");
      inp.value = n ? Number(n).toLocaleString("en-GB") : "";
    });
  });

  // ---------------------------------------------------------- fee estimator
  var est = $("[data-estimator]");
  if (est) {
    var boxes = $$("input[name=svc]", est);
    var total = $("[data-est-total]", est), year = $("[data-est-year]", est), label = $("[data-est-label]", est);
    var link = $("[data-est-link]", est);
    var update = function () {
      var picked = boxes.filter(function (b) { return b.checked; });
      var sum = picked.reduce(function (s, b) { return s + Number(b.value); }, 0);
      total.textContent = gbp(sum);
      year.innerHTML = sum ? "£" + gbp(sum * 12) + " " + T.perYear : "&nbsp;";
      label.textContent = picked.length ? T.approx + " · " + picked.length + " " + T.services : T.pickOne;
      var keys = picked.map(function (b) { return b.dataset.key; });
      link.href = "contact.html" + (keys.length ? "?s=" + keys.join(",") : "") + "#quote";
    };
    boxes.forEach(function (b) { b.addEventListener("change", update); });
    update();
  }

  // ---------------------------------------------------------- MTD checker
  var mtd = $("[data-mtd]");
  if (mtd) {
    var mIn = $("input", mtd), mTitle = $("[data-mtd-title]", mtd), mText = $("[data-mtd-text]", mtd);
    var mUpdate = function () {
      var v = num(mIn.value);
      if (!mIn.value) { mTitle.textContent = T.mtd.empty; mText.textContent = ""; return; }
      var k = v > 50000 ? "in26" : v > 30000 ? "in27" : v > 20000 ? "in28" : "out";
      mTitle.textContent = T.mtd[k][0];
      mText.textContent = T.mtd[k][1];
    };
    mIn.addEventListener("input", mUpdate);
  }

  // ---------------------------------------------------------- Stamp Duty (England & NI, residential, from 1 April 2025)
  var sd = $("[data-sdlt]");
  if (sd) {
    var STD = [[125000, 0], [250000, 0.02], [925000, 0.05], [1500000, 0.10], [Infinity, 0.12]];
    var FTB = [[300000, 0], [500000, 0.05]];
    var pIn = $("#sdlt-price"), out = $("[data-sdlt-total]", sd), eff = $("[data-sdlt-eff]", sd);
    var table = $("[data-sdlt-table]", sd), note = $("[data-sdlt-note]", sd);
    var calc = function () {
      var price = num(pIn.value);
      var buyer = ($("input[name=buyer]:checked", sd) || {}).value;
      var nonres = $("input[name=nonres]", sd).checked;
      var bands = STD, extra = 0, msg = "";
      if (buyer === "ftb") { if (price <= 500000) bands = FTB; else msg = T.sdlt.ftbOver; }
      if (buyer === "add" && price >= 40000) extra += 0.05;
      if (nonres) extra += 0.02;
      var prev = 0, totalTax = 0, rows = "";
      for (var i = 0; i < bands.length && price > prev; i++) {
        var top = bands[i][0], rate = bands[i][1] + extra;
        var slice = Math.min(price, top) - prev;
        var tax = slice * rate;
        totalTax += tax;
        var name = top === Infinity ? T.sdlt.above + " £" + gbp(prev) : "£" + gbp(prev) + " – £" + gbp(top);
        rows += "<tr><td>" + name + "</td><td>" + (Math.round(rate * 1000) / 10) + "%</td><td>£" + gbp(Math.floor(tax)) + "</td></tr>";
        prev = top;
      }
      totalTax = Math.floor(totalTax);
      out.textContent = "£" + gbp(totalTax);
      eff.textContent = price ? T.sdlt.eff + ": " + (totalTax / price * 100).toFixed(2) + "%" : "";
      table.hidden = !price;
      table.innerHTML = price ? "<thead><tr><th>" + T.sdlt.band + "</th><th>" + T.sdlt.rate + "</th><th>" + T.sdlt.tax + "</th></tr></thead><tbody>" + rows + "</tbody>" : "";
      note.textContent = msg;
    };
    pIn.addEventListener("input", calc);
    $$("input[name=buyer], input[name=nonres]", sd).forEach(function (i) { i.addEventListener("change", calc); });
    calc();
  }

  // ---------------------------------------------------------- quote form → WhatsApp or email
  var form = $("[data-quote]");
  if (form) {
    var F = T.form, err = $("[data-form-error]", form), via = "wa";
    // services ticked in the fee estimator arrive as ?s=… and are noted in the message
    var pre = (location.search.match(/[?&]s=([^&]+)/) || [])[1];
    if (pre) {
      var map = { sa: "Self Assessment", landlord: "Landlord tax", company: "Company accounts & tax", books: "Bookkeeping", vat: "VAT", paye: "Payroll" };
      var list = decodeURIComponent(pre).split(",").map(function (k) { return map[k]; }).filter(Boolean);
      if (list.length) form.msg.value = list.join(", ") + "\n";
      if (/vat/.test(pre)) $("input[name=vat][value=yes]", form).checked = true;
      if (/paye/.test(pre)) $("input[name=payroll][value=yes]", form).checked = true;
      if (/books/.test(pre)) $("input[name=books][value=yes]", form).checked = true;
    }
    $$("button[type=submit]", form).forEach(function (b) { b.addEventListener("click", function () { via = b.value; }); });
    form.addEventListener("input", function (e) { var f = e.target.closest(".field"); if (f) f.classList.remove("invalid"); });
    form.addEventListener("change", function (e) { var f = e.target.closest(".field"); if (f) f.classList.remove("invalid"); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var bad = [];
      $$("[required]", form).forEach(function (el) {
        if (el.type === "radio") {
          if (!$("input[name=" + el.name + "]:checked", form)) bad.push(el.closest(".field"));
        } else if (!el.value.trim() || (el.type === "email" && !/^\S+@\S+\.\S+$/.test(el.value))) {
          bad.push(el.closest(".field"));
        }
      });
      $$(".field", form).forEach(function (f) { f.classList.toggle("invalid", bad.indexOf(f) > -1); });
      if (bad.length) {
        err.textContent = F.missing; err.hidden = false;
        var first = $("input, select, textarea", bad[0]); if (first) first.focus();
        return;
      }
      err.hidden = true;
      var val = function (n) { var c = $("input[name=" + n + "]:checked", form); return c ? c.parentNode.textContent.trim() : "–"; };
      var lines = [
        F.hello, "",
        F.name + ": " + form.first.value.trim() + " " + form.last.value.trim(),
        F.email + ": " + form.email.value.trim(),
        F.phone + ": " + form.phone.value.trim(),
        F.type + ": " + form.type.value,
        F.turnover + ": £" + form.turnover.value.trim(),
        F.vat + ": " + val("vat"),
        F.payroll + ": " + val("payroll"),
        F.books + ": " + val("books"),
        F.lang + ": " + val("pref")
      ];
      if (form.msg.value.trim()) lines.push("", F.msg + ": " + form.msg.value.trim());
      var text = lines.join("\n");
      if (via === "mail") {
        location.href = "mailto:info@iqtiaccountants.co.uk?subject=" + encodeURIComponent(F.subject + " – " + form.first.value.trim() + " " + form.last.value.trim()) + "&body=" + encodeURIComponent(text);
      } else {
        window.open("https://wa.me/447305084561?text=" + encodeURIComponent(text), "_blank", "noopener");
      }
    });
  }
})();
