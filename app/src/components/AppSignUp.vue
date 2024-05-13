<script setup>
  import {useRouter} from 'vue-router'
  import axios from "axios";
  const router = useRouter()
  function register() {
    var login = document.getElementById("loginInput")?.value;
    var password = document.getElementById("passwordInput")?.value;
    // Проверка на длину имени
    if (login.length <= 2) {
      alert("В поле Логин должно быть указано более 2 символов");
      return;
    }

    // // Проверка на валидный email-адрес
    // if (!/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(email)) {
    //   alert("В поле Email должен быть указан валидный email-адрес");
    //   return;
    // }

    // Проверка на длину пароля
    if (password.length < 6 || password.length > 14) {
      alert("В поле Пароль должно быть указано от 6 до 16 символов");
      return;
    }
    
    const data = {
      login: login,
      password: password
    };
    // console.log(data);
    // /*

    axios.post(
        'http://127.0.0.1:5000/user_api/register'
        , data
      )
      .then(response => {
        console.log(response)

        var user_id = response.data['user_id'] // тут лежит id пользователя
        var login = response.data['login']

        console.log(user_id, login)
        router.push({ name: 'main-screen-auth', params: { id: user_id } })

      }).catch((e) => {
        if (e.response) {
          var error_p = document.getElementById('error')
          var status_code = e.response.status_code
          if (status_code = 409) {
            error_p.innerHTML = 'Пользователь с таким логином уже существует!'
          }
          
        } else {
          alert('Внутренняя ошибка сервера')
        }
      });

      // */


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

.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
 
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
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
      Регистрация в системе GeoInsight
    </h4>
    <main class="form-signin w-100 m-auto">
    <form id="register-form">
      <div class="form-floating">
        <input type="text" class="form-control" id="loginInput" placeholder="Admin">
        <label for="floatingInput">Логин</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="passwordInput" placeholder="Password">
        <label for="floatingPassword">Пароль</label>
      </div>
      <div class="form-floating">
        <p id="error" style="color:red" align="center" font-color="red"></p>
      </div>
      <button class="btn btn-primary w-100 py-2" id="btn-reqister" type="button" @click="register()">Зарегистрироваться</button>
    </form>
    </main>
  </container>
</template>
