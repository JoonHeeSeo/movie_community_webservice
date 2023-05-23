<template>
  <div>
    <h1>MovieDetailView</h1>
    <div class="movie-detail-container" style="display:flex; ">
      <img :src="getMoviePoster()" alt="movie_post" class="detail-poster">
      <div >
        <p v-if="movie.title">제목: {{ movie.title }} </p>

      </div>
      <p v-if="movie.original_title">오리지날 제목: {{ movie.original_title }}</p>
      <p v-if="movie.vote_average">평점: {{ movie.vote_average }}</p>
      
      <p v-if="movie.genres && movie.genres.length > 0">장르: 
        <span v-for="genre in movie.genres" :key="genre.id">
          {{ genre.name }}
          <span v-if="!$last">, </span>
        </span></p>
      <p v-if="movie.overview">요약: {{ movie.overview }}</p>
      
      <p v-if="movie.runtime">상영시간: {{ movie.runtime }}분</p>
      <p v-if="movie.video">{{ movie.video }}</p>
      
      <p v-if="movie.backdrop_path">{{ movie.backdrop_path }}</p>

    </div>

    <br>
    <hr>

    <div>
      <h1>Comments</h1>
      <hr>

      <div v-for="comment in movieComments" :key="comment.id">
        <p>댓글 작성자 : <router-link :to="{ name: 'profile/:username', params: { username: comment.user } }">{{ comment.user }}</router-link></p>
        <p>댓글 내용 : {{ comment.content }}</p>
        <p>댓글 작성 시간 : {{ comment.created_at }}</p>
        <!-- <p>댓글 수정 시간 : {{ comment.updated_at }}</p> -->
        <form @submit.prevent="deleteMovieComment(comment.id)">
        <input type="submit" value="DELETE"></form>

        <!-- <router-link :to="{name : 'article/:id/comment/:commentid/update', params: {id: articleDetail.id, commentid: comment.id}}">[UPDATE]</router-link> -->

        <hr>
      </div>

      <form @submit.prevent="createMovieComment">
        <label for="comment">댓글 내용 : </label>
        <textarea id="comment" cols="30" rows="10" v-model="movieComment"></textarea>
        <br>
        <input type="submit" id="submit">
      </form>

    </div>


      <!-- <p>{{ movie }}</p> -->
      <!-- <p v-if="movie.adult">{{ movie.adult }}</p>
      <p v-if="movie.backdrop_path">{{ movie.backdrop_path }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.id">{{ movie.belongs_to_collection.id }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.name">{{ movie.belongs_to_collection.name }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.poster_path">{{ movie.belongs_to_collection.poster_path }}</p>
      <p v-if="movie.belongs_to_collection && movie.belongs_to_collection.backdrop_path">{{ movie.belongs_to_collection.backdrop_path }}</p>
      <p v-if="movie.budget">{{ movie.budget }}</p>
      <p v-if="movie.genres && movie.genres.length > 0">{{ movie.genres }}</p>
      <p v-if="movie.homepage">{{ movie.homepage }}</p>
      <p v-if="movie.id">{{ movie.id }}</p>
      <p v-if="movie.imdb_id">{{ movie.imdb_id }}</p>
      <p v-if="movie.original_language">{{ movie.original_language }}</p>
      <p v-if="movie.original_title">{{ movie.original_title }}</p>
      <p v-if="movie.overview">{{ movie.overview }}</p>
      <p v-if="movie.popularity">{{ movie.popularity }}</p>
      <p v-if="movie.poster_path">{{ movie.poster_path }}</p>
      <p v-if="movie.production_companies && movie.production_companies.length > 0">{{ movie.production_companies }}</p>
      <p v-if="movie.production_countries && movie.production_countries.length > 0">{{ movie.production_countries }}</p>
      <p v-if="movie.release_date">{{ movie.release_date }}</p>
      <p v-if="movie.revenue">{{ movie.revenue }}</p>
      <p v-if="movie.runtime">{{ movie.runtime }}</p>
      <p v-if="movie.spoken_languages && movie.spoken_languages.length > 0">{{ movie.spoken_languages }}</p>
      <p v-if="movie.status">{{ movie.status }}</p>
      <p v-if="movie.tagline">{{ movie.tagline }}</p>
      <p v-if="movie.video">{{ movie.video }}</p>
      <p v-if="movie.vote_average">{{ movie.vote_average }}</p>
      <p v-if="movie.vote_count">{{ movie.vote_count }}</p> -->



  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'MovieDetailView',
  data(){
    return{
      movie: null,
      movieId: null,
      movieComment: null,
      movieComments: [],
    }
  },
  
  created() {
    this.movieId = this.$route.params.movie_id;
    this.getMovieDetail()
    this.getMovieComments()
  },
  
  methods:{
    getMovieDetail() {
      const movieId = this.movieId
      axios({
          method:'get',
          url: `${API_URL}/movies/get/movie_detail/${movieId}/`,
        })
        .then((res) => {
          this.movie = res.data
        })
        .catch(err => console.log(err))
    },

    getMovieComments() {
      const movieId = this.movieId

      axios({
        method: 'get',
        url: `${API_URL}/movies/${movieId}/comments/get/`,
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`
        // }
      })
      .then((res) => {
        this.movieComments = res.data
        console.log(res.data)
      })
      .catch((err => {
        console.log(err)
      }))
    },

    getMoviePoster() {
      if(this.movie.poster_path) {
        return "https://image.tmdb.org/t/p/w200" + this.movie.poster_path
      } else {
        return "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
      }
    },

    createMovieComment() {
      const content = this.movieComment
      const movieId = this.movieId

      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/comments/create/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // 새로고침
        location.reload()
      })
      .catch((err => {
        console.log(err)
      }))
    },

    deleteMovieComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // 새로고침
        location.reload()
      })
      .catch((err => {
        console.log(err)
      }))
    },

  }
}
</script>

<style>
.movie-detail-container {
  background: #ffffff;
  color: #000000;
  width: auto;
  height: auto;
  padding: 20px;
}

.movie-detail-container p {
  margin: 10px 0;
}

.movie-detail-container img {
  max-width: 200px;
  height: auto;
  margin-right: 20px;
}

.movie-detail-container hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 20px 0;
}
</style>
