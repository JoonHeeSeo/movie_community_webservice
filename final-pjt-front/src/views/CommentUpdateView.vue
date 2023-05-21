<template>
  <div>
    <h1>댓글 수정</h1>
    <form @submit.prevent="updateComment">
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
  name: 'CommentUpdateView',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    updateComment() {
      const content = this.content
      const commentId = this.$route.params.commentid

      axios({
        method: 'put',
        url: `${API_URL}/articles/comments/${commentId}/`,
        data: { content },
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


    getComment(commentId) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((response) => {
        const comment = response.data
        console.log(comment)
        this.content = comment.content
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  
  // mounted가 getComment보다 밑에 있어야해
  mounted() {
    const commentId = this.$route.params.commentid
    this.getComment(commentId)
  },    

  
}
</script>

<style>

</style>