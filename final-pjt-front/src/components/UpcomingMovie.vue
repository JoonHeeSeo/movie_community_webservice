<template>
  <div>
    <div classs="main-container">
      <div class="poster-container">
        <img :src="getMoviePoster()" alt="movie_post" class="poster">
        <div class="ticket-container">
          <div class="ticket-content">
            <p class="ticket-movie-title">{{ upcoming.title }}</p>
            <p class="ticket-movie-vote">Release date: {{ upcoming.release_date }}</p>
            <button class="like-btn" @click="toggleHeart()">
              {{  isActive ? '❤️' : '🤍' }}
            </button>
            <router-link :to="{ name: 'moviedetail', params: { movie_id: upcoming.movie_id }}">
            <button class="ticket-detail-btn">자세히 보기</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'UpcomingMovie',
  props: {
    upcoming: Object,
  },
  data(){
    return {
      isActive: false
    }
  },
  methods: {
    getMoviePoster() {
      return "https://image.tmdb.org/t/p/w200" + this.upcoming.poster_path
    },
    
    toggleHeart() {
      this.isActive = !this.isActive
    }
  }
}
</script>

<style>

</style>