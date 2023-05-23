<template>
  <div>
    <h1>MovieDetailView</h1>
    <div class="movie-detail-container" style="display:flex; ">
      <img :src="getMoviePoster()" alt="movie_post" class="detail-poster">
      <div >
        <p v-if="movie.title">제목: {{ movie.title }} </p>

      </div>
      <p v-if="movie.original_title">오리지날 제목: {{ movie.original_title }}</p>
      <p v-if="movie.vote_average">평점: {{ movie.vote_average }}</p>
      
      <p v-if="movie.genres && movie.genres.length > 0">장르: {{ movie.genres }}</p>
      <p v-if="movie.overview">요약: {{ movie.overview }}</p>
      
      <p v-if="movie.runtime">상영시간: {{ movie.runtime }}분</p>
      <p v-if="movie.video">{{ movie.video }}</p>
      
      <p v-if="movie.backdrop_path">{{ movie.backdrop_path }}</p>
      <!-- genre in genres로 수정해놓을 수 있도록 -->
    </div>
      <!-- <p>{{ movie }}</p> -->
      <!-- <p v-if="movie.adult">{{ movie.adult }}</p>
      <p v-if="movie.backdrop_path">{{ movie.backdrop_path }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.id">{{ movie.belongs_to_collection.id }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.name">{{ movie.belongs_to_collection.name }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.poster_path">{{ movie.belongs_to_collection.poster_path }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.backdrop_path">{{ movie.belongs_to_collection.backdrop_path }}</p>
      <p v-if="movie.budget">{{ movie.budget }}</p>
      <p v-if="movie.genres && movie.genres.length > 0">{{ movie.genres }}</p>
      <p v-if="movie.homepage">{{ movie.homepage }}</p>
      <p v-if="movie.id">{{ movie.id }}</p>
      <p v-if="movie.imdb_id">{{ movie.imdb_id }}</p>
      <p v-if="movie.original_language">{{ movie.original_language }}</p>
      <p v-if="movie.original_title">{{ movie.original_title }}</p>
      <p v-if="movie.overview">{{ movie.overview }}</p>
      <p v-if="movie.popularity">{{ movie.popularity }}</p>
      <p v-if="movie.poster_path">{{ movie.poster_path }}</p>
      <p v-if="movie.production_companies && movie.production_companies.length > 0">{{ movie.production_companies }}</p>
      <p v-if="movie.production_countries && movie.production_countries.length > 0">{{ movie.production_countries }}</p>
      <p v-if="movie.release_date">{{ movie.release_date }}</p>
      <p v-if="movie.revenue">{{ movie.revenue }}</p>
      <p v-if="movie.runtime">{{ movie.runtime }}</p>
      <p v-if="movie.spoken_languages && movie.spoken_languages.length > 0">{{ movie.spoken_languages }}</p>
      <p v-if="movie.status">{{ movie.status }}</p>
      <p v-if="movie.tagline">{{ movie.tagline }}</p>
      <p v-if="movie.video">{{ movie.video }}</p>
      <p v-if="movie.vote_average">{{ movie.vote_average }}</p>
      <p v-if="movie.vote_count">{{ movie.vote_count }}</p> -->



  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'MovieDetailView',
  data(){
    return{
      movie: null,
      movieId: null,
    }
  },
  
  created() {
    this.movieId = this.$route.params.movie_id;
    this.getMovieDetail()
  },
  
  methods:{
    getMovieDetail() {
      const movieId = this.movieId
      axios({
          method:'get',
          url: `${API_URL}/movies/get/movie_detail/${movieId}/`,
        })
        .then((res) => {
          this.movie = res.data
        })
        .catch(err => console.log(err))
    },
    getMoviePoster() {
      if(this.movie.poster_path) {
        return "https://image.tmdb.org/t/p/w200" + this.movie.poster_path
      } else {
        return "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
      }
    }   
  }
}
</script>

<style>
.movie-detail-container{
  background:#ffffff;
  color:#000000;
  width: auto;
  height: auto;
}

</style>