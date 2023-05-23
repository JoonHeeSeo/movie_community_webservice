<template>
  <div>
    <h1 style="color:black; margin: 80px 30px 20px 20px; position: relative;">Community</h1>
    <hr>
    <ArticleList/>
    <router-link :to="{ name: 'articlecreate' }">[CREATE]</router-link>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name:'CommunityView',
  components: {
    ArticleList,
  },
  created() {
    this.getArticles()
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods:{
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name:'signin' })
      }
    }
  }
}
</script>

<style>

</style>