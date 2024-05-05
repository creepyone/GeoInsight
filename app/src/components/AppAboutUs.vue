<script>
export default {
  data() {
  },
  methods: {}
}
</script>
<style>
.bd-callout-warning {
    --bd-callout-color: var(--bs-warning-text-emphasis);
    --bd-callout-bg: var(--bs-warning-bg-subtle);
    --bd-callout-border: var(--bs-warning-border-subtle);
}
.bd-callout {
  --bs-link-color-rgb: var(--bd-callout-link);
  --bs-code-color: var(--bd-callout-code-color);
  padding: 1.25rem;
  margin-top: 1.25rem;
  margin-bottom: 1.25rem;
  color: var(--bd-callout-color, inherit);
  background-color: var(--bd-callout-bg, var(--bs-gray-100));
  border-left: 0.25rem solid var(--bd-callout-border, var(--bs-gray-300));
}
</style>

<template>
  <container>
    <h2 class="display-8 fw-normal" align="center">
      О программе GeoInsight
    </h2>
    <div class="bd-callout bd-callout-warning small">
    <p class="col-md-10 col-lg-12 mx-auto lead" align="justify">
      Для ознакомления с системой вы можете <a href="user_guide" download>скачать руководство пользователя</a>
    </p>
    </div>
    <p class="col-md-10 col-lg-12 mx-auto lead" align="justify">
      <b>GeoInsight</b> - система для автоматического анализа ландшафта и обнаружения объектов с использованием технологий компьютерного зрения для анализа спутниковых изображений. 
      Использование технологий компьютерного зрения позволяет автоматизировать процессы по анализу местности, минимизировать человеческие ошибки и повысить точность результатов.
    </p>
    <p class="col-md-10 col-lg-12 mx-auto lead" align="justify">
      Для работы с системой представлены следующие разделы:
      <li class="col-md-10 col-lg-12 mx-auto lead">Анализ - раздел работы с интерактивной картой для выбора территории для анализа и получения результатов анализа.</li>
      <li class="col-md-10 col-lg-12 mx-auto lead">История запросов - раздел с историей ранее отправленных пользователем запросов.</li>
      <li class="col-md-10 col-lg-12 mx-auto lead">Профиль - раздел, содержащий в себе информацию о пользователе.</li>
      <li class="col-md-10 col-lg-12 mx-auto lead">О программе - раздел, содержащий в себе информацию о предназначении системы и разработчиках.</li>
      Разделы Анализ, История запросов и Профиль доступны только для <b>авторизованных в системе</b> пользователей.
    </p>
    <p class="col-md-10 col-lg-12 mx-auto lead" align="justify">
    Система была разработана командой студентов НИУ ВШЭ - Пермь в рамках выполнения выпускной квалификационной работы в 2024 году:
      <li class="col-md-10 col-lg-12 mx-auto lead">Разработка серверной части системы - Черепанов Денис Анатольевич, <a href="mailto:dacherepanov@edu.hse.ru">dacherepanov@edu.hse.ru</a></li>
      <li class="col-md-10 col-lg-12 mx-auto lead">Разработка клиентской части системы - Крохина Ольга Андреевна, <a href="mailto:oakrokhina@edu.hse.ru">oakrokhina@edu.hse.ru</a></li>
    </p>
  </container>
</template>
