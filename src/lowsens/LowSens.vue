<template>
  <div class="ls-page">
    <!-- Navbar -->
    <nav class="ls-navbar">
      <div class="ls-nav-pill">
        <img :src="logo" alt="Logo LowSens" class="ls-nav-logo" />
        <ul class="ls-nav-links" :class="{ open: menuOpen }">
          <li v-for="link in navLinks" :key="link.href">
            <a :href="link.href" @click.prevent="scrollTo(link.href)">{{ link.label }}</a>
          </li>
        </ul>
        <a href="#/" class="ls-btn ls-btn-small">Retour <span>→</span></a>
        <button class="ls-burger" type="button" aria-label="Menu" @click="menuOpen = !menuOpen">&#9776;</button>
      </div>
      <button
        class="ls-theme-toggle"
        type="button"
        :aria-label="isLightTheme ? 'Activer le thème sombre' : 'Activer le thème clair'"
        @click="isLightTheme = !isLightTheme"
      >&#9788;</button>
    </nav>

    <!-- Titre -->
    <h1 class="ls-title">Projet LowSens</h1>

    <!-- Bannière -->
    <div class="ls-banner">
      <img :src="banniere" alt="LowSens : la team Esport de tout les espoirs" />
    </div>

    <!-- Technologies -->
    <div class="ls-stack">
      <img :src="competences" alt="HTML, CSS, JavaScript, Python, SQLite, Git, VSCode" />
    </div>

    <!-- Présentation -->
    <section id="ls-presentation" class="ls-section">
      <h2 class="ls-h2">Présentation du projet</h2>
      <p class="ls-text">
        Dans le cadre du développement et de la professionnalisation d’une structure esport amatrice en pleine
        expansion, ce projet a pour but de construire une identité numérique forte à la suite d’une fusion. La version
        initiale du site ne répondant plus aux nouveaux enjeux de l’organisation, j’ai pris en charge la refonte
        complète du design afin d’en faire un véritable hub communautaire et informatif. Conçu pour valoriser
        l’écosystème du club auprès des fans, des compétiteurs et de futurs partenaires, le site centralise l’ensemble
        des contenus importants tel que le fil d’actualités, le calendrier des matchs à venir, ceux des derniers
        résultats et de la mise en valeur des différents rosters. Cette initiative a permis d’harmoniser l’image de
        marque de la nouvelle structure tout en offrant une expérience utilisateur fluide et adaptée aux exigences des
        dirigeants.
      </p>
    </section>

    <!-- Réalisation -->
    <section id="ls-realisation" class="ls-section">
      <h2 class="ls-h2">Comment je l’ai réalisé ?</h2>

      <span class="ls-badge">
        <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">
          <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2" />
          <path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
        </svg>
        En cours
      </span>

      <ol class="ls-timeline">
        <li v-for="(step, i) in steps" :key="i" class="ls-step">
          <span class="ls-step-num">{{ i + 1 }}</span>
          <div class="ls-step-body">
            <h3>{{ step.title }}</h3>
            <p>{{ step.subtitle }}</p>
          </div>
          <div v-if="step.image" class="ls-step-img">
            <img :src="step.image" :alt="step.title" />
          </div>
          <div v-else-if="step.placeholder" class="ls-step-placeholder">
            <strong>ILLUSTRATION</strong>
            <span>{{ step.placeholder }}</span>
          </div>
        </li>
      </ol>
    </section>

    <!-- Résultat -->
    <section id="ls-resultat" class="ls-section">
      <h2 class="ls-h2">Résultat de mon travail</h2>
      <p class="ls-text ls-text-large">
        Premier projet personnel mené pour de vrais clients, cette expérience m’a permis de travailler sur
        l’intégralité du cycle de développement du site, du recueil des besoins jusqu’au déploiement. Face aux enjeux
        d’ergonomie, j’ai développé mes compétences en UX/UI design pour livrer une interface intuitive et soignée,
        faisant de cette réalisation une réelle réussite formatrice dont je suis très fier.
      </p>
      <div class="ls-center">
        <a :href="siteUrl" target="_blank" rel="noopener noreferrer" class="ls-btn">Consulter le site <span>→</span></a>
      </div>
    </section>

    <!-- Liens utiles -->
    <section id="ls-liens" class="ls-section">
      <h2 class="ls-h2">Liens utiles du projet</h2>
      <div class="ls-links">
        <div class="ls-link-item">
          <span>Dépôt GitHub :</span>
          <a :href="repoUrl" target="_blank" rel="noopener noreferrer" class="ls-btn ls-btn-large">
            Consulter le dépôt <span>→</span>
          </a>
        </div>
        <div class="ls-link-item">
          <span>Documentation :</span>
          <a :href="docUrl" target="_blank" rel="noopener noreferrer" class="ls-btn ls-btn-large">
            Consulter la documentation <span>→</span>
          </a>
        </div>
      </div>
    </section>

    <footer class="ls-footer">
      <p>&copy; Granier Mathis - 2026</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import banniere from './img/banniere.svg';
import competences from './img/competences.svg';
import logo from './img/logo.svg';

const isLightTheme = ref(document.body.classList.contains('light-theme'));
const menuOpen = ref(false);

watch(isLightTheme, (val) => {
  document.body.classList.toggle('light-theme', val);
});

// Liens externes (à compléter)
const siteUrl = '#';
const repoUrl = 'https://github.com/0Shin6/Team-sens';
const docUrl = '#';

const navLinks = [
  { href: '#ls-presentation', label: 'Présentation' },
  { href: '#ls-realisation', label: 'Réalisation' },
  { href: '#ls-resultat', label: 'Résultat' },
  { href: '#ls-liens', label: 'Liens utiles' }
];

// `image` : chemin d'une illustration (null => placeholder, ou rien si placeholder est null)
const steps = [
  { title: 'Définition de l’identité visuelle', subtitle: 'Figma — inspiration logo + maillot', image: null, placeholder: 'logo figma' },
  { title: 'Recueil des besoins & validation', subtitle: 'Maquette — image : téléphone', image: null, placeholder: 'téléphone' },
  { title: 'Développement des vues', subtitle: 'HTML — image : html', image: null, placeholder: 'html' },
  { title: 'Bot Discord & back-end', subtitle: 'Création du bot et du back-end', image: null, placeholder: 'bot + back' },
  { title: 'Tests utilisateur (validé)', subtitle: 'Ancien site — image : page d’accueil', image: null, placeholder: 'ancien site' },
  { title: 'Redesign du site', subtitle: 'Contexte de fusion — nouvelles visions', image: null, placeholder: 'logo figma' },
  { title: 'Validation de la maquette', subtitle: 'Pas d’image', image: null, placeholder: null },
  { title: 'Redesign du site', subtitle: 'Site actuel — image : page du site', image: null, placeholder: 'site actuel' },
  { title: 'Validations & tests utilisateur', subtitle: 'Pas d’image', image: null, placeholder: null }
];

const scrollTo = (hash) => {
  menuOpen.value = false;
  document.querySelector(hash)?.scrollIntoView({ behavior: 'smooth' });
};

onMounted(() => window.scrollTo(0, 0));
</script>

<style scoped>
.ls-page {
  --ls-bg: #160d22;
  --ls-grad: linear-gradient(90deg, #c69bff, #8a3ffc, #c69bff);
  width: 100%;
  max-width: 1440px;
  margin: 0 auto;
  padding: 94px 0 78px;
  color: #ffffff;
  font-family: inherit;
}

:global(body:has(.ls-page)) {
  background: #160d22;
}
:global(body.light-theme:has(.ls-page)) {
  background: #f6e7ff;
}
:global(body.light-theme) .ls-page {
  --ls-bg: #f6e7ff;
  color: #160d22;
}

/* Navbar */
.ls-navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px 24px 14px;
}
.ls-nav-pill {
  display: flex;
  align-items: center;
  gap: 40px;
  padding: 6px 6px 6px 18px;
  min-height: 50px;
  background: rgba(16, 0, 44, 0.75);
  border-radius: 999px;
  backdrop-filter: blur(10px);
}
.ls-nav-logo {
  width: 32px;
  height: 32px;
}
.ls-nav-links {
  display: flex;
  gap: 50px;
  list-style: none;
  margin: 0;
  padding: 0;
}
.ls-nav-links a {
  color: #ffffff;
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  transition: color 0.2s;
}
.ls-nav-links a:hover {
  color: #c69bff;
}
.ls-burger {
  display: none;
  background: none;
  border: 0;
  color: #fff;
  font-size: 22px;
  cursor: pointer;
}
.ls-theme-toggle {
  position: absolute;
  right: 70px;
  width: 50px;
  height: 50px;
  border: 0;
  border-radius: 50%;
  background: rgba(16, 0, 44, 0.6);
  color: #faf0f0;
  font-size: 30px;
  line-height: 1;
  cursor: pointer;
  backdrop-filter: blur(15px);
}

/* Boutons */
.ls-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 45px;
  padding: 0 22px;
  border-radius: 999px;
  background: var(--ls-grad);
  background-size: 200% auto;
  background-position: left center;
  color: #100029;
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
  white-space: nowrap;
  transition: background-position 0.4s ease;
}
.ls-btn:hover {
  background-position: right center;
}
.ls-btn-small {
  min-height: 38px;
  padding: 0 18px;
  font-size: 14px;
}
.ls-btn-large {
  min-height: 45px;
  padding: 0 22px;
  font-size: 14px;
}

/* Titre + bannière */
.ls-title {
  margin: 34px 0 30px;
  text-align: center;
  font-size: 54px;
  font-weight: 700;
  text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.ls-banner img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 20px;
}
.ls-stack {
  display: flex;
  justify-content: center;
  margin: 70px 0 60px;
  padding: 0 16px;
}
.ls-stack img {
  width: 100%;
  max-width: 886px;
  height: auto;
}

/* Sections */
.ls-section {
  width: 100%;
  max-width: none;
  margin: 0 0 90px;
  padding: 0 48px;
}
.ls-h2 {
  margin: 0 0 30px;
  padding: 0;
  border: 0;
  font-size: 24px;
  font-weight: 700;
  text-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
}
.ls-text {
  margin: 0;
  padding: 0 0 0 60px;
  font-size: 16px;
  line-height: 1.5;
}
.ls-text-large {
  padding: 0 100px;
  font-size: 16px;
}
.ls-center {
  display: flex;
  justify-content: center;
  margin-top: 40px;
}

/* Badge */
.ls-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin: 0 0 30px 30px;
  padding: 6px 14px;
  border-radius: 999px;
  background: #2a1745;
  color: #e6d4ff;
  font-size: 14px;
  font-weight: 600;
}
.ls-badge svg {
  color: #c69bff;
}

/* Timeline */
.ls-timeline {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0 0 0 100px;
}
.ls-timeline::before {
  content: '';
  position: absolute;
  left: 129px;
  top: 15px;
  bottom: 15px;
  width: 2px;
  background: linear-gradient(to bottom, #8a3ffc, #5a2a9a);
}
.ls-step {
  position: relative;
  display: flex;
  align-items: center;
  gap: 30px;
  min-height: 120px;
}
.ls-step-num {
  position: relative;
  z-index: 1;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  margin-left: 14px;
  border-radius: 50%;
  background: linear-gradient(135deg, #c69bff, #8a3ffc);
  color: #100029;
  font-weight: 700;
  font-size: 16px;
  box-shadow: 0 0 0 6px var(--ls-bg);
}
.ls-step-body {
  flex: 1;
  min-width: 0;
}
.ls-step-body h3 {
  margin: 0 0 6px;
  font-size: 19px;
  font-weight: 700;
}
.ls-step-body p {
  margin: 0;
  font-size: 15px;
  opacity: 0.8;
}
.ls-step-img img {
  display: block;
  max-width: 260px;
  max-height: 100px;
  border-radius: 12px;
}
.ls-step-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 92px;
  height: 52px;
  margin-right: 60px;
  border-radius: 10px;
  background: #241536;
  font-size: 10px;
  text-align: center;
  color: #d9c6f5;
}
.ls-step-placeholder strong {
  font-size: 11px;
  letter-spacing: 0.5px;
}

/* Liens utiles */
.ls-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 30px;
}
.ls-link-item {
  display: flex;
  align-items: center;
  gap: 24px;
  font-size: 16px;
  font-weight: 600;
}

.ls-footer {
  text-align: center;
  color: #c9b3e8;
  margin: 0;
  padding: 16px;
}

/* Responsive */
@media (max-width: 1100px) {
  .ls-nav-links,
  .ls-nav-pill {
    gap: 24px;
  }
  .ls-theme-toggle {
    right: 16px;
  }
}

@media (max-width: 800px) {
  .ls-navbar {
    padding: 14px 16px 10px;
  }
  .ls-burger {
    display: block;
  }
  .ls-nav-links {
    display: none;
    position: absolute;
    top: 72px;
    left: 50%;
    transform: translateX(-50%);
    flex-direction: column;
    gap: 16px;
    padding: 20px 32px;
    border-radius: 20px;
    background: rgba(16, 0, 44, 0.95);
  }
  .ls-nav-links.open {
    display: flex;
  }
  .ls-title {
    font-size: 38px;
  }
  .ls-section {
    padding: 0 16px;
    margin-bottom: 60px;
  }
  .ls-h2 {
    font-size: 24px;
  }
  .ls-text,
  .ls-text-large {
    padding: 0;
    font-size: 15px;
  }
  .ls-timeline {
    padding-left: 0;
  }
  .ls-timeline::before {
    left: 29px;
  }
  .ls-step {
    gap: 16px;
    min-height: 90px;
  }
  .ls-step-placeholder {
    margin-right: 0;
  }
  .ls-link-item {
    flex-direction: column;
    gap: 12px;
  }
}
</style>
