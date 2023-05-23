<template>
  <div>
    <div class="commentcreate-container">
      <h1 style="color:black; margin:20px; position: relative flex-basis:fill;">게시글 작성</h1>
      <form @submit.prevent="createArticle">
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title">
        <br><br>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
        <br>
        <input type="submit" id="submit">
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
.commentcreate-container{
  display: flex;
  flex-flow: wrap;
  width: auto;
  height: auto;
  border: solid white 1px;
  flex-basis: 'content';

}

</style>