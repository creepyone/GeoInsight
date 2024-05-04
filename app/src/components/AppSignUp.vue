<script>
export default {
  data() {
  },
  methods: {
    register() {
      var name = document.getElementById("nameInput")?.value;
      var email = document.getElementById("emailInput")?.value;
      var password = document.getElementById("passwordInput")?.value;
      // Проверка на длину имени
      if (name.length <= 2) {
        alert("В поле Имя должно быть указано более 2 символов");
        return;
      }

      // Проверка на валидный email-адрес
      if (!/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(email)) {
        alert("В поле Email должен быть указан валидный email-адрес");
        return;
      }

      // Проверка на длину пароля
      if (password.length < 6 || password.length > 16) {
        alert("В поле Пароль должно быть указано от 6 до 16 символов");
        return;
      }
      
      const data = {
        name: name,
        email: email,
        password: password
      };
      console.log(data);
      /*

      axios.post(
        'http://127.0.0.1:5000/model_api/get_prediction'
        , {image: image_data.data, width: image_data.width, height: image_data.height}
        )
        .then(response => {
          console.log(response)
          console.log(response.status)
        }).catch((e) => {
          alert('Model server is not responding!')
        });
        */

    },
  }
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
    <h4>Регистрация в системе GeoInsight</h4>
    <main class="form-signin w-100 m-auto">
    <form id="register-form">
      <div class="form-floating">
        <input type="text" class="form-control" id="nameInput" placeholder="Иван">
        <label for="floatingInput">Имя</label>
      </div>
      <div class="form-floating">
        <input type="email" class="form-control" id="emailInput" placeholder="name@example.com">
        <label for="floatingInput">Email-адрес</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="passwordInput" placeholder="Password">
        <label for="floatingPassword">Пароль</label>
      </div>
      <button class="btn btn-primary w-100 py-2" id="btn-reqister" type="button" @click="register()">Зарегистрироваться</button>
    </form>
    </main>
  </container>
</template>
