<template>
  <div>
    <h1>
      ArticlesList
    </h1>
    <button>create</button>
      <ArticleListItem
      v-for="article in articles" :key="article.id" :article="article"
      />
  </div>
  
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name:'ArticleList',
  components:{
    ArticleListItem,
  },

  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>