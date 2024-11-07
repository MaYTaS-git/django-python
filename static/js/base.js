document.addEventListener("DOMContentLoaded", function () {
    const closeButtons = document.querySelectorAll(".close-btn");
    closeButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        const alertBox = this.parentElement;
        alertBox.classList.add("hidden");
      });
    });
  });
  