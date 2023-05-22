<template>
  <div>
    <h1>MovieDetailView</h1>
      <br>
      <!-- <p>{{ movie }}</p> -->

      <p>{{ movie.adult }}</p>
      <p>{{ movie.backdrop_path }}</p>
      <p>{{ movie.belongs_to_collection.id }}</p>
      <p>{{ movie.belongs_to_collection.name }}</p>
      <p>{{ movie.belongs_to_collection.poster_path }}</p>
      <p>{{ movie.belongs_to_collection.backdrop_path }}</p>
      <p>{{ movie.budget }}</p>
      <p>{{ movie.genres }}</p>
      <p>{{ movie.homepage }}</p>
      <p>{{ movie.id }}</p>
      <p>{{ movie.imdb_id }}</p>
      <p>{{ movie.original_language }}</p>
      <p>{{ movie.original_title }}</p>
      <p>{{ movie.overview }}</p>
      <p>{{ movie.popularity }}</p>
      <p>{{ movie.poster_path }}</p>
      <p>{{ movie.production_companies }}</p>
      <p>{{ movie.production_countries }}</p>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.revenue }}</p>
      <p>{{ movie.runtime }}</p>
      <p>{{ movie.spoken_languages }}</p>
      <p>{{ movie.status }}</p>
      <p>{{ movie.tagline }}</p>
      <p>{{ movie.title }}</p>
      <p>{{ movie.video }}</p>
      <p>{{ movie.vote_average }}</p>
      <p>{{ movie.vote_count }}</p>


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
          console.log(res)
        })
        .catch(err => console.log(err))
    },   
  }
}
</script>

<style>

</style>