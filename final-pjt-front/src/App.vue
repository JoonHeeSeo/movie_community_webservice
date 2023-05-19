<template>
  <div id="app">
    <nav>
      <router-link to="/">홈</router-link> |
      <router-link to="/recommend">영화추천</router-link> |
      <router-link to="/search">영화 검색</router-link> |
      <router-link to="/signin">로그인</router-link> |
      <router-link to="/signup">가입</router-link> |
      <router-link to="/community">게시판</router-link>
      <div>
        <label for="searchinput">검색 : </label>
        <input type="text" v-on:keyup.enter="search()" id="inputtext" v-model="inputtext">
        <button @click="search()">검색</button>
      </div>

      <!-- 게시판은 로그인 했을때만 보이게, 로그인 안했으면 안보이게 만들어야함  -->
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  data() {
    return{
      inputtext: null,
      currentRoute: window.location.pathname
    }
  },
  methods: {
    search() {
      const inputtext = this.inputtext
      // 이거 담아서 Moviedetail로 연결시켜줘야하는데 어떻게 하지?
      console.log(inputtext)
      this.$store.state.moviesearch = inputtext
      if (this.$route.path !== '/search') {
        this.$router.push({ name:'search' })
      } 
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: black;
  color: white;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: grey;
}
</style>
