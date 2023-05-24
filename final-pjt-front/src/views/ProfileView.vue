<template>
  <div>
    <h1>{{ username }}님의 Profile</h1>
    <hr>


    <p>작성한 글</p>
    <div v-if="articles.length > 0">
      <div v-for="article in articles" :key="article.id">
        <p>{{ article.id }}번 글 :
        <router-link :to="{ name: 'article/:id', params: { id: article.id } }">{{ article.title }}</router-link></p>
        
      </div>
    </div>
    <div v-else>
      <p>작성한 글이 없습니다.</p>
    </div>
    <hr>
    

    <p>글에 작성한 댓글</p>
    <div v-if="articleComments.length > 0">
      <div v-for="comment in articleComments" :key="comment.id">
        <p><router-link :to="{ name: 'article/:id', params: { id: comment.article } }">{{ comment.article }}</router-link>
        번 글에 단 댓글: {{ comment.content }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성한 댓글이 없습니다.</p>
    </div>
    <hr>


    <p>영화에 작성한 댓글</p>
    <div v-if="movieComments.length > 0">
      <div v-for="comment in movieComments" :key="comment.id">
        <p><router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: comment.movie_id } }">
            {{ comment.movie_id }}</router-link>
          번 영화에 단 댓글: {{ comment.content }}</p>
      </div>
    </div>
    <div v-else>
      <p>작성한 댓글이 없습니다.</p>
    </div>
    <hr>


    <p>좋아요 누른 영화</p>
    <div v-if="movies.length > 0">
      <div v-for="movie in movies" :key="movie">
        <li><router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.movie_id } }">{{ movie.title }}</router-link></li>
      </div>
    </div>
    <div v-else>
      <p>좋아요를 누른 영화가 없습니다.</p>
    </div>
    <hr>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      username: null,
      articles: [],
      articleComments: [],
      movies: [],
      movieComments: [],
    }
  },

  mounted() {
    this.username = this.$route.params.username
  },

  created() {
    this.getArticleProfile()
    this.getMovieProfile()
  },

  methods: {
    getArticleProfile() {
      const username = this.$route.params.username

      axios({
        method: 'get',
        url: `${API_URL}/articles/profile/${username}`,
        data: { username },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.articles = res.data.articles
          this.articleComments = res.data.comments
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getMovieProfile() {
      const username = this.$route.params.username

      axios({
        method: 'get',
        url: `${API_URL}/movies/profile/${username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.movies = res.data.movies
          this.movieComments = res.data.comments
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },



}
</script>

<style>

</style>