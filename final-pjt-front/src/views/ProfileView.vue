<template>
  <div>

    <h1 style="margin:80px 0px 0px 30px; color:black;">{{ username }}님의 프로필</h1>

    <div v-if="currentusername">
      <button @click="logOut" style="background: none; color:white; justify-self: end; border:solid white 1px; padding:10px; margin-left:90%; cursor:pointer;">SIGN OUT</button>
    </div>

    <div class="profile-detail">
      
      <div class="profile-article">
        <h3>작성한 글</h3>
        <hr style="border: 1px solid #fff; margin-top:10px">
        <div v-if="articles.length > 0" style="margin-top:10px;">
          <div v-for="article in articles" :key="article.id">
            <p>{{ article.id }}번 글 :
            <router-link :to="{ name: 'article/:id', params: { id: article.id } }">{{ article.title }}</router-link></p>
          </div>
        </div>
        <div v-else>
          <p style="color:#fff; margin-top:10px;">글이 없습니다.</p>
        </div>
      </div>

      <div class="profile-articlecomment">
        <h3>글에 작성한 댓글</h3>
        <hr style="border: 1px solid #fff; margin-top:10px">
        <div v-if="articleComments.length > 0">
          <div v-for="comment in articleComments" :key="comment.id" style="margin-top:10px;">
            <p><router-link :to="{ name: 'article/:id', params: { id: comment.article } }">{{ comment.article }}</router-link>
            번 글에 단 댓글: {{ comment.content }}</p>
          </div>
        </div>
        <div v-else>
          <p style="color:#fff; margin-top:10px;">작성한 댓글이 없습니다.</p>
        </div>
      </div>

      <div class="profile-moviecomment">
        <h3>영화에 작성한 댓글</h3>
        <hr style="border: 1px solid #fff; margin-top:10px">
        <div v-if="movieComments.length > 0">
          <div v-for="comment in movieComments" :key="comment.id" style="margin-top:10px;">
            <p><router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: comment.movie_id } }">
                {{ comment.movie_id }}</router-link>
              번 영화에 단 댓글: {{ comment.content }}</p>
          </div>
        </div>
        <div v-else>
          <p>작성한 댓글이 없습니다.</p>
        </div>
      </div>

      <div class="profile-movielist">
        <h3>좋아요를 누른 영화</h3>
        <hr style="border: 1px solid #fff; margin-top:10px">
        <div v-if="movies.length > 0">
          <div v-for="movie in movies" :key="movie" style="margin-top:10px;">
            <li><router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.movie_id } }">{{ movie.title }}</router-link></li>
          </div>
        </div>
        <div v-else style="margin-top:10px; color:#fff;">
          <p>좋아요를 누른 영화가 없습니다.</p>
        </div>
      </div>

    </div>





    <!-- <h1>{{ username }}님의 Profile</h1>
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
    </div> -->

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

  computed: {
    currentusername() {
      return this.$store.state.username
    },
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

    logOut() {
      const token = this.$store.state.token
      this.$store.dispatch('logOut', token)
    },
  },



}
</script>

<style>
.profile-detail{
  display: flex;
  flex-direction: column;
  margin: 20px;
  padding: 10px;
  color:black;
}
.profile-articlecomment{
  margin-top:20px;
}
.profile-moviecomment{
  margin-top:20px;
}
.profile-movielist{
  margin-top:20px;
}

</style>