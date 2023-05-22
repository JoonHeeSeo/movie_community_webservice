<template>
  <div>
    <h1>Search</h1>

    <div v-if="movies !== null">
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

    <div v-if="searchInput === null">      
      <p>검색결과가 없습니다.</p>
    </div>


    <div v-if="movies === null">      
      <p>검색결과가 없습니다.</p>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'SearchView',
  data(){
    return{
      searchInput: null,
      movies: null,
    }
  },
    
  created() {
    this.searchInput = this.$store.state.searchInput
    this.searchMovies()
  },
  
  computed: {
    searchedmovie: function() {
      console.log(this.$store.state.searchInput)
      return this.$store.state.searchInput
    }
  },
  
  methods: {
    getMoviePoster(poster_path) {
      return "https://image.tmdb.org/t/p/w200" + poster_path
    },

    searchMovies() {
      const searchInput = this.searchInput

      axios({
        method: 'post',
        url: `${API_URL}/movies/get/movies_search/`,
        data : { searchInput },
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })  
    },
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