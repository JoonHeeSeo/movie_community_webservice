<template>
  <div id="app">
    <nav>
      <router-link to="/" class="router-btn">HOME</router-link>
      <router-link to="/recommend" class="router-btn">Surprise Me</router-link>
      <!-- <router-link to="/search" class="router-btn">영화 검색</router-link> -->
      <router-link to="/community" class="router-btn">Board</router-link>

      <div v-if="!username">
        <router-link to="/login" class="router-btn">Sign In</router-link>
        <router-link to="/signup" class="router-btn">Sign Up</router-link>
      </div>

      <div v-if="username">
        <p>Welcome
          <router-link :to="{ name: 'profile/:username', params: { username: username } }">{{ username }}</router-link>!</p>
        <button @click="logOut">Sign Out</button>
      </div>

      <div class="searchbox">
        <label for="searchinput"></label>
        <input type="text" v-on:keyup.enter="search()" id="searchInput" v-model="searchInput" style="border-radius:4px">
        <button class="search-btn" @click="search()">search</button>
      </div>

    </nav>
    <div class="router-section"></div>
    <router-view/>
  </div>
</template>

<script>

export default {
  data() {
    return{
      searchInput: '',
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

      const searchInput = this.searchInput
      this.$store.dispatch('saveSearchInput', searchInput)
      
      if (this.searchInput.trim() === "") {
        alert('영화 제목을 입력해주세요.');
        return;
      }

      if (this.$route.path !== '/search') {
        this.$router.push({ name:'search' })
        location.reload()
      } else {
        location.reload()
      }
    },
    

    logOut() {
      const token = this.$store.state.token
      this.$store.dispatch('logOut', token)
    },
    
    connetApi(){
      this.$store.dispatch('getMovies')
    },
    
  },

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
  text-align: left;
  color: #fff;
  width: 100%;
}

nav {
  width: 100%;
  height: 60px;
  position: fixed;
  top: 0;
  z-index: 9999;
  padding: 10px;
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

.router-btn{
  margin: 20px;
}
</style>
