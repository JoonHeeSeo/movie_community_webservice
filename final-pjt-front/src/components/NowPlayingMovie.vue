<template>
  <div>
    <div classs="main-container">
      <div class="poster-container">
        <img :src="getMoviePoster()" alt="movie_post" class="poster">
        <div class="ticket-container">
          <div class="ticket-content">
            <p class="ticket-movie-title">{{ nowplaying.title }}</p>
            <p class="ticket-movie-vote">Rate: {{ nowplaying.vote_average }}</p>
            <button class="like-btn" @click="toggleHeart()">
              {{  isActive ? '❤️' : '🤍' }}
            </button>
            
            <router-link :to="{ name: 'moviedetail', params: { movie_id: nowplaying.movie_id }}">
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
  name:'NowPlayingMovie',
  props: {
    nowplaying: Object,
  },
  data(){
    return {
      isActive: false
    }
  },
  methods: {
    getMoviePoster() {
      if(this.nowplaying.poster_path) {
        return "https://image.tmdb.org/t/p/w200" + this.nowplaying.poster_path
      } else {
        return "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
      }
    },
    toggleHeart() {
      this.isActive = !this.isActive
    }
  }
}
</script>

<style>
</style>