<script>
export default {
  data() {},
  methods: {},
};
</script>

<template>
    <h5 class="display-8 fw-normal">
      Типы классифицируемых поверхностей:
    </h5>
    <table class="table table-striped table-sm" style="font-size: 1.0rem; line-height: 1.2rem;">
      <thead>
        <tr>
          <th scope="col">Пусто</th>
          <th scope="col">Агрозона</th>
          <th scope="col">Лес</th>
          <th scope="col">Здание</th>
          <th scope="col" >Дорога</th>
          <th scope="col" >Вода</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #FFFFFF;
            border-radius: 20px;
          ">
        </div></td>
          <td><div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #FFFF00;
            border-radius: 20px;
          ">
        </div></td>
          <td><div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #4A6741;
            border-radius: 20px;
          ">
        </div></td>
        <td><div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #9B7653;
            border-radius: 20px;
          ">
        </div></td>
        <td>   <div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #696969;
            border-radius: 20px;
          ">
        </div></td>
        <td><div
          class="container"
          style="
            width: 40px;
            height: 30px;
            position: relative;
            background: #0000FF;
            border-radius: 20px;
          ">
        </div></td>
        </tr>
      </tbody>
    </table>
</template>

<style>

table th {
  text-align: center;
}
</style>