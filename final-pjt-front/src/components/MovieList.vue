<template>
  <div class="movie-list" id="movieList">
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
  },
  mounted(){
    const movieList = document.getElementById("movieList");
    movieList.addEventListener('mousemove', (event) => {
      const mouseX = event.clientX;
      const containerWidth = movieList.offsetWidth;
      const speed = ((containerWidth/2) - mouseX ) * 10; // Adjust the speed factor as needed
      console.log(speed)
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

.list-name {
  margin-top:20px;
  margin-left: 20px;
  text-align: left;
  color: #000;;
  height: 125px;
}
</style>