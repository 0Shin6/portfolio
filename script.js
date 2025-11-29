const burger = document.getElementById("burger");
const navLinks = document.getElementById("navLinks");
const links = document.querySelectorAll(".nav-links li a");

burger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
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