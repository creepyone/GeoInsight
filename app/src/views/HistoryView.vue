<script setup>
import {
    computed
  } from 'vue'
  import {
    useRoute
  } from 'vue-router'
  const route = useRoute()
  const id = computed(() => route.params.id)
import Header from '../components/AppHeaderAuthorized.vue';
import Footer from '../components/AppFooter.vue';
</script>

<template>
  <div class="container px-3 mx-auto">
    <Header />
    <h1>Пользователь ID {{ id }}</h1>
    <Footer />
  </div>
</template>
