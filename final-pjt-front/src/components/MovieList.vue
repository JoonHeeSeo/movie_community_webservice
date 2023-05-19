<template>
  <div class="movie-list">
    <h1>
      <MovieListItem
      v-for="movie in movies" :key="movie.id" :movie="movie"
      />
    </h1>


  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';

export default {
  name:'MovieList',
  components: {
    MovieListItem,
  },
  computed:{
    movies() {
      return this.$store.state.movies
    }
  }
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>