<script setup>
import Header from '../components/AppHeaderAuthorized.vue';
import Body from '../components/AppMap.vue';
import Footer from '../components/AppFooter.vue';
import Legend from '../components/AppLegend.vue';
</script>

<template>
  <div class="container px-3 mx-auto">
    <Header />
    <Body />
    <Legend />
    <Footer />
  </div>
</template>
