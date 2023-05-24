<template>
  <div style="position: relative; margin-left:40%">
    <div class="article-create-container">
      <h3 style="margin:0px 0px 20px 20px;">게시글 작성</h3>
      <form @submit.prevent="createArticle">
        <label for="title" style="margin-left:20px; font-weight:bold;">제목: </label>
        <input type="text" id="title" v-model.trim="title">
        <br><br>
        <label for="content" style="margin-left: 20px; font-weight:bold;">내용: </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <input type="submit" id="submit" class="article-submit-btn">
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({ name : 'community' })
      })
      .catch((err => {
        console.log(err)
      }))
    }
  }
}
</script>

<style>
.article-create-container{
  display: flex;
  flex-direction: column;
  border: solid white 1px;
  border-radius: 4px;
  color:black;
  width:500px;
  height:300px;
  justify-content: center;
  margin-top:20px;
}
.article-submit-btn{
  border: 1px solid #fff;
  background: none;
  cursor: pointer;
  margin-left: 25%;
  height: 30px;
  width: 50px;
}
.article-submit-btn:hover{
  background:#fff;
}
</style>