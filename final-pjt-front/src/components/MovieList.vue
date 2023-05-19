<template>
  <div class="movie-list">
    <h1>
      <MovieListItem
      v-for="movie in movies" :key="movie.id" :movie="movie"
      />
      <div id="card-container">
      </div>
      <div id="loader">
        <div class="skleton-card"></div>
        <div class="skleton-card"></div>
        <div class="skleton-card"></div>
        <div class="skleton-card"></div>
      </div>
      <div class="card-actions">
        <span> Showing
          <span id="card-count"></span> of
          <span id="card-total"></span> cards
        </span>
      </div>
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
#card-container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  height: 55vh;
  width: cals(100% / 3) -16px;
  margin: 8px
}
</style>