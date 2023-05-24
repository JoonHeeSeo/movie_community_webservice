<template>
  <div>

    <h3 style="color:#000000; margin-top:20px;">댓글 작성</h3>
    <form @submit.prevent="createComment">
      <label for="comment">댓글 내용 : </label>
      <textarea id="comment" cols="30" rows="1" v-model="comment"></textarea>
      <button @click="submit">제출</button>
    </form>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentCreate',
  props : [ 'articleId' ],
  data() {
    return {
      comment: null,
    }
  },
  methods: {
    createComment() {
      const content = this.comment
      const articleId = this.articleId

      axios({
        method: 'post',
        url: `${API_URL}/articles/${articleId}/comments/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // 새로고침
        location.reload()
      })
      .catch((err => {
        console.log(err)
      }))
    }
  },
}
</script>

<style>

</style>