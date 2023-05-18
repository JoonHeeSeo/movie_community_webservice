<template>
  <div>
    <p>
      <img :src="getMoviePoster()" alt="movie_post">
      <br>{{  movie.title  }}  
      rate: {{  movie.vote_average }}
    </p>
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props: {
    movie: Object,
  },
  methods: {
    getMoviePoster() {
      return "https://image.tmdb.org/t/p/w200" + this.movie.poster_path
    }
  }
}
</script>

<style>

</style>