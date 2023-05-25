<template>
  <div style="display: flex; justify-content: center;">
    <div class="articlelist-item-container">
      <div>
        <p style="margin-top: 20px">Article #{{ articleDetail.id }}  {{ articleDetail.title }}</p>
        <hr>

        <div>
          <h1>{{ articleDetail.title }}</h1>
        </div>
        <div>
          {{ articleDetail.content }}
        </div>
        <div style="margin-top: 20px">
          <p style="margin-left: 300px; font-size:smaller;">작성자 :  <router-link :to="{ name: 'profile/:username', params: { username: articleDetail.username } }">{{ articleDetail.username }}</router-link></p>
        </div>
        <p>{{ articleDetail.like_users.length }}명이 좋아합니다.
        <button @click="likeArticle(articleDetail.id)" class="article-like-btn">
          {{ checkLikeArticle(articleDetail) ? '❤️' : '🤍' }}
        </button></p>
        <div style="display: flex; justify-content: flex-end;">
          <form @submit.prevent="deleteArticle">
            <input type="submit" value="DELETE">
          </form>
          <router-link :to="{name : 'article/:id/update', params: {id: articleDetail.id}}">[UPDATE]</router-link>
        </div>
      </div>
    </div>
    <hr>

    
    <!-- <p>작성 시간 : {{ articleDetail.created_at }}</p>
    <p>수정 시간 : {{ articleDetail.updated_at }}</p> -->
    <div class="article-comment-container">
      <p style="margin-top:20px; font-weight: bold;">총 {{ articleDetail.comment_count }}개의 댓글이 있습니다.</p>
      <hr>
      <CommentCreate :articleId="articleId"/>
      <div v-for="comment in articleDetail.comment_set" :key="comment.id">
        <br>
        <!-- <p>댓글 번호 : {{ comment.id }}</p> -->
        
        <p>{{ comment.content }}</p>
        <p style="margin-left:300px; font-size: smaller;">작성자 : <router-link :to="{ name: 'profile/:username', params: { username: comment.username } }">{{ comment.username }}</router-link></p>
        <!-- <p>댓글 작성 시간 : {{ comment.created_at }}</p>
        <p>댓글 수정 시간 : {{ comment.updated_at }}</p> -->
        <div style="display: flex; justify-content: flex-end;">
          <form @submit.prevent="deleteComment(comment.id)">
            <input type="submit" value="DELETE">
          </form>
          <router-link :to="{name : 'article/:id/comment/:commentid/update', params: {id: articleDetail.id, commentid: comment.id}}">[UPDATE]</router-link>
        </div>
      </div>
    </div>  
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
        location.reload()
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
.articlelist-item-container{
  color:black;
  display:flex;
  margin: 20px;
}
.article-comment-container{
  color:black;
  display: flex;
  flex-direction: column;
  margin: 20px;

}
</style>
