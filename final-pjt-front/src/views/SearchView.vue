<template>
  <div class="search-container">
    <li v-for="movie in movies" :key="movie.id" :movie="movie" style="display:flex">
      <div class="poster-container">
        <img :src="getMoviePoster(movie.poster_path)" alt="movie_post" class="search-poster">
      </div>
      <div class="search-info">
        <h3>{{ movie.title }}</h3>
        <p>출시일: {{ movie.release_date }}</p>
        <p>평점: {{ movie.vote_average }}</p>
        <p>요약: {{ movie.overview }}</p>
        <router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.id }}">          
          <button class="search-detail-btn">자세히 보기</button>
        </router-link>
          
          <!-- <p>{{ movie.vote_count }}</p> -->
          <!-- <p> adult : {{ movie.adult }}</p> -->
          <!-- <p>{{ movie.backdrop_path }}</p> -->
          <!-- <p>{{ movie.genre_ids }}</p> -->
          <!-- <p>{{ movie.id }}</p> -->
          <!-- <p>{{ movie.original_language }}</p>
          <p>{{ movie.original_title }}</p>
          <p>{{ movie.popularity }}</p>
          <p>{{ movie.poster_path }}</p>
          <p>{{ movie.video }}</p> -->

        </div>
    </li>
    <div v-if="movies === false">      
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
  
  methods: {
    getMoviePoster(poster_path) {
      return "https://image.tmdb.org/t/p/w200" + poster_path
    },

    searchMovies() {
      const searchInput = this.searchInput

      axios({
        method: 'get',
        url: `${API_URL}/movies/get/movies_search/${searchInput}/`,
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
.search-container{
  margin-top: 100px;
}
.search-poster {
  width: 100%;
  height: 330px;
  box-shadow: 0, 5px, 20px, rgba(0, 5px, 20px, 0.6);
  margin:auto;
}

.search-info {
  position: relative;
  background: black;
  padding: 30px;
  margin: 20px;
  width: 500px;
  height: auto;
  z-index: 0;
}


.search-detail-btn {
	cursor: pointer;
	width: 100%;
	background: #2f2f2f;
	color: white;
  margin-top: 30px;
	padding: 15px 0;
	font-size: 1rem;
	font-weight: bold;
	text-transform: uppercase;
	border: 0;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
}
</style>