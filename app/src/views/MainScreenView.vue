<script setup>
import Header from '../components/AppHeaderAuthorized.vue';
import Body from '../components/AppMainScreen.vue';
import Footer from '../components/AppFooter.vue';
</script>

<template>
  <section>
    <router-view />
  </section>
  <div class="container px-3 mx-auto">
    <Header />
    <Body />
    <Footer />
  </div>
</template>
