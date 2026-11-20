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
      <h1>Mathis Granier</h1>
      <h2 class="header-subtitle">Développeur Web Full-Stack</h2> 
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
          <img :src="'/' + skill.img" :alt="skill.name + ' Logo'" class="skill-icon" :style="skill.iconStyle">
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
    <section id="contact" class="reveal">
      <h2>Me contacter</h2>
      <div class="contact-container">
        <!-- Colonne gauche : Cartes de contact -->
        <div class="contact-cards-list">
          <div
            v-for="contact in contacts"
            :key="contact.type"
            class="contact-card"
          >
            <div class="contact-icon-box">
              <img :src="'/' + contact.img" :alt="contact.type" class="contact-icon" />
            </div>
            <div class="contact-info">
              <span class="contact-type">{{ contact.type }}</span>
              <span class="contact-value">{{ contact.value }}</span>
            </div>
            <a
              :href="contact.url"
              target="_blank"
              rel="noopener noreferrer"
              class="contact-btn"
            >
              {{ contact.btnText }}
            </a>
          </div>
        </div>

        <!-- Colonne droite : Preview CV + Téléchargement -->
        <div class="cv-card">
          <img src="/img/cv.svg" alt="Aperçu du CV" class="cv-img" />
          <a
            href="/doc/CV_Granier_Mathis.pdf"
            download="CV_Granier_Mathis.pdf"
            target="_blank"
            rel="noopener noreferrer"
            class="cv-btn"
          >
            Télécharger mon CV <span>&rarr;</span>
          </a>
        </div>
      </div>
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
  "Étudiant en 3ᵉ année de BUT Informatique, je conçois et déploie des applications web du design au déploiement. J'ai toujours été curieux de comprendre le fonctionnement interne des technologies, j'aime concevoir les interfaces, structurer des API et optimiser l'expérience utilisateur.",
  "Ayant un profil polyvalent, je travaille sur l'ensemble du cycle de développement allant de la création d'interfaces dynamiques au développement back-end, jusqu'à l'administration système et au déploiement du site via un VPS. En parallèle du code, je pratique régulièrement du sport d'endurance et de la musique m'apporte au quotidien rigueur, discipline et persévérance dans la réalisation de mes projets."
];

const experiences = [
  { date: 'Avril - Juin 2026', company: 'FinOwl AI', role: 'Stage – Développeur Web & mobile', logoClass: 'logo-owl', logo: 'img/conscientia.svg?v=2', link: '#', linkLabel: 'Découvrir Conscientia' },
  { date: '2024 -', company: 'IUT du Limousin', role: 'BUT informatique', logoClass: 'logo-iut', logo: 'img/iut.png', link: '#', linkLabel: 'Découvrir mes projets universitaires' },
  { date: '2021 - 2024', company: 'Lycée Max Linder', role: 'Baccalauréat Général', detail: 'Mathématique - NSI', logoClass: 'logo-lycee', logo: 'img/maxlinder.svg?v=2', link: '#', linkLabel: 'Vous souhaitez me contacter ?' }
];

const activeSkillCategory = ref('Front-end');

const skillCategories = [
  { 
    title: 'Front-end', 
    skills: [
      { name: 'HTML', img: 'img/html.svg' },
      { name: 'CSS', img: 'img/css.svg' },
      { name: 'JavaScript', img: 'img/js.svg' },
      { name: 'XAML', img: 'img/xaml.svg' },
      { name: 'React', img: 'img/react.svg' },
      { name: 'VueJS', img: 'img/vue.svg' },
      { name: 'Twig', img: 'img/twig.svg' },
      { name: 'Tailwind CSS', img: 'img/tailwind.svg' },
    ]
  },
  { 
    title: 'Back-end', 
    skills: [
      { name: 'Python', img: 'img/python.svg' },
      { name: 'C++', img: 'img/cpp.svg' },
      { name: 'C#', img: 'img/cs.svg' },
      { name: 'PhP', img: 'img/php.svg' },
      { name: 'Symfony', img: 'img/symfony.svg' },
      { name: 'TypeScript', img: 'img/ts.svg' }
    ]
  },
  { 
    title: 'Base de donnée', 
    skills: [
      { name: 'SQL', img: 'img/sql.svg' },
      { name: 'NoSQL', img: 'img/nosql.svg', iconStyle: 'transform: scale(2.5);' },
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
      { name: 'VS Code', img: 'img/vscode.svg' },
      { name: 'Figma', img: 'img/figma.svg' },
      { name: 'IntelliJ', img: 'img/intellij.svg' },
      { name: 'Rider', img: 'img/rider.svg' },
      { name: 'Android Studio', img: 'img/android_studio.svg' },
      { name: 'Docker', img: 'img/docker.svg' },
      { name: 'VPS', img: 'img/reseau.png' },
      { name: 'Git', img: 'img/git.svg' }
    ]
  }
];

const currentSkills = computed(() => {
  const category = skillCategories.find(c => c.title === activeSkillCategory.value);
  return category ? category.skills : [];
});

const projects = [
  { title: 'Conscientia', label: 'Découvrir conscientia →', image: 'img/card_conscientia.svg', url: '#', gradient: ['#4B5ABE', '#26328D'] },
  { title: 'LowSens', label: 'Découvrir LowSens →', image: 'img/card_lowsens.svg', url: '#/lowsens', gradient: ['#8318FE', '#5100AE'] },
  { title: 'Appogix', label: 'Découvrir Appogix →', image: 'img/card_appogix.svg', url: '#/appogix', gradient: ['#B8860B', '#DAA520'] },
  { title: 'Uniliste', label: 'Découvrir Uniliste →', image: 'img/card_uniliste.svg', url: 'https://github.com/0Shin6/soundPulse', gradient: ['#D43545', '#C70215'] },
  { title: 'Flame', label: 'Découvrir Flame →', image: 'img/card_flame.svg', url: 'https://github.com/0Shin6/Flame.git²N', gradient: ['#B736FD', '#8203C6'] },
  { title: 'USSD', label: 'Découvrir USSD →', image: 'img/card_ussd.svg', url: '#/ussd', gradient: ['#CB0101', '#880101'] }
];

const contacts = [
  { 
    type: 'Discord', 
    value: '.shin60', 
    btnText: 'Envoyer un message', 
    url: 'https://discord.com/app/', 
    img: 'img/discord.svg?v=2' 
  },
  { 
    type: 'Email', 
    value: 'mathis.granier.pro@gmail.com', 
    btnText: 'Envoyer un email', 
    url: 'mailto:mathis.granier.pro@gmail.com', 
    img: 'img/mail.svg' 
  },
  { 
    type: 'LinkedIn', 
    value: 'mathis.granier.pro@gmail.com', 
    btnText: 'Aller sur LinkedIn', 
    url: 'https://www.linkedin.com/in/mathis-granier-06a460360/', 
    img: 'img/linkedin.svg' 
  },
  { 
    type: 'GitHub', 
    value: '0Shin6', 
    btnText: 'Aller sur GitHub', 
    url: 'https://github.com/0Shin6', 
    img: 'img/github.svg' 
  }
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
