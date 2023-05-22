<template>
  <div class="movie-list">
    <h3 class="list-name"> 평점 높은 순 </h3>
    <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
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
  /* text-align: start; */
  margin: auto;
  display: flex;
  overscroll-behavior: auto;
}

@keyframes circleMovement {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}

.list-name {
  margin-top:20px;
  margin-left: 20px;
  text-align: left;
  color: #000;;
  background: #fff;
  height: 125px;
}
</style>