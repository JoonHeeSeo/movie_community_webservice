<template>
  <div style="position: relative; margin-left:40%">
    <div>
      <h3 style="margin:80px 0px 20px 20px; color:black;">게시글 수정</h3>
      <form @submit.prevent="updateArticle" class="article-update-container">
        <label for="title" style="font-weight:bold; margin-bottom: 10px;">제목 : </label>
        <input type="text" id="title" v-model.trim="title">
        <br><br>
        <label for="content" style="font-weight:bold; margin-bottom: 10px;">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <input style="margin-left:auto; margin-top:20px;" type="submit" id="submit">
        <br>
      </form>
    </div>
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

  // mounted가 getArticle보다 밑에 있어야해
  mounted() {
    const articleId = this.$route.params.id
    this.getArticle(articleId)
  },
  
}
</script>

<style>
.article-update-container{
  display: flex;
  flex-direction: column;
  border: solid white 1px;
  border-radius: 4px;
  color:black;
  width:500px;
  height:300px;
  justify-content: center;
  margin-top:20px;
  padding:20px;
}
.article-update-submit-btn{
  border: 1px solid #fff;
  background: none;
  cursor: pointer;
  height: 30px;
  width: 50px;
}
.article-update-submit-btn:hover{
  background:#fff;
}
</style>