<script setup>
import Header from '../components/AppHeaderAuthorized.vue';
import Body from '../components/AppAnalysis.vue';
import Footer from '../components/AppFooter.vue';
import Legend from '../components/AppLegend.vue';
import {
    computed
  } from 'vue'
  import {
    useRoute
  } from 'vue-router'
  const route = useRoute()
  const id = computed(() => route.params.id)
</script>

<template>
  <div class="container px-3 mx-auto">
    <section>
        <router-view />
    </section>
    <Header />
    <Body />
    <Legend />
    <Footer />
  </div>
</template>
