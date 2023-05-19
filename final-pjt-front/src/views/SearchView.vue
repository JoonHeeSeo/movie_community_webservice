<template>
  <div>
    <h1>Search</h1>
    <div v-if="movies !== null && movies.length > 0">
      <li v-for="movie in movies" :key="movie.id" :movie="movie">
        {{ movie.title }}
      </li>
    </div>
    <div v-else>      
      <p>{{ searchedmovie }} 검색결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "https://api.themoviedb.org/3/search/movie?api_key=af5292844a6af1d68203e1c0b3104130&query="

export default {
  name:'SearchView',
  data(){
    return{
      moviesearch: null,
      movies: null
    }
  },
  updated() {
    axios({
      method: 'get',
      url: `${API_URL}` + this.$store.state.moviesearch + "&language=ko-kr",
    })
  
    .then(res =>
      this.movies = res.data.results
    )
    .catch(err => console.log(err))
  },
  computed: {
    searchedmovie: function() {
      return this.$store.state.moviesearch
    }
  }
}
</script>

<style>

</style>