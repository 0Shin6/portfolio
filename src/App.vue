<template>
  <div :class="{ 'light-theme': isLightTheme }">
    <!-- Navbar -->
    <nav class="navbar">
      <ul class="nav-links" :class="{ active: menuOpen }" id="navLinks">
        <li v-for="link in navLinks" :key="link.href">
          <a :href="link.href" @click="closeMenu">{{ link.label }}</a>
        </li>
      </ul>
      <button
        class="theme-toggle"
        type="button"
        :aria-label="isLightTheme ? 'Activer le thème sombre' : 'Activer le thème clair'"
        @click="toggleTheme"
      >&#9788;</button>
      <div class="burger" @click="toggleMenu">&#9776;</div>
    </nav>

    <!-- Header -->
    <header class="reveal active">
      <h1>Bienvenue sur mon portfolio</h1>
    </header>

    <!-- À propos -->
    <section id="about" class="reveal">
      <h2>Je me présente</h2>
      <div class="about-content">
        <div class="about-text">
          <p v-for="para in aboutParagraphs" :key="para">{{ para }}</p>
        </div>
        <img class="about-image" src="/img/pdp.jpg" alt="Photo de Mathis GRANIER">
      </div>
    </section>

    <!-- Parcours -->
    <section id="parcours" class="reveal">
      <h2>Mon parcours</h2>
      <div class="experience-list">
        <article
          v-for="exp in experiences"
          :key="exp.company"
          class="experience-item"
        >
          <div class="experience-date">{{ exp.date }}</div>
          <div class="experience-main">
            <p class="experience-company">{{ exp.company }}</p>
            <p class="experience-role">{{ exp.role }}</p>
            <p v-if="exp.detail" class="experience-detail">{{ exp.detail }}</p>
          </div>
          <img
            class="experience-logo"
            :class="exp.logoClass"
            :src="'/' + exp.logo"
            :alt="'Logo ' + exp.company"
          >
          <a :href="exp.link" class="experience-link">
            {{ exp.linkLabel }} <span>→</span>
          </a>
        </article>
      </div>
    </section>

    <!-- Compétences -->
    <section id="skills" class="reveal">
      <h2>Compétences</h2>

      <template v-for="category in skillCategories" :key="category.title">
        <h3>{{ category.title }}</h3>
        <div class="skills-row">
          <div
            v-for="skill in category.skills"
            :key="skill.name"
            class="skill"
          >
            <img :src="'/' + skill.img" :alt="skill.name + ' Logo'">
            <span>{{ skill.name }}</span>
          </div>
        </div>
      </template>

      <h3>Soft-skills</h3>
      <div class="skill-row">
        <div
          v-for="soft in softSkills"
          :key="soft"
          class="soft-skill"
        >
          <span>{{ soft }}</span>
        </div>
      </div>
    </section>

    <!-- Projets -->
    <section id="projects" class="reveal">
      <h2>Mes Projets</h2>
      <div class="projects">
        <a
          v-for="project in projects"
          :key="project.title"
          :href="project.url"
          target="_blank"
          class="project"
        >
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <p class="project-skills">{{ project.skills }}</p>
        </a>
      </div>
    </section>

    <!-- Contact + CV -->
    <section class="bottom-section reveal">
      <div id="contact">
        <h2>Me contacter</h2>
        <div class="contact-list">
          <a
            v-for="contact in contacts"
            :key="contact.label"
            :href="contact.url"
            target="_blank"
          >
            <img :src="'/' + contact.img" :alt="'Logo ' + contact.label">
            <span>{{ contact.label }}</span>
          </a>
        </div>
      </div>

      <a href="/doc/CV_GRANIER_Mathis.pdf" class="cv-box" target="_blank" download>
        <div class="cv-content">
          <h3>Télécharger mon CV</h3>
          <p>Format PDF</p>
        </div>
      </a>
    </section>

    <footer>
      <p>&copy; Granier Mathis - 2026</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';

// État réactif
const isLightTheme = ref(false);
const menuOpen = ref(false);

// Appliquer la classe sur le body pour garder le style initial si nécessaire
watch(isLightTheme, (newVal) => {
  if (newVal) {
    document.body.classList.add('light-theme');
  } else {
    document.body.classList.remove('light-theme');
  }
});

// Données
const navLinks = [
  { href: '#about', label: 'Qui suis-je ?' },
  { href: '#parcours', label: 'Parcours' },
  { href: '#skills', label: 'Compétences' },
  { href: '#projects', label: 'Projets' },
  { href: '#contact', label: 'Contact' }
];

const aboutParagraphs = [
  "Étudiant en 3ᵉ année de BUT Informatique, j'ai une réelle curiosité technique pour la conception d'outils numériques à la fois fiables, accessibles et performants. Mon approche repose sur une démarche de comprendre le fonctionnement interne des technologies pour créer des solutions utiles qui répondent à de véritables besoins.",
  "Polyvalent, j'interviens sur l'ensemble du cycle de développement, du front-end au back-end, jusqu'à l'administration système et réseau. Qu'il s'agisse de concevoir et déployer des sites web ou de déployer des logiciels conteneurisés avec Docker, j'aime mener des projets de bout en bout en veillant à la cohérence de l'architecture du projet.",
  "En parallèle du code, je fais beaucoup de sport notamment le cyclisme, la course à pied et la musculation. La musique occupent une grande importance dans mon quotidien. Ces activités contribuent directement à mon équilibre physique et mental, tout en développant une rigueur et une endurance que je réinvestis naturellement dans chacun de mes projets."
];

const experiences = [
  { date: 'Avril - Juin 2026', company: 'Conscentia', role: 'Stage – Développeur Web & mobile', logoClass: 'logo-owl', logo: 'img/conscientia.png', link: '#', linkLabel: 'Découvrir Conscentia' },
  { date: '2024 -', company: 'IUT du Limousin', role: 'BUT informatique', logoClass: 'logo-iut', logo: 'img/iut.png', link: '#', linkLabel: 'Découvrir mes projets universitaires' },
  { date: '2021 - 2024', company: 'Lycée Max Linder', role: 'Baccalauréat Général', detail: 'Mathématique - NSI', logoClass: 'logo-lycee', logo: 'img/lycee.png', link: '#', linkLabel: 'Vous souhaitez me contacter ?' }
];

const skillCategories = [
  { title: 'Front-end', skills: [{ name: 'HTML', img: 'img/html.png' }, { name: 'CSS', img: 'img/css.png' }, { name: 'JavaScript', img: 'img/js.png' }] },
  { title: 'Back-end', skills: [{ name: 'Python', img: 'img/python.png' }, { name: 'Java', img: 'img/java.png' }, { name: 'Rust', img: 'img/rust.png' }, { name: 'C++', img: 'img/cpp.png' }] },
  { title: 'Réseaux', skills: [{ name: 'DHCP - DNS - Routage - SSH - FTP - iptables - IPv4', img: 'img/reseau.png' }] },
  { title: 'Langues', skills: [{ name: 'Anglais - Avancé', img: 'img/uk.png' }, { name: 'Espagnol - Notions', img: 'img/spain.png' }] },
  { title: 'Logiciels', skills: [{ name: 'VSCode', img: 'img/VSC.png' }, { name: 'Eclipse IDE', img: 'img/eclipse.png' }, { name: 'IntelliJ IDEA', img: 'img/intellij.png' }, { name: 'Android Studio', img: 'img/android-studio.png' }, { name: 'Figma', img: 'img/Figma.png' }, { name: 'Terminal', img: 'img/terminal.png' }, { name: 'Docker', img: 'img/Docker.png' }] },
  { title: 'Frameworks', skills: [{ name: 'Kathara', img: 'img/kathara.png' }, { name: 'VueJS', img: 'img/Vue.png' }] },
  { title: 'Base de données', skills: [{ name: 'mySQL', img: 'img/mySQL.png' }, { name: 'Mongo DB', img: 'img/mongodb.png' }, { name: 'SQLite', img: 'img/sqlite.png' }, { name: 'mariaDB', img: 'img/mariadb.png' }] }
];

const softSkills = ['Travail d’équipe', 'Soif d’apprendre', 'Force de proposition', 'Qualité de code', 'Gestion du stress', 'Rigueur', 'Communication', 'Résolution des problèmes', 'Autodidacte'];

const projects = [
  { title: 'RobyBot', description: 'Bot Discord en python avec une base de donnée sqlite pour le serveur Robynet', skills: 'Python, Discord API, SQLite, Resolution de problèmes, soif d\'apprendre, VScode', url: 'https://github.com/0Shin6/roleby.git' },
  { title: 'Team Sens', description: 'Site officiel en HTML, CSS et JS + bot discord en python pour sa gestion avec une base de données sqlite', skills: 'HTML, CSS, JavaScript, Python, SQLite', url: 'https://github.com/0Shin6/Team-sens' },
  { title: 'Administration réseau', description: "Création et administration d'un réseau virtuel en IPv4 sur Katharà", skills: "Réseau, Katharà, Travail d'équipe, Rigueur, Terminal", url: 'https://github.com/0Shin6/S2.03.git' },
  { title: 'Mon Portfolio', description: 'Site web personnel En HTML, CSS et JS', skills: 'HTML, CSS, JavaScript, Autodidacte', url: 'https://github.com/0Shin6/portfolio.git' },
  { title: 'Uniliste', description: "Application web de gestion des absences à l'IUT en vueJS, Rust et MongoDB", skills: "VueJS, Rust, MongoDB,Travail d'équipe, Communication,soif d'apprendre, Figma, VScode", url: 'https://github.com/0Shin6/soundPulse' },
  { title: 'Flame', description: 'Application mobile de to-do list', skills: "Kotlin, Android Studio, Figma, Soif d'apprendre, Autodidacte", url: 'https://github.com/0Shin6/Flame.git²N' }
];

const contacts = [
  { label: '.shin60', url: 'https://discord.com/app/', img: 'img/discord.png' },
  { label: 'Mathis Granier', url: 'https://www.linkedin.com/in/mathis-granier-06a460360/', img: 'img/linkedin.png' },
  { label: 'mathis.granier@etu.unilim.fr', url: 'mailto:mathis.granier@etu.unilim.fr', img: 'img/mail.png' },
  { label: '0Shin6', url: 'https://github.com/0Shin6', img: 'img/github.png' }
];

// Méthodes
const toggleTheme = () => {
  isLightTheme.value = !isLightTheme.value;
};

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};

const closeMenu = () => {
  menuOpen.value = false;
};

const handleScroll = () => {
  const windowHeight = window.innerHeight;
  const reveals = document.querySelectorAll('.reveal');
  
  reveals.forEach(el => {
    const elementTop = el.getBoundingClientRect().top;
    if (elementTop < windowHeight - 100) {
      el.classList.add('active');
    }
  });
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
  handleScroll();
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>
