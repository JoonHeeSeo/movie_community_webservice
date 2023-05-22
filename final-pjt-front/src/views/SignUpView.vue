<template>
  <div>
    <h2 style="text-align:center; margin-top:80px; margin-bottom: 20px;">회원가입</h2>
    <form @submit.prevent = "signUp">
      <div class="login-container" style="color:black">
        <label for="userid" style="text-align: left;">아이디 :</label>
        <input type="text" id="userid" v-model="userid">
        <br>
        <label for="password1">비밀번호 : </label>
        <input type="text" id="password1" v-model="password1">
        <br>
        <label for="password2">비밀번호 확인 : </label>
        <input type="text" id="password2" v-model="password2">
        <br>
        <input class="login-button" type="submit" value="가입">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name:'SignUpView',
  data(){
    return {
      userid: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const userid = this.userid
      const password1 = this.password1 
      const password2 = this.password2

      const payload = {
        userid, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>

input[id="password1"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[id="password2"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

</style>