<script setup>
  import {useRouter} from 'vue-router'
  import axios from "axios";
  const router = useRouter()
  function authorize() {      
    var login = document.getElementById("loginInput")?.value;
    var password = document.getElementById("passwordInput")?.value;

    // Проверка на валидный email-адрес
    // if (!/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(email)) {
    //   alert("В поле Email должен быть указан валидный email-адрес");
    //   return;
    // }

    // Проверка на длину пароля
    if (password.length < 6 || password.length > 14) {
      alert("В поле Пароль должно быть указано от 6 до 14 символов");
      return;
    }
    
    const data = {
      login: login,
      password: password
    };

    console.log(data);

    axios.post(
        'http://127.0.0.1:5000/user_api/login'
        , data
      )
      .then(response => {
        var user_id = response.data['user_id'] // тут лежит id пользователя
        var login = response.data['login']
        console.log(user_id)
        console.log(login)
        router.push({ name: 'main-screen-auth', params: { id: user_id } })

      }).catch((e) => {
        if (e.response) {
          var error_p = document.getElementById('error')
          var status_code = e.response.status_code
          if (status_code = 401) {
            error_p.innerHTML = e.response.data.auth_error
          }
        } else {
          alert('Внутренняя ошибка сервера')
        }
      });
  }
</script>

<style>
.form-signin {
  max-width: 390px;
  padding: 15px;
}
 
.form-signin .form-floating:focus-within {
  z-index: 2;
}

 
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
 
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>

<template>
  <container>
    <h4 class="display-8 fw-normal" align="center">
      Войти в систему GeoInsight
    </h4>
    <main class="form-signin w-100 m-auto">
    <form id="register-form">
      <div class="form-floating">
        <input type="email" class="form-control" id="loginInput" placeholder="name@example.com">
        <label for="floatingInput">Логин</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="passwordInput" placeholder="Password">
        <label for="floatingPassword">Пароль</label>
      </div>
      <div class="form-floating">
        <p id="error" style="color:red" align="center" font-color="red"></p>
      </div>
      <button class="btn btn-primary w-100 py-2" id="btn-authorize" type="button" @click="authorize()">Войти</button>
    </form>
    </main>
  </container>
</template>
