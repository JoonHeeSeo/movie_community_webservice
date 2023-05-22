<template>
  <div>
    <h1>Search</h1>
    <div v-if="movies !== null && movies.length > 0">
      <li v-for="movie in movies" :key="movie.id" :movie="movie">
        <div class="poster-container">
          <img :src="getMoviePoster(movie.poster_path)" alt="movie_post" class="poster">
        </div>

        <p>{{ movie.adult }}</p>
        <p>{{ movie.backdrop_path }}</p>
        <p>{{ movie.genre_ids }}</p>
        <p>{{ movie.id }}</p>
        <p>{{ movie.original_language }}</p>
        <p>{{ movie.original_title }}</p>
        <p>{{ movie.overview }}</p>
        <p>{{ movie.popularity }}</p>
        <p>{{ movie.poster_path }}</p>
        <p>{{ movie.release_date }}</p>
        <p>{{ movie.title }}</p>
        <p>{{ movie.video }}</p>
        <p>{{ movie.vote_average }}</p>
        <p>{{ movie.vote_count }}</p>

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
      movies: null,
    }
  },
    
  updated() {
    axios({
      method: 'get',
      url: `${API_URL}` + this.$store.state.moviesearch + "&language=ko-kr",
    })
  
    .then((res) => {
      this.movies = res.data.results
    })
    .catch((err) => {
      console.log(err)
    })
  },
  
  computed: {
    searchedmovie: function() {
      return this.$store.state.moviesearch
    }
  },
  
  methods: {
    getMoviePoster(poster_path) {
      return "https://image.tmdb.org/t/p/w200" + poster_path
    }
  }
}
</script>

<style>
.poster-container {
  width: 230px;
  position: relative;
  left: 20px;
  z-index: 9999;
}

.poster {
  width: 100%;
  box-shadow: 0, 5px, 20px, rgba(0, 5px, 20px, 0.6);
}
</style>