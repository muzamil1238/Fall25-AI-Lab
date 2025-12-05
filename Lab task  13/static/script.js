document.addEventListener("DOMContentLoaded", () => {
  const ratingSlider = document.getElementById("rating_value");
  const ratingDisplay = document.getElementById("rating_display");
  const form = document.getElementById("predictForm");
  const predictBtn = document.getElementById("predictBtn");


  ratingSlider.addEventListener("input", () => {
    ratingDisplay.textContent = ratingSlider.value;
  });

  form.addEventListener("submit", (e) => {
    const gender = document.getElementById("gender").value;
    const ratingCount = document.getElementById("rating_count").value;

    if (!gender || ratingCount <= 0) {
      e.preventDefault();
      alert("⚠️ Please fill out all fields correctly.");
      return;
    }

   
    predictBtn.innerHTML = "⏳ Predicting...";
    predictBtn.disabled = true;
    predictBtn.style.opacity = "0.7";
  });

  const resultBox = document.getElementById("resultBox");
  if (resultBox) {
    resultBox.style.opacity = 0;
    setTimeout(() => {
      resultBox.style.opacity = 1;
      resultBox.style.transition = "opacity 1s ease-in-out";
    }, 300);
  }
});
