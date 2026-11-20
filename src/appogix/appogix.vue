<template>
  <div class="ap-page">
    <!-- Navbar -->
    <nav class="ap-navbar" aria-label="Navigation du projet">
      <div class="ap-nav-pill">
        <img :src="logo" alt="Logo Appogix" class="ap-nav-logo" />
        <ul class="ap-nav-links" :class="{ open: menuOpen }">
          <li v-for="link in navLinks" :key="link.href">
            <a :href="link.href" @click.prevent="scrollTo(link.href)">{{ link.label }}</a>
          </li>
        </ul>
        <a href="#/" class="ap-btn ap-btn-small">Retour <span>→</span></a>
        <button class="ap-burger" type="button" aria-label="Menu" @click="menuOpen = !menuOpen">&#9776;</button>
      </div>
      <button
        class="ap-theme-toggle"
        type="button"
        :aria-label="isLightTheme ? 'Activer le thème sombre' : 'Activer le thème clair'"
        @click="isLightTheme = !isLightTheme"
      >&#9788;</button>
    </nav>

    <!-- Titre -->
    <h1 class="ap-title">Projet Appogix</h1>

    <!-- Bannière -->
    <div class="ap-banner">
      <img :src="banniere" alt="Appogix : Vos applications mobiles sont entre de bonnes mains" />
    </div>

    <!-- Technologies -->
    <div class="ap-stack">
      <img :src="competences" alt="HTML, CSS, JavaScript, Python, Git, VSCode, Figma" />
    </div>

    <!-- Présentation -->
    <section id="ap-presentation" class="ap-section">
      <h2 class="ap-h2">Présentation du projet</h2>
      <p class="ap-text">
        Dans le cadre de mon stage de deuxième année de BUT informatique, j’ai conçu et développé le site vitrine
        d’Appogix, une jeune société spécialisée dans le développement d’applications mobiles multiplateformes.
        L’objectif principal était d’établir rapidement une présence numérique crédible et professionnelle pour
        valoriser leur expertise technique auprès de potentiels clients. Ce site à l’architecture épurée s’articule
        autour d’une présentation des services de l’entreprise, complétée par une page dédiée mettant en avant une de
        leurs réalisations phares. J’ai également ajouter un système d’envoie d’email automatique sans passer par un
        service tiers ou par un lien mailto.
      </p>
    </section>

    <!-- Réalisation -->
    <section id="ap-realisation" class="ap-section">
      <h2 class="ap-h2">Comment je l’ai réalisé ?</h2>

      <span class="ap-badge">
        <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true">
          <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2" />
          <path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
        </svg>
        En cours
      </span>

      <ol class="ap-timeline">
        <li v-for="(step, i) in steps" :key="i" class="ap-step">
          <span class="ap-step-num">{{ i + 1 }}</span>
          <div class="ap-step-body">
            <h3>{{ step.title }}</h3>
            <p>{{ step.subtitle }}</p>
          </div>
          <div v-if="step.image" class="ap-step-img">
            <img :src="step.image" :alt="step.title" />
          </div>
          <div v-else-if="step.placeholder" class="ap-step-placeholder">
            <strong>ILLUSTRATION</strong>
            <span>{{ step.placeholder }}</span>
          </div>
        </li>
      </ol>
    </section>

    <!-- Résultats -->
    <section id="ap-resultat" class="ap-section ap-section-result">
      <h2 class="ap-h2">Résultats de ce projet</h2>
      <p class="ap-text ap-text-result">
        En ligne et opérationnel, le site web répond parfaitement aux attentes d’Appogix en matière de visibilité et de
        présentation de son savoir-faire. Bien que j’ai eu quelques difficultés avec la prise en main de la
        méthodologie de gestion de projet de l’entreprise ainsi que la définition d’une identité graphique, finalement
        résolue grâce à une base d’inspiration WordPress fournie par l’équipe, ont été des défis stimulants. Cette
        réalisation m’a permis de gagner en adaptabilité, j’ai pris un réel plaisir à mener ce développement à terme et
        je suis particulièrement fier du rendu final livré à l’entreprise.
      </p>
      <div class="ap-center">
        <a :href="siteUrl" target="_blank" rel="noopener noreferrer" class="ap-btn">
          Consulter le site <span>→</span>
        </a>
      </div>
    </section>

    <!-- Liens utiles -->
    <section id="ap-liens" class="ap-section ap-section-links">
      <h2 class="ap-h2">Liens utiles du projet</h2>
      <div class="ap-links">
        <div class="ap-link-item">
          <span>Rapport de stage :</span>
          <a :href="reportUrl" target="_blank" rel="noopener noreferrer" class="ap-btn">
            Consulter le rapport <span>→</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="ap-footer">
      <p>&copy; Granier Mathis - 2026</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue';
import banniere from './img/banniere.svg';
import competences from './img/competences.svg';
import logo from './img/logo.svg';

const isLightTheme = ref(document.body.classList.contains('light-theme'));
const menuOpen = ref(false);

watch(isLightTheme, (val) => {
  document.body.classList.toggle('light-theme', val);
});

// Lien vers la one-page dans src/appogix/site/
const siteUrl = new URL('./site/index.html', import.meta.url).href;
const reportUrl = '#';

const navLinks = [
  { href: '#ap-presentation', label: 'Présentation' },
  { href: '#ap-realisation', label: 'Réalisation' },
  { href: '#ap-resultat', label: 'Résultat' },
  { href: '#ap-liens', label: 'Liens utiles' }
];

const steps = [
  { title: 'Recueil des besoins', subtitle: 'Maquette — image : Personnes', image: null, placeholder: 'Personnes' },
  {
    title: 'Définition de l’identité visuelle & de la structure du site',
    subtitle: 'Maquette — image : Figma',
    image: null,
    placeholder: 'Figma'
  },
  { title: 'Préparation au développement', subtitle: 'Maquette — image : Git', image: null, placeholder: 'Figma' },
  {
    title: 'Développement section par section',
    subtitle: 'Maquette — image : picto HTML',
    image: null,
    placeholder: 'Figma'
  },
  {
    title: 'Développement d’une page projet',
    subtitle: 'Maquette — image : paysagix',
    image: null,
    placeholder: 'Figma'
  },
  {
    title: 'Validation client section par section',
    subtitle: 'Maquette — image : logo personne',
    image: null,
    placeholder: 'Figma'
  },
  { title: 'Tests utilisateur', subtitle: 'Maquette — image : Boîte à outils', image: null, placeholder: 'Figma' }
];

const scrollTo = (hash) => {
  menuOpen.value = false;
  document.querySelector(hash)?.scrollIntoView({ behavior: 'smooth' });
};

onMounted(() => {
  document.body.classList.add('ap-scrollbar');
  window.scrollTo(0, 0);
});

onUnmounted(() => {
  document.body.classList.remove('ap-scrollbar');
});
</script>

<style scoped>
.ap-page {
  --ap-bg: #151200;
  --ap-gold: #d2a951;
  --ap-gold-hover: #d9b061;
  --ap-gold-bright: #e0b220;
  width: 100%;
  max-width: 1440px;
  min-height: 100vh;
  margin: 0 auto;
  padding: 94px 0 80px;
  color: #faf0f0;
  font-family: inherit;
}

:global(body:has(.ap-page)) {
  background: #151200;
}
:global(body.light-theme:has(.ap-page)) {
  background: #fffaef;
}
:global(body.light-theme) .ap-page {
  --ap-bg: #fffaef;
  color: #1e1500;
}
:global(body.light-theme) .ap-nav-pill {
  background: rgba(255, 250, 239, 0.85);
  border-color: rgba(210, 169, 81, 0.35);
}
:global(body.light-theme) .ap-nav-links a,
:global(body.light-theme) .ap-burger,
:global(body.light-theme) .ap-title,
:global(body.light-theme) .ap-h2,
:global(body.light-theme) .ap-text,
:global(body.light-theme) .ap-step-body h3,
:global(body.light-theme) .ap-link-item {
  color: #1e1500;
}
:global(body.light-theme) .ap-step-body p {
  color: rgba(30, 21, 0, 0.72);
}
:global(body.light-theme) .ap-badge {
  background: #f5ebd1;
  color: #1e1500;
}
:global(body.light-theme) .ap-step-placeholder {
  background: #f5ebd1;
  border-color: rgba(210, 169, 81, 0.35);
  color: #5c4813;
}
:global(body.light-theme) .ap-step-placeholder strong {
  color: #1e1500;
}
:global(body.light-theme) .ap-footer {
  color: #8a6816;
}
:global(body.light-theme) .ap-theme-toggle {
  background: rgba(255, 250, 239, 0.85);
  border: 1px solid rgba(210, 169, 81, 0.35);
  color: #1e1500;
}
:global(body.ap-scrollbar::-webkit-scrollbar-track) {
  background: #1e1500;
}
:global(body.ap-scrollbar::-webkit-scrollbar-thumb) {
  background: #9a6a01;
  border-radius: 10px;
}
:global(body.ap-scrollbar::-webkit-scrollbar-thumb:hover) {
  background: #d2a951;
}

/* Navbar */
.ap-navbar {
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
.ap-nav-pill {
  display: flex;
  align-items: center;
  gap: 54px;
  padding: 8px 18px 8px 24px;
  min-height: 58px;
  background: rgba(42, 33, 4, 0.85);
  border: 1px solid rgba(210, 169, 81, 0.22);
  border-radius: 999px;
  backdrop-filter: blur(12px);
}
.ap-nav-logo {
  width: 34px;
  height: 40px;
  object-fit: contain;
}
.ap-nav-links {
  display: flex;
  gap: 56px;
  list-style: none;
  margin: 0;
  padding: 0;
}
.ap-nav-links a {
  color: #faf0f0;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: color 0.2s, text-shadow 0.2s;
}
.ap-nav-links a:hover {
  color: #d9b061;
  text-shadow: 0 0 10px rgba(210, 169, 81, 0.6);
}
.ap-burger {
  display: none;
  background: none;
  border: 0;
  color: #faf0f0;
  font-size: 22px;
  cursor: pointer;
}
.ap-theme-toggle {
  position: absolute;
  right: 70px;
  width: 50px;
  height: 50px;
  border: 1px solid rgba(210, 169, 81, 0.22);
  border-radius: 50%;
  background: rgba(42, 33, 4, 0.85);
  color: #faf0f0;
  font-size: 30px;
  line-height: 1;
  cursor: pointer;
  backdrop-filter: blur(12px);
}

/* Boutons avec effet néon au hover comme dans site/styles.css (.btn-gold) */
.ap-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 38px;
  padding: 0 26px;
  border-radius: 8px;
  background-color: var(--ap-gold);
  color: #1e1500;
  font-weight: 700;
  font-size: 13px;
  text-decoration: none;
  white-space: nowrap;
  transition: box-shadow 220ms ease, filter 220ms ease, background-color 220ms ease;
}
.ap-btn:hover {
  background-color: var(--ap-gold-hover);
  box-shadow: 0 0 10px #d2a951cc, 0 0 24px #d2a9518c;
  filter: saturate(1.08);
}
.ap-btn-small {
  min-width: 145px;
  min-height: 36px;
  padding: 0 22px;
  border-radius: 8px;
}

/* Titre + bannière */
.ap-title {
  margin: 34px 0 30px;
  text-align: center;
  font-size: 52px;
  font-weight: 700;
  color: #faf0f0;
}
.ap-banner img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 20px;
}
.ap-stack {
  display: flex;
  justify-content: center;
  margin: 64px 0 60px;
  padding: 0 16px;
}
.ap-stack img {
  width: 100%;
  max-width: 788px;
  height: auto;
}

/* Sections */
.ap-section {
  width: 100%;
  max-width: none;
  margin: 0 0 84px;
  padding: 0 48px;
}
.ap-section-result,
.ap-section-links {
  padding: 0 94px;
}
.ap-h2 {
  margin: 0 0 28px;
  padding: 0;
  border: 0;
  font-size: 30px;
  font-weight: 700;
  color: #faf0f0;
}
.ap-text {
  margin: 0;
  padding: 0 0 0 60px;
  max-width: 1280px;
  font-size: 16px;
  line-height: 1.45;
  color: #faf0f0;
}
.ap-text-result {
  padding: 0;
  max-width: 1220px;
}
.ap-center {
  display: flex;
  justify-content: center;
  margin-top: 48px;
}

/* Badge */
.ap-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin: 0 0 28px 30px;
  padding: 6px 14px;
  border-radius: 999px;
  background: #2b2408;
  color: #faf0f0;
  font-size: 13px;
  font-weight: 600;
}
.ap-badge svg {
  color: var(--ap-gold-bright);
}

/* Timeline */
.ap-timeline {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0 0 0 100px;
}
.ap-timeline::before {
  content: '';
  position: absolute;
  left: 129px;
  top: 15px;
  bottom: 15px;
  width: 2px;
  background: linear-gradient(to bottom, #e0b220, #7a600e);
}
.ap-step {
  position: relative;
  display: flex;
  align-items: center;
  gap: 28px;
  min-height: 120px;
}
.ap-step-num {
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
  background: linear-gradient(135deg, #f0c430, #c89610);
  color: #151200;
  font-weight: 700;
  font-size: 15px;
  box-shadow: 0 0 0 6px var(--ap-bg);
}
.ap-step-body {
  flex: 1;
  min-width: 0;
}
.ap-step-body h3 {
  margin: 0 0 6px;
  font-size: 19px;
  font-weight: 700;
  color: #faf0f0;
}
.ap-step-body p {
  margin: 0;
  font-size: 14px;
  color: rgba(250, 240, 240, 0.72);
}
.ap-step-img img {
  display: block;
  max-width: 260px;
  max-height: 100px;
  border-radius: 12px;
}
.ap-step-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 92px;
  height: 52px;
  margin-right: 32px;
  border-radius: 10px;
  background: #231e08;
  border: 1px solid rgba(210, 169, 81, 0.14);
  font-size: 10px;
  text-align: center;
  color: #e8deb5;
}
.ap-step-placeholder strong {
  font-size: 11px;
  letter-spacing: 0.4px;
  color: #faf0f0;
}

/* Liens utiles */
.ap-links {
  display: flex;
  justify-content: center;
  margin-top: 38px;
}
.ap-link-item {
  display: flex;
  align-items: center;
  gap: 22px;
  font-size: 16px;
  font-weight: 700;
  color: #faf0f0;
}

.ap-footer {
  text-align: center;
  color: #c4a96b;
  margin: 0;
  padding: 24px 16px 40px;
}

/* Responsive */
@media (max-width: 1100px) {
  .ap-nav-links,
  .ap-nav-pill {
    gap: 24px;
  }
  .ap-theme-toggle {
    right: 16px;
  }
}

@media (max-width: 800px) {
  .ap-navbar {
    padding: 14px 16px 10px;
  }
  .ap-burger {
    display: block;
  }
  .ap-nav-links {
    display: none;
    position: absolute;
    top: 72px;
    left: 50%;
    transform: translateX(-50%);
    flex-direction: column;
    gap: 16px;
    padding: 20px 32px;
    border-radius: 20px;
    background: rgba(30, 21, 0, 0.96);
    border: 1px solid rgba(210, 169, 81, 0.25);
  }
  .ap-nav-links.open {
    display: flex;
  }
  :global(body.light-theme) .ap-nav-links {
    background: rgba(255, 250, 239, 0.96);
    border-color: rgba(210, 169, 81, 0.35);
  }
  .ap-title {
    font-size: 38px;
  }
  .ap-section,
  .ap-section-result,
  .ap-section-links {
    padding: 0 16px;
    margin-bottom: 60px;
  }
  .ap-h2 {
    font-size: 24px;
  }
  .ap-text,
  .ap-text-result {
    padding: 0;
    font-size: 15px;
  }
  .ap-timeline {
    padding-left: 0;
  }
  .ap-timeline::before {
    left: 29px;
  }
  .ap-step {
    gap: 16px;
    min-height: 90px;
  }
  .ap-step-placeholder {
    margin-right: 0;
  }
  .ap-link-item {
    flex-direction: column;
    gap: 12px;
  }
}
</style>
