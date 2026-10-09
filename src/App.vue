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
      <h2>Mes compétences</h2>

      <div class="skills-tabs">
        <button 
          v-for="category in skillCategories" 
          :key="category.title"
          :class="['skill-tab', { active: activeSkillCategory === category.title }]"
          @click="activeSkillCategory = category.title"
        >
          {{ category.title }}
        </button>
      </div>

      <div class="skills-grid">
        <div
          v-for="skill in currentSkills"
          :key="skill.name + Math.random()"
          class="skill-card"
        >
          <img :src="'/' + skill.img" :alt="skill.name + ' Logo'" class="skill-icon">
          <span>{{ skill.name }}</span>
        </div>
      </div>
    </section>

    <!-- Projets -->
    <section id="projects" class="reveal">
      <h2>Mes projets</h2>
      <div class="projects">
        <a
          v-for="project in projects"
          :key="project.title"
          :href="project.url"
          target="_blank"
          class="project-card"
        >
          <img :src="'/' + project.image" :alt="project.title" class="project-img">
          <div 
            class="project-btn" 
            :style="{ '--grad-start': project.gradient[0], '--grad-end': project.gradient[1] }"
          >
            {{ project.label }}
          </div>
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
import { ref, onMounted, onUnmounted, watch, computed } from 'vue';

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

const activeSkillCategory = ref('Front-end');

const skillCategories = [
  { 
    title: 'Front-end', 
    skills: [
      { name: 'HTML', img: 'img/html.svg' },
      { name: 'CSS', img: 'img/css.svg' },
      { name: 'JavaScript', img: 'img/javascript.svg' },
      { name: 'XAML', img: 'img/vuejs.svg' },
      { name: 'React', img: 'img/react.svg' },
      { name: 'VueJS', img: 'img/vuejs.svg' },
      { name: 'Twig', img: 'img/twig.svg' },
      { name: 'Tailwind CSS', img: 'img/tailwind css.svg' },
    ]
  },
  { 
    title: 'Back-end', 
    skills: [
      { name: 'Python', img: 'img/reseau.png' },
      { name: 'C++', img: 'img/reseau.png' },
      { name: 'C#', img: 'img/reseau.png' },
      { name: 'PhP', img: 'img/reseau.png' },
      { name: 'Symfony', img: 'img/vuejs.svg' },
      { name: 'TypeScript', img: 'img/reseau.png' }
    ]
  },
  { 
    title: 'Base de donnée', 
    skills: [
      { name: 'SQL', img: 'img/reseau.png' },
      { name: 'NoSQL', img: 'img/reseau.png' },
    ]
  },
  { 
    title: 'Soft-skills', 
    skills: [
      { name: 'Anglais - Maîtrise', img: 'img/reseau.png' },
      { name: 'Espagnol - Notions', img: 'img/reseau.png' },
      { name: 'Travail d’équipe', img: 'img/reseau.png' },
      { name: 'Communication', img: 'img/reseau.png' },
      { name: 'Qualité de code', img: 'img/reseau.png' },
      { name: 'Persévérance', img: 'img/reseau.png' },
      { name: 'Gestion du stress', img: 'img/reseau.png' },
      { name: 'Soif d\'apprendre', img: 'img/reseau.png' }
    ]
  },

  { 
    title: 'Logiciels', 
    skills: [
      { name: 'Visual Studio Code', img: 'img/reseau.png' },
      { name: 'Figma', img: 'img/reseau.png' },
      { name: 'IntelliJ', img: 'img/reseau.png' },
      { name: 'Rider', img: 'img/reseau.png' },
      { name: 'IntelliJ', img: 'img/reseau.png' },
      { name: 'Android Studio', img: 'img/reseau.png' },
      { name: 'Docker', img: 'img/reseau.png' },
      { name: 'VPS', img: 'img/reseau.png' },
      { name: 'Git', img: 'img/reseau.png' }
    ]
  }
];

const currentSkills = computed(() => {
  const category = skillCategories.find(c => c.title === activeSkillCategory.value);
  return category ? category.skills : [];
});

const projects = [
  { title: 'Conscientia', label: 'Découvrir conscientia →', image: 'img/card_conscientia.svg', url: '#', gradient: ['#4B5ABE', '#26328D'] },
  { title: 'LowSens', label: 'Découvrir LowSens →', image: 'img/card_lowsens.svg', url: 'https://github.com/0Shin6/Team-sens', gradient: ['#8318FE', '#5100AE'] },
  { title: 'Appogix', label: 'Découvrir Appogix →', image: 'img/card_appogix.svg', url: '#', gradient: ['#B8860B', '#DAA520'] },
  { title: 'Uniliste', label: 'Découvrir Uniliste →', image: 'img/card_uniliste.svg', url: 'https://github.com/0Shin6/soundPulse', gradient: ['#FF0000', '#8B0000'] },
  { title: 'Flame', label: 'Découvrir Flame →', image: 'img/card_flame.svg', url: 'https://github.com/0Shin6/Flame.git²N', gradient: ['#B736FD', '#8203C6'] },
  { title: 'USSD', label: 'Découvrir USSD →', image: 'img/card_ussd.svg', url: '#', gradient: ['#8B0000', '#550000'] }
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
