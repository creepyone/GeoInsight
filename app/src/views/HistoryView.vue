<script setup>
import {
    computed
  } from 'vue'
  import {
    useRoute
  } from 'vue-router'
  const route = useRoute()
  const user_id = computed(() => route.params.id)
import Header from '../components/AppHeaderAuthorized.vue';
import Body from '../components/AppHistory.vue';
import Footer from '../components/AppFooter.vue';
</script>

<template>
  <div class="container px-3 mx-auto">
    <Header />
    <Body />
    <Footer />
  </div>
</template>
