<template>
  <div class="article-list-container">
    <div v-for="article in articles" :key="article.id" class="article-container">
      <div class="article-top-part">
        <router-link :to="{ name: 'article/:id', params: { id: article.id } }">{{ article.title }}</router-link>
        <span class="article-writer">작성자: <router-link :to="{ name: 'profile/:username', params: { username: article.username } }">{{ article.username }}</router-link></span>
      </div>
      <!-- <p>글 번호: {{ article.id }}</p> -->
      <p class="article-content">{{ article.content }}</p>
      <div class="article-like">
        <span>{{ article.like_users.length }}명이 좋아합니다</span>
        <button @click="likeArticle(article.id)" class="article-like-btn">
          {{ checkLikeArticle(article) ? '❤️' : '🤍' }}
        </button>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleList',
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
  methods: {
    likeArticle(articleId) {
      axios({
        method: 'post',
        url: `${API_URL}/articles/${articleId}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // 새로고침..
        location.reload()
      })
      .catch((err => {
        console.log(err)
      }))
    },

  checkLikeArticle(article) {
    const currentUserIdx = this.$store.state.useridx
      return article.like_users.includes(currentUserIdx)
    },
  }
}
</script>

<style>
/* 게시글 좋아요 버튼 */
.article-like-btn{
  font-size: 20px;
  border: none;
  background: none;
  cursor: pointer;
  position: static;
  margin:0px 10px 10px 10px;
}
.article-like-btn:hover {
  color:#fff
}
.article-like-btn:active {
  transform: translateY(4px);
}

/* 게시글 형태 꾸미는 작업 */
.article-list-container{
  margin-left: 30px;
  color:black;
}
.article-container {
  margin-top: 20px;
}
.article-top-part {
  font-size:30px;
  font-weight:bold;
}
.article-writer {
  margin-left:30px;
  font-size: 15px;
}
.article-content {
  margin-top: 20px;
}
.article-like {
  color:#fff;
  display: flex;
  margin-top:20px;
  justify-content: right;
}

</style>