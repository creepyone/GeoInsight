<script>
import axios from "axios"
import {computed} from 'vue'
import {useRoute} from 'vue-router'
import {useRouter} from 'vue-router'
const route = useRoute()
const user_id = parseInt(window.location.pathname.split('/')[2])
const analysis_id = parseInt(window.location.pathname.split('/')[4])

export default {
  data() {
    return {
      router : useRouter(),
      item: null
    };
  },
  mounted() {
    console.log(user_id)
    console.log(analysis_id)
    const data = {
        user_id: user_id,
        analysis_id: analysis_id
    };
    console.log(data);
    axios.post(
      'http://127.0.0.1:5000//analysis_api/analysis_info'
      , data
    )
    .then(response => {
        this.item = response.data
        this.item.original_image = "../"+ this.item.original_image
        this.item.segmentation_image = "../"+ this.item.segmentation_image
        this.item.detection_image = "../"+ this.item.detection_image
    }).catch((e) => {
      if (e.response) {
        alert('Внутренняя ошибка сервера')
      }
      else alert('Внутренняя ошибка сервера')
    });
  },
};
</script>

<template>
  <container>
    <button
          class="btn btn-primary"
          id="btn-analyze"
          type="button"
          @click="router.push({ name: 'history' })"
          style="position: relative"
        >
          <span role="status">Назад</span>
    </button>
  <h4 class="display-8 fw-normal" align="center">
  Запрос от {{item.created_dttm}}
  </h4>
  <table class="table table-striped" width="50%">
    <thead>
      <tr>
        <th scope="col">Исходное изображение</th>
        <th scope="col">Классифицированные поверхности</th>
        <th scope="col">Найденные здания</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><img :src="item.original_image" width="400" height="400"></td>
        <td><img :src="item.segmentation_image" width="400" height="400"></td>
        <td><img v-if="item.detection_image != null" :src="item.detection_image" width="400" height="400"></td>
      </tr>
    </tbody>
  </table>

  </container>
</template>
