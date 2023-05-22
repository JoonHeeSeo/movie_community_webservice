<template>
  <div>
    <h2 style="text-align:center; margin-top:80px; margin-bottom: 20px;">로그인</h2>
    <form @submit.prevent = "logIn" class="login-container">
      <input type="text" id="userid" v-model="userid" placeholder="아이디를 입력하세요" style="margin-bottom: 10px;">
      <br>
      <input type="text" id="password" v-model="password" placeholder="비밀번호를 입력하세요">
      <br>
      <input class="login-button" type="submit" value="로그인">
    </form>
  </div>
</template>

<script>
export default {
  name:'LogInView',
  data() {
    return {
      userid: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const userid = this.userid
      const password = this.password

      const payload = {
        userid, password
      }

      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f7f7f7;
}

input[id="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[id="userid"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.login-button {
  display: block;
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  margin-top:20px;
  background-color: #bfd2ea;
  color: #fff;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
}

.login-button:hover {
  background-color: rgb(34, 80, 171);
}

</style>