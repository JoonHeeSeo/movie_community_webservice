<template>
  <div id="app">
    <nav class="container">
      <router-link to="/">홈</router-link> |
      <router-link to="/recommend">영화추천</router-link> |
      <router-link to="/search">영화 검색</router-link> |
      <router-link to="/signin">로그인</router-link> |
      <router-link to="/signup">가입</router-link> |
      <router-link to="/community">게시판</router-link>
      <div class="searchbox">

        <p>{{ username }}님 환영합니다</p>

        <label for="searchinput"></label>
        <input type="text" v-on:keyup.enter="search()" id="inputtext" v-model="inputtext" style="border-radius:4px">
        <button class="search-btn" @click="search()">검색</button>
      </div>

      <!-- 게시판은 로그인 했을때만 보이게, 로그인 안했으면 안보이게 만들어야함  -->
    </nav>
    <div class="router-section"></div>
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
  created() {
    this.connetApi()
  },
  computed: {
    username() {
      return this.$store.state.username
    },
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
    },
    connetApi(){
      this.$store.dispatch('connetMovies')
    }
  }
}

</script>

<style>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
}

nav {
  width: 100%;
  height: 60px;
  position: fixed;
  top: 0;
  z-index: 9;
  padding: 0 2.5vw;
  display: flex;
  align-items: center;
  background-color: black;
  color: white;
}

.logo{
  height: 60%;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: grey;
}

.searchbox{
  width: fit-content;
  display: flex;
  justify-content: center;
  align-content: center;
  height: auto;
  margin-left: auto;
}

.search-btn{
  border: 1px solid #fff;
  border-radius: 2px;
  background: none;
  color: #fff;
  height: 35px;
  padding: 0 10px;
  margin-left: 10px;
  text-transform: uppercase;
  cursor: pointer;
}

.router-section{
  width: 100%;
  margin-top: 60px;
  position: relative;
}
</style>
