<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title">
      <br><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      <br>
      <input type="submit" id="submit">
    </form>
  </div>

</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleUpdateView',
  data() {
    return {
      title: null,
      content: null,

    }
  },
  methods: {
    updateArticle() {
      const title = this.title
      const content = this.content
      const articleId = this.$route.params.id

      axios({
        method: 'put',
        url: `${API_URL}/articles/${articleId}/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({ name: 'article/:id' });
      })
      .catch((err => {
        console.log(err)
      }))
    },

    getArticle(articleId) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((response) => {
        const article = response.data
        this.title = article.title
        this.content = article.content
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  
  mounted() {
    const articleId = this.$route.params.id
    this.getArticle(articleId)
  },
  
}
</script>

<style>

</style>