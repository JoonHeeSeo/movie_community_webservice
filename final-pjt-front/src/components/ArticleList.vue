<template>
  <div>
    <h1>ArticlesList</h1>
    <hr>

    <div v-for="article in articles" :key="article.id">
      <p> 제목: 
      <router-link :to="{ name: 'article/:id', params: { id: article.id } }">{{ article.title }}</router-link>
      </p>
      <p>글 번호: {{ article.id }}</p>
      <p>내용: {{ article.content }}</p>
      <p>작성자: {{ article.username }}</p>
      <p>{{ article.like_users.length }}명이 좋아합니다.</p>
      
      <form @submit.prevent="likeArticle(article.id)">
        <input type="submit" :value="checkLikeArticle(article) ? 'Like Cancel' : 'Like'">
      </form>
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

</style>