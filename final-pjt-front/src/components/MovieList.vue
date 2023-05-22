<template>
  <div class="movie-list">
    <h1>
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </h1>
    
    
    <div id="card-container">
      <div id="loader">
        <div class="skleton-card">1</div>
        <div class="skleton-card">2</div>
        <div class="skleton-card">3</div>
        <div class="skleton-card">4</div>
      </div>
      <div class="card-actions">
        <span> Showing
        <span id="card-count"></span> of
        <span id="card-total"></span> cards
        </span>
      </div>
    </div>
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
  width: calc((100% / 3) -16px);
  margin: 8px;
  border-radius: 3px;
  transition: all 200ms ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
.card-actions {
  margin:8px;
  padding: 16px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#loader {
  display: flex;
}

.skeleton-card{
  height: 55vh;
  width: cals(100% / 3) -16px;
  margin: 8px;
  border-radius: 3px;
  transition: all 200ms ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media screen and (prefers-reduced-motion: reduce){

}


</style>