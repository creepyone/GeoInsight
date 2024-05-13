<script>
import axios from "axios"
import {computed} from 'vue'
import {useRoute} from 'vue-router'
import {useRouter} from 'vue-router'
const route = useRoute()
var user_id = null;

export default {
  data() {
    return {
      router : useRouter(),
      array: []
    };
  },
  methods: {
    show_analysis(id_analysis) {
      const enterFunction = () => {
        console.log('ID записи: ' + id_analysis)
        console.log('ID пользователя: ' + user_id)
        this.router.push({ name: 'history-analysis-info', params: { id: user_id, id_analysis: id_analysis} });};
        enterFunction()
    }
  },
  mounted() {
    user_id = parseInt(window.location.pathname.split('/')[2])
    const data = {
      user_id: user_id
    };
    axios.get(
        'http://127.0.0.1:5000/analysis_api/analysis_history'
        , {
            params: data
        }
    )
    .then(response => {
      for (var item in response.data) {
        this.array.push(response.data[item])
      }
    }).catch((e) => {
      if (e.response) {
        alert('Внутренняя ошибка сервера')
      }
    });
  },
};
</script>

<template>
  <container>
  <h4 class="display-8 fw-normal" align="center">
  История запросов
  </h4>

  <div v-if="array.length > 0">
  <h6 class="display-8 fw-normal">
     Нажмите на запись, чтобы просмотреть ее.
  </h6>
  <table class="table table-striped">
    <thead>
      <tr>
        <th scope="col" width="100">Номер</th>
        <th scope="col">Дата запроса</th>
        <th scope="col">Исходное изображение</th>
        <th scope="col">Классифицированные поверхности</th>
        <th scope="col">Найденные здания</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in array" class='text-center':key="item.id" @click="show_analysis(item.id)">
        <td class="align-middle">{{ item.new_id }}</td>
        <td class="align-middle">{{ item.created_dttm }}</td>
        <td class="align-middle"><img :src="item.original_image" width="100" height="100"></td>
        <td class="align-middle"><img :src="item.segmentation_image" width="100" height="100"></td>
        <td class="align-middle"><img v-if="item.detection_image != null" :src="item.detection_image" width="100" height="100"></td>
      </tr>
    </tbody>
  </table>
</div>

<div v-if="array.length == 0">
  <h6 class="display-8 fw-normal" align="center">
    История запросов для текущего пользователя не найдена. Сделайте свой первый запрос на вкладке "Анализ".
  </h6>
</div>

  </container>
</template>


<style>
table tbody tr:hover {
  cursor: pointer;
}
</style>