<template>
  <div>
    <h1 style="margin:80px 0px 0px 30px; color:black;">Community</h1>
    <ArticleList/>
    <button @click="$router.push({ name: 'articlecreate' })" style="position:relative; top:20px; left:95%; border: solid 1px black; padding:5px; background-color: none; cursor:pointer;">
    CREATE
    </button>
    <!-- <router-link :to="{ name: 'articlecreate' }" style="margin:20px 0px 0px 30px;">[CREATE]</router-link> -->
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
        this.$router.push({ name:'login' })
      }
    }
  }
}
</script>

<style>

</style>