const burger = document.getElementById("burger");
const navLinks = document.getElementById("navLinks");
const themeToggle = document.getElementById("themeToggle");
const links = document.querySelectorAll(".nav-links li a");

burger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("light-theme");
  const isLightTheme = document.body.classList.contains("light-theme");
  themeToggle.setAttribute("aria-label", isLightTheme ? "Activer le thème sombre" : "Activer le thème clair");
});

links.forEach(link => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("active");
  });
});

const reveals = document.querySelectorAll(".reveal");

const revealOnScroll = () => {
  const windowHeight = window.innerHeight;
  reveals.forEach(el => {
    const elementTop = el.getBoundingClientRect().top;
    if (elementTop < windowHeight - 100) {
      el.classList.add("active");
     }
  });
};

window.addEventListener("scroll", revealOnScroll);
window.addEventListener("load", revealOnScroll);