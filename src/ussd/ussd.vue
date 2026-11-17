<template>
  <div class="ussd-page">
    <nav class="ussd-navbar" aria-label="Navigation du projet">
      <div class="ussd-nav-pill">
        <img :src="logo" alt="Logo USSD" class="ussd-nav-logo" />
        <ul class="ussd-nav-links" :class="{ open: menuOpen }">
          <li v-for="link in navLinks" :key="link.href">
            <a :href="link.href" @click.prevent="scrollTo(link.href)">{{ link.label }}</a>
          </li>
        </ul>
        <a href="#/" class="ussd-button ussd-button-small">Retour <span>→</span></a>
        <button class="ussd-burger" type="button" aria-label="Ouvrir le menu" @click="menuOpen = !menuOpen">
          &#9776;
        </button>
      </div>
      <button
        class="ussd-theme-toggle"
        type="button"
        :aria-label="isLightTheme ? 'Activer le thème sombre' : 'Activer le thème clair'"
        @click="isLightTheme = !isLightTheme"
      >
        &#9788;
      </button>
    </nav>

    <main>
      <h1 class="ussd-title">Projet USSD</h1>

      <div class="ussd-banner">
        <img :src="banniere" alt="Site officiel de l'Union Sportive de Saint Denis de Pile" />
      </div>

      <div class="ussd-stack">
        <img :src="competences" alt="Figma" />
      </div>

      <section id="ussd-presentation" class="ussd-section">
        <h2>Présentation du projet</h2>
        <p>
          Dans le cadre du développement et de la professionnalisation d'une structure esport amatrice en pleine
          expansion, ce projet a pour but de construire une identité numérique forte à la suite d'une fusion. La
          version initiale du site ne répondant plus aux nouveaux enjeux de l'organisation, j'ai pris en charge la
          refonte complète du design afin d'en faire un véritable hub communautaire et informatif. Conçu pour valoriser
          l'écosystème du club auprès des fans, des compétiteurs et de futurs partenaires, le site centralise
          l'ensemble des contenus importants tel que le fil d'actualités, le calendrier des matchs à venir, ceux des
          derniers résultats et de la mise en valeur des différents rosters. Cette initiative a permis d'harmoniser
          l'image de marque de la nouvelle structure tout en offrant une expérience utilisateur fluide et adaptée aux
          exigences des dirigeants.
        </p>
      </section>

      <section id="ussd-realisation" class="ussd-section">
        <h2>Comment je l'ai réalisé ?</h2>
        <span class="ussd-badge">
          <svg viewBox="0 0 24 24" aria-hidden="true">
            <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2" />
            <path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          </svg>
          En cours
        </span>

        <ol class="ussd-timeline">
          <li v-for="(step, index) in steps" :key="step.title" class="ussd-step">
            <span class="ussd-step-number">{{ index + 1 }}</span>
            <div>
              <h3>{{ step.title }}</h3>
              <p>{{ step.subtitle }}</p>
            </div>
            <div class="ussd-placeholder">
              <strong>ILLUSTRATION</strong>
              <span>{{ step.image }}</span>
            </div>
          </li>
        </ol>
      </section>

      <section id="ussd-raison" class="ussd-section ussd-reason">
        <h2>Raison d'être du projet</h2>
        <p>
          Dans le cadre d'une étape historique avec leur montée en Régional 3 et une expansion de sa communication sur
          les réseaux sociaux, ce club de football souhaitait aligner son image numérique avec ses nouvelles ambitions.
          La plateforme existante, générée via un outil standardisé, ne répondait plus aux exigences du club en matière
          de personnalisation, d'autonomie et de performance. L'objectif de ce projet était donc de concevoir et
          développer un site web entièrement sur-mesure, offrant à la direction la pleine propriété de son outil
          numérique tout en valorisant l'identité du club auprès de ses supporters et partenaires.
        </p>
      </section>

      <section id="ussd-liens" class="ussd-section">
        <h2>Liens utiles du projet</h2>
        <div class="ussd-links">
          <div class="ussd-link-item">
            <span>Dépôt GitHub :</span>
            <a :href="repoUrl" target="_blank" rel="noopener noreferrer" class="ussd-button">Qui sont nos éducateurs ? <span>→</span></a>
          </div>
          <div class="ussd-link-item">
            <span>Documentation :</span>
            <a :href="docUrl" target="_blank" rel="noopener noreferrer" class="ussd-button">Qui sont nos éducateurs ? <span>→</span></a>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref, watch } from 'vue';
import banniere from './img/banniere.svg';
import competences from './img/competences.svg';
import logo from './img/logo.svg';

const isLightTheme = ref(false);
const menuOpen = ref(false);
const repoUrl = '#';
const docUrl = '#';

const navLinks = [
  { href: '#ussd-presentation', label: 'Présentation' },
  { href: '#ussd-realisation', label: 'Réalisation' },
  { href: '#ussd-raison', label: 'Pourquoi ?' },
  { href: '#ussd-liens', label: 'Lien utiles' }
];

const steps = [
  { title: 'Recueil des besoins', subtitle: 'Maquette — image : téléphone', image: 'Téléphone' },
  { title: "Définition de l'identité visuelle & de la structure du site", subtitle: 'Maquette — image : téléphone', image: 'Figma' }
];

watch(isLightTheme, (value) => {
  document.body.classList.toggle('light-theme', value);
});

const scrollTo = (hash) => {
  menuOpen.value = false;
  document.querySelector(hash)?.scrollIntoView({ behavior: 'smooth' });
};

onMounted(() => {
  document.body.classList.remove('light-theme');
  document.body.classList.add('ussd-scrollbar');
  document.body.style.backgroundColor = '#150000';
  window.scrollTo(0, 0);
});

onUnmounted(() => {
  document.body.classList.remove('ussd-scrollbar');
  document.body.style.removeProperty('background-color');
});
</script>

<style scoped>
.ussd-page {
  --ussd-bg: #150000;
  --ussd-red: #b90000;
  --ussd-bright: #f3292e;
  width: 100%;
  max-width: 1440px;
  min-height: 100vh;
  margin: 0 auto;
  padding: 92px 0 76px;
  color: #faf0f0;
  font-family: inherit;
}

:global(body:has(.ussd-page)) {
  background: var(--ussd-bg);
}
:global(body.light-theme:has(.ussd-page)) {
  background: #faeaea;
}
:global(body.ussd-scrollbar::-webkit-scrollbar-track) {
  background: #210000;
}
:global(body.ussd-scrollbar::-webkit-scrollbar-thumb) {
  background: #820508;
  border-radius: 10px;
}
:global(body.ussd-scrollbar::-webkit-scrollbar-thumb:hover) {
  background: #a90000;
}

.ussd-navbar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 0 16px;
}
.ussd-nav-pill {
  display: flex;
  align-items: center;
  width: min(1246px, calc(100vw - 32px));
  gap: 40px;
  min-height: 72px;
  padding: 13px 72px 13px 16px;
  border: 1px solid rgba(251, 8, 12, .2);
  border-radius: 999px;
  background: #3700018c;
  backdrop-filter: blur(10px);
}
.ussd-nav-logo { width: 45px; height: 45px; }
.ussd-nav-links {
  display: flex;
  gap: 50px;
  flex: 1;
  margin: 0;
  padding: 0;
  list-style: none;
}
.ussd-nav-links a {
  color: #faf0f0;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
}
.ussd-nav-links a:hover { color: #ff6d70; }
.ussd-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 45px;
  padding: 0 22px;
  border: 0;
  border-radius: 999px;
  background: #820508;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  white-space: nowrap;
}
.ussd-button:hover { filter: brightness(1.2); }
.ussd-button-small { width: 130px; min-height: 40px; padding: 0; }
.ussd-theme-toggle {
  position: absolute;
  right: max(16px, calc((100vw - 1246px) / 2 + 16px));
  width: 40px;
  height: 40px;
  border: 0;
  border-radius: 50%;
  background: #faf0f0;
  color: #150000;
  font-size: 32px;
  line-height: 1;
  cursor: pointer;
}
.ussd-burger { display: none; }

.ussd-title {
  margin: 34px 0 30px;
  color: #faf0f0;
  font-size: 54px;
  text-align: center;
}
.ussd-banner img {
  display: block;
  width: 100%;
  border-radius: 12px;
}
.ussd-stack {
  display: flex;
  justify-content: center;
  margin: 70px 0 60px;
}
.ussd-stack img { width: 87px; }

.ussd-section {
  margin: 0 0 90px;
  padding: 0 48px;
}
.ussd-section h2 {
  margin: 0 0 26px;
  border: 0;
  color: #faf0f0;
  font-size: 24px;
}
.ussd-section p {
  max-width: 1180px;
  margin: 0 auto;
  font-size: 16px;
  line-height: 1.5;
}
.ussd-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin: 0 0 30px 30px;
  padding: 6px 14px;
  border-radius: 999px;
  background: #2b0d0d;
  color: #faf0f0;
  font-size: 14px;
}
.ussd-badge svg { width: 14px; height: 14px; color: var(--ussd-bright); }
.ussd-timeline {
  position: relative;
  max-width: 1180px;
  margin: 0 auto;
  padding: 0 0 0 100px;
  list-style: none;
}
.ussd-timeline::before {
  content: '';
  position: absolute;
  top: 16px;
  bottom: 14px;
  left: 72px;
  width: 2px;
  background: linear-gradient(#f3292e, #7d1717);
}
.ussd-step {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 92px;
  align-items: center;
  min-height: 120px;
}
.ussd-step-number {
  position: absolute;
  left: -44px;
  display: grid;
  place-items: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #a90000;
  font-size: 16px;
}
.ussd-step h3 { margin: 0 0 6px; font-size: 19px; }
.ussd-step p { margin: 0; font-size: 15px; }
.ussd-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 92px;
  height: 52px;
  border-radius: 8px;
  background: #210909;
  color: #faf0f0;
  font-size: 10px;
  text-align: center;
}
.ussd-placeholder strong { color: #ff6568; font-size: 11px; }
.ussd-reason { padding: 0 72px; }
.ussd-links {
  display: flex;
  justify-content: space-around;
  gap: 30px;
  margin-top: 40px;
}
.ussd-link-item {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 16px;
}
.ussd-link-item .ussd-button { min-width: 150px; font-size: 14px; }

@media (max-width: 800px) {
  .ussd-navbar { padding: 12px 16px; }
  .ussd-nav-pill { gap: 14px; min-height: 50px; padding: 6px 52px 6px 12px; }
  .ussd-nav-logo { width: 32px; height: 32px; }
  .ussd-nav-links { display: none; }
  .ussd-nav-links.open {
    position: absolute;
    top: 62px;
    left: 50%;
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 18px 26px;
    border: 1px solid #480000;
    border-radius: 16px;
    background: #210000;
    transform: translateX(-50%);
  }
  .ussd-burger {
    display: block;
    border: 0;
    background: transparent;
    color: #fff;
    font-size: 20px;
  }
  .ussd-theme-toggle { right: 16px; }
  .ussd-title { margin: 24px 0 22px; font-size: 30px; }
  .ussd-section, .ussd-reason { padding: 0 20px; }
  .ussd-section p { font-size: 14px; }
  .ussd-timeline { padding-left: 60px; }
  .ussd-timeline::before { left: 28px; }
  .ussd-step { grid-template-columns: minmax(0, 1fr) 72px; min-height: 100px; }
  .ussd-step h3 { font-size: 16px; }
  .ussd-step p { font-size: 13px; }
  .ussd-links { flex-direction: column; align-items: flex-start; }
}
</style>
