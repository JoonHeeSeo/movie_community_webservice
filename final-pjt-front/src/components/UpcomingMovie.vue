<template>
  <div>
    <div classs="main-container">
      <div class="poster-container">
        <img :src="getMoviePoster()" alt="movie_post" class="poster">
        <div class="ticket-container">
          <div class="ticket-content">
            <p class="ticket-movie-title">{{ upcoming.title }}</p>
            <p class="ticket-movie-vote">Release date: {{ upcoming.release_date }}</p>

            <!-- <button class="like-btn" @click.prevent="likeMovie(upcoming.id)">
              <span v-if="likeMoviesId.includes(upcoming.id)">❤️</span>
              <span v-else>🤍</span>
            </button> -->

            <router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: upcoming.id }}">
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
  name:'UpcomingMovie',
  props: {
    upcoming: Object,
  },
  data(){
    return {
      likeMoviesId : this.$store.state.likeMoviesId
    }
  },
  methods: {
    getMoviePoster() {
      return "https://image.tmdb.org/t/p/w200" + this.upcoming.poster_path
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