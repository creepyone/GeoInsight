<script setup>
  import {
    useRouter
  } from 'vue-router'
  const router = useRouter()
</script>

<template>
  <container>
    <h2 class="display-8 fw-normal" align="center">
      Добро пожаловать в GeoInsight!
    </h2>
    <p class="col-md-10 col-lg-12 mx-auto lead" align="center">
      GeoInsight - система для автоматического анализа ландшафта и обнаружения
      объектов с использованием технологий компьютерного зрения для анализа
      спутниковых изображений. Использование технологий компьютерного зрения
      позволяет автоматизировать процессы по анализу местности, минимизировать
      человеческие ошибки и повысить точность результатов.
    </p>
    <p class="col-md-10 col-lg-12 mx-auto lead" align="center">
      Для использования возможностей GeoInsight
      <router-link :to="{ name: 'log-in' }">войдите в систему</router-link> или <router-link :to="{ name: 'sign-up' }">зарегистрируйтесь</router-link>.
    </p>
  </container>
</template>
