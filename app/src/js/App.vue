<script setup>
import HeaderAuthorized from '../components/AppHeaderAuthorized.vue'
import HeaderNotAuthorized from '../components/AppHeaderNotAuthorized.vue'
import Footer from '../components/AppFooter.vue'
import Map from '../components/AppMap.vue'
</script>

<template>
  <div class="container px-3 mx-auto">
    <HeaderAuthorized />
    <Map />
    <Footer />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
