<template>
  <component :is="currentView" />
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import App from './App.vue';
import LowSens from './lowsens/LowSens.vue';
import USSD from './ussd/ussd.vue';

// Routage minimal basé sur le hash (#/lowsens)
const routes = {
  '#/lowsens': LowSens,
  '#/ussd': USSD
};

const hash = ref(window.location.hash);
const currentView = computed(() => routes[hash.value] || App);

const onHashChange = () => {
  hash.value = window.location.hash;
};

onMounted(() => window.addEventListener('hashchange', onHashChange));
onUnmounted(() => window.removeEventListener('hashchange', onHashChange));
</script>
