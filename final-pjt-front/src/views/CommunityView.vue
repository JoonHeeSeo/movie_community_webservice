<template>
  <div>
    <h1>Community</h1>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '../components/ArticleList.vue'

export default {
  name:'CommunityView',
  components: {
    ArticleList,
  },
  created() {
    this.getArticles()
  },
  methods:{
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>