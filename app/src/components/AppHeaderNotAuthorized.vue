<script setup>
  import {
    useRouter
  } from 'vue-router'
  const router = useRouter()
</script>

<template>
<container>
  
  <header class="d-flex flex-wrap align-items-start justify-content-start justify-content-md-between py-3 mb-4 border-bottom">

  <ul class="nav col-12 col-md-auto mb-md-0">

    <li><a href="#" class="nav-link px-2 link-secondary" @click="router.push({ name: 'main-screen-not-auth' })">GeoInsignt</a></li>
    <li><a href="#" class="nav-link px-2" @click="router.push({ name: 'about-us-not-auth' })">О нас</a></li>
  </ul>

  <div class="col-md-3 text-end">
    <button type="button" class="btn btn-outline-primary me-2" @click="router.push({ name: 'log-in' })">Войти</button>
    <button type="button" class="btn btn-primary" @click="router.push({ name: 'sign-up' })">Зарегистрироваться</button>
  </div>
  </header>
</container>
</template>