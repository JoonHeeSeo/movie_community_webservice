<template>
  <div>
    <h3 style="margin-top:90px; color:#000000; margin-left:30px">Top Rated</h3>
    <div class="movie-list" id="movieList">
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
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
  },
  mounted(){
    const movieList = document.getElementById("movieList");
    movieList.addEventListener('mousemove', (event) => {
      const mouseX = event.clientX;
      const containerWidth = movieList.offsetWidth;
      const speed = ((containerWidth/2) - mouseX ) * 10; // Adjust the speed factor as needed
      movieList.style.transform = `translateX(${speed}%)`;
      });
      movieList.addEventListener('mouseleave', () => {
        movieList.style.transform = "translateX(0)";
        });
        
  }
}
</script>

<style>
.movie-list {
  /* text-align: start; */
  margin: auto;
  display: flex;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  transition: transform 120s ease;
}


.movie-list:hover {
  transform: translateX(-10000%)
}

</style>