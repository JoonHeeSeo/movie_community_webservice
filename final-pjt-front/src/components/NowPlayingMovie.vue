<template>
  <div>
    <div classs="main-container">
      <div class="poster-container">
        <img :src="getMoviePoster()" alt="movie_post" class="poster">
        <div class="ticket-container">
          <div class="ticket-content">
            <p class="ticket-movie-title">{{ nowplaying.title }}</p>
            <p class="ticket-movie-vote">Rate: {{ nowplaying.vote_average }}</p>

            <button class="like-btn" @click.prevent="likeMovie(nowplaying.id)">
              <span v-if="likeMoviesId.includes(nowplaying.id)">❤️</span>
              <span v-else>🤍</span>
            </button>
            
            <router-link :to="{ name: 'moviedetail', params: { movie_id: nowplaying.movie_id }}">
            <button class="ticket-detail-btn">자세히 보기</button></router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'NowPlayingMovie',
  props: {
    nowplaying: Object,
  },
  data(){
    return {
      likeMoviesId : this.$store.state.likeMoviesId
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

    likeMovie(movieId) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.likeMoviesId = res.data
        console.log(res.data)
      })
      .catch((err => {
        console.log(err)
      }))
    },

  }
}
</script>

<style>
</style>