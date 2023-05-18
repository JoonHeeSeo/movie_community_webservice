<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent = "signIn">
      <label for="userid">아이디 : </label>
      <input type="text" id="userid" v-model="userid">
      <br>
      <label for="password">비밀번호 : </label>
      <input type="text" id="password" v-model="password">
      <br>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script>
export default {
  name:'SignInView',
  data() {
    return {
      userid: null,
      password: null,
    }
  },
  methods: {
    signIn() {
      const userid = this.userid
      const password = this.password

      const payload = {
        userid, password
      }

      this.$store.dispatch('signIn', payload)
    }
  }
}
</script>

<style>

</style>