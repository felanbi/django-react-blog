document.getElementById("form-btn-submit").addEventListener("click", (e) => {
  var formOk = document.getElementById("form-ok");

  if (!formOk) return;

  formOk.classList.remove("visually-hidden");

  setTimeout(() => {
    formOk.style.opacity = 0;

    setTimeout(() => {
      formOk.classList.add("visually-hidden");
    }, 750);
  }, 5000);
});

document.addEventListener("DOMContentLoaded", () => {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});
