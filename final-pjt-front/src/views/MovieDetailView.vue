<template>
  <div>
    <div class="movie-detail-container" style="display:flex; padding: 20px; justify-content:center;">
      <img :src="getMoviePoster()" alt="movie_post" class="detail-poster">
      <div style="width:700px">
        <h1 v-if="movie.title" class="detail-title">{{ movie.title }}</h1>
        <span v-if="movie.original_title">({{ movie.original_title }})</span>
        <b v-if="movie.vote_average" style="float:right;">평점: ⭐{{ movie.vote_average }}</b>
        <br>
        <div>
          <span v-if="movie.runtime" class="detail-movie-time">상영시간: {{ movie.runtime }}분</span>
          <span v-if="movie.genres && movie.genres.length > 0" class="detail-movie-time">
            장르: 
            <span v-for="(genre, idx) in movie.genres" :key="{idx}" style="margin-left:7px;">
              {{ genre.name }}
            </span>
          </span>
        </div>
        
        <h2 style="margin:15px 0">요약
          <button class="movie-like-btn" @click.prevent="likeMovie(movie.id)">
            <span v-if="likeMoviesId.includes(movie.id)">❤️</span>
            <span v-else>🤍</span>
          </button>
        </h2>
        <hr style="border: solid black 1px">
        <p v-if="movie.overview" class="detail-overview">{{ movie.overview }}</p>
      </div>
    </div>

    <div class="detail-comment-container">
      <div>
        <h1>Comment</h1>
        <hr>
      </div>
      <div>
        <form @submit.prevent="createMovieComment" style="display=flex; justify-content:space-between;">
          <textarea id="comment" cols="80" rows="auto" v-model="movieComment" placeholder="댓글을 입력하세요."></textarea>
          <input type="submit" id="submit" style="margin-right: auto;" value="작성">
          <br>
        </form>
      </div>
      <div>
        <ul>
          <li v-for="comment in movieComments" :key="comment.id" style="display:flex; justify-content:end; border:solid 1px #fff; margin:10px; padding:10px; width: 600px;">
            <p style="margin-right: auto; marigin-left:5px;">{{ comment.content }}</p>
            <p style="font-size:5px; margin-right:10px; color:#fff;">작성자 : 
              <router-link :to="{ name: 'profile/:username', params: { username: comment.user } }">{{ comment.user }}</router-link>
              <!-- 작성 시간 : {{ comment.created_at }} -->
            </p>
            <!-- <p>댓글 수정 시간 : {{ comment.updated_at }}</p> -->
            <form @submit.prevent="deleteMovieComment(comment.id)">
            <input type="submit" value="DELETE" style="align-self: end;"></form>
            <!-- <router-link :to="{name : 'article/:id/comment/:commentid/update', params: {id: articleDetail.id, commentid: comment.id}}">[UPDATE]</router-link> -->
          </li>
        </ul>
      </div>
    </div>
    <div style="display:flex; justify-content:center; align-items: center; margin-top: 20px; ">
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
      likeMoviesId : [],
    }
  },
  
  created() {
    this.movieId = this.$route.params.movie_id;
    this.getMovieDetail()
    this.getMovieComments()
    this.getLikeMovie(this.movieId)
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
    
    getLikeMovie(movieId) {
      axios({
        method: 'get',
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
.movie-detail-container{
  color:#000000;
  width: auto;
  height: auto;
  flex-wrap: wrap;

}
.detail-poster {
  height: 500px;
  width: 300px;
  margin: 20px;
}
.detail-title{
  margin-top:20px;
  font-size: 50px;
  width: 700px;
  font-weight:bold;
}
.detail-movie-time{
  font-size: 15px;
  display: flex;
  color: #4d454b;
  justify-content: left;

}
.detail-overview{
  margin-top: 20px;
  font-size: 20px;
}
/* 좋아요 버튼 */
.movie-like-btn{
  font-size: 30px;
  border: none;
  background: none;
  cursor: pointer;
  float:right;
  margin-right:auto;
}
.movive-like-btn:hover {
  color:#fff
}
.movie-like-btn:active {
  transform: translateY(4px);
}

/* comment */
.detail-comment-container{
  display:flex;
  flex-direction: column;
  align-items: center;
  width:auto;
  padding:20px;
  height:auto;
  color:black;
}
</style>
