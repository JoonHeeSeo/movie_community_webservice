<template>
  <div id="app">
    <nav>
      <router-link to="/">홈</router-link> |
      <router-link to="/recommend">영화추천</router-link> |
      <router-link to="/search">영화 검색</router-link> |
      <router-link to="/signin">로그인</router-link> |
      <router-link to="/signup">가입</router-link> |
      <router-link to="/community">게시판</router-link>
      <!-- 게시판은 로그인 했을때만 보이게, 로그인 안했으면 안보이게 만들어야함  -->
    </nav>
    <router-view/>
  </div>
</template>

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
