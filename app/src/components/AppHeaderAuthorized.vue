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
    
        <li><a href="#" class="nav-link px-2 link-secondary" @click="router.push({ name: 'main-screen-auth' })">GeoInsignt</a></li>
        <li><a href="#" class="nav-link px-2" @click="router.push({ name: 'analysis' })">Анализ</a></li>
        <li><a href="#" class="nav-link px-2" @click="router.push({ name: 'history' })">История запросов</a></li>
        <li><a href="#" class="nav-link px-2" @click="router.push({ name: 'about-us-auth' })">О нас</a></li>
      </ul>
    
      <div class="dropdown text-end">
      <a href="#" class="d-block link-body-emphasis text-decoration-none dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        <img src="..\css\images\dog.png" alt="mdo" width="32" height="32" class="rounded-circle">
      </a>
      <ul class="dropdown-menu text-small">
        <li><a class="dropdown-item" href="#" @click="router.push({ name: 'history' })">История запросов</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#" @click="router.push({ name: 'main-screen-not-auth' })">Выйти</a></li>
      </ul>
      </div>
      </header>
    </container>
    </template>