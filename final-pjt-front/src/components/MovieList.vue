<template>
  <div>
    <h3 style="margin-top:90px; color:#000000; margin-left:30px">Top Rated</h3>
    <div class="movie-list" id="movieList">
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
    <hr style="border: solid 1px white;">
    <h3 style="margin-top:20px; color:#000000; margin-left:30px">Now Playing</h3>
    <div class="nowplaying-list" id="nowplayingList">
      <NowPlaying/>
      <NowPlaying v-for="nowplaying in nowplayings" :key="nowplaying.id" :nowplaying="nowplaying"/>
    </div>
    <hr style="border: solid 1px white;">
    <h3 style="margin-top:20px; color:#000000; margin-left:30px">Upcoming</h3>
    <div class="upcoming-list" id="upcomingList">
      <UpComing v-for="upcoming in upcomings" :key="upcoming.id" :upcoming="upcoming"/>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';
import NowPlaying from '@/components/NowPlayingMovie.vue';
import UpComing from '@/components/UpcomingMovie.vue';

export default {
  name:'MovieList',
  components: {
    MovieListItem,
    NowPlaying,
    UpComing,
  },
  computed:{
    movies() {
      return this.$store.state.movies
    },
    nowplayings() {
      return this.$store.state.nowplayings
    },
    upcomings() {
      return this.$store.state.upcomings
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
    const nowplayingList = document.getElementById("nowplayingList");
    nowplayingList.addEventListener('mousemove', (event) => {
      const mouseX = event.clientX;
      const containerWidth = movieList.offsetWidth;
      const speed = ((containerWidth/2) - mouseX ) * 10; // Adjust the speed factor as needed
      nowplayingList.style.transform = `translateX(${speed}%)`;
      });
      nowplayingList.addEventListener('mouseleave', () => {
        nowplayingList.style.transform = "translateX(0)";
        });
    
    const upcomingList = document.getElementById("upcomingList");
    upcomingList.addEventListener('mousemove', (event) => {
      const mouseX = event.clientX;
      const containerWidth = movieList.offsetWidth;
      const speed = ((containerWidth/2) - mouseX ) * 10; // Adjust the speed factor as needed
      upcomingList.style.transform = `translateX(${speed}%)`;
      });
      upcomingList.addEventListener('mouseleave', () => {
        upcomingList.style.transform = "translateX(0)";
        });
        
  }
}
</script>

<style>
.movie-list {
  /* text-align: start; */
  margin: auto;
  display: flex;
  transition: transform 120s ease;
}


.movie-list:hover {
  transform: translateX(-10000%)
}

.nowplaying-list {
  margin: auto;
  display: flex;
  transition: transform 120s ease;
}
.nowplaying-list:hover {
  transform: translateX(-10000%)
}

.upcoming-list {
  margin: auto;
  display: flex;
  /* overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory; */
  transition: transform 120s ease;
}
.upcoming-list:hover {
  transform: translateX(-10000%)
}
</style>