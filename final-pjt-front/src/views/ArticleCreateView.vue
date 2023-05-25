<template>
  <div style="position: relative; margin-left:40%">
    <div>
      <h3 style="margin:80px 0px 20px 20px; color:black;">게시글 작성</h3>
      <form @submit.prevent="createArticle" class="article-create-container">
        <label for="title" style="font-weight:bold; margin-bottom: 10px;">제목</label>
        <input type="text" id="title" v-model.trim="title">
        <br><br>
        <label for="content" style="font-weight:bold; margin-bottom: 10px;">내용</label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <input style="margin-left:auto; margin-top:20px;" type="submit" id="submit" class="article-submit-btn">
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
  padding:20px;
}
.article-submit-btn{
  border: 1px solid #fff;
  background: none;
  cursor: pointer;
  /* margin-left: 25%; */
  height: 30px;
  width: 50px;
}
.article-submit-btn:hover{
  background:#fff;
}
</style>