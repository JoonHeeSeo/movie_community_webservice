<template>
  <div>

    <h1>ArticleItem</h1>
    <hr>

    <p>글 번호 : {{ articleDetail.id }}</p>
    <p>작성자 :  <router-link :to="{ name: 'profile/:username', params: { username: articleDetail.username } }">{{ articleDetail.username }}</router-link>
    <p>제목 : {{ articleDetail.title }}</p>
    <p>내용 : {{ articleDetail.content }}</p>
    <p>작성 시간 : {{ articleDetail.created_at }}</p>
    <p>수정 시간 : {{ articleDetail.updated_at }}</p>
    <p>{{ articleDetail.like_users.length }}명이 좋아합니다.</p>

    <br>
    <form @submit.prevent="deleteArticle">
      <input type="submit" value="DELETE">
    </form> 
    
    <br>
    <router-link :to="{name : 'article/:id/update', params: {id: articleDetail.id}}">[UPDATE]</router-link>


    <hr>
    <p>총 {{ articleDetail.comment_count }}개의 댓글이 있습니다.</p>
    <div v-for="comment in articleDetail.comment_set" :key="comment.id">
      <br>
      <!-- <p>댓글 번호 : {{ comment.id }}</p> -->
      
      <p>댓글 작성자 : <router-link :to="{ name: 'profile/:username', params: { username: comment.username } }">{{ comment.username }}</router-link></p>
      <p>댓글 내용 : {{ comment.content }}</p>
      <p>댓글 작성 시간 : {{ comment.created_at }}</p>
      <p>댓글 수정 시간 : {{ comment.updated_at }}</p>
      <form @submit.prevent="deleteComment(comment.id)">
        <input type="submit" value="DELETE">
      </form>
      <br>
      <router-link :to="{name : 'article/:id/comment/:commentid/update', params: {id: articleDetail.id, commentid: comment.id}}">[UPDATE]</router-link>

    </div>

    <hr>
    <CommentCreate :articleId="articleId"/>


  </div>
</template>

<script>
import CommentCreate from '@/components/CommentCreate'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListItem',
  components: {
    CommentCreate,
  },
  props: {
    article: Object,
  },
  data() {
    return {
      articleId: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    articleDetail() {
      return this.$store.state.article
    },
    // articles() {
    //   return this.$store.state.articles
    // },

  },

  mounted() {
    this.articleId = this.$route.params.id
  },
  
  methods:{
    getArticleDetail() {
      const articleId = this.$route.params.id

      const payload = {
        articleId
      }

      this.$store.dispatch('getArticleDetail', payload)
    },

    deleteArticle() {
      const articleId = this.$route.params.id

      axios({
        method: 'delete',
        url: `${API_URL}/articles/${articleId}/`,
        data: { articleId },
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
    },

    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/comments/${commentId}/`,
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
    },
    
  }
}
</script>

<style>

</style>
