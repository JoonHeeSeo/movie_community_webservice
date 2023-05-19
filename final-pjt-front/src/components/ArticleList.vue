<template>
  <div>
    <h1>ArticlesList</h1>
    <hr>

    <div v-for="article in articles" :key="article.id">
      <p> 제목: 
      <router-link :to="{ name: 'article/:id', params: { id: article.id } }">{{ article.title }}</router-link>
      </p>
      <p>글 번호: {{ article.id }}</p>
      <p>내용: {{ article.content }}</p>
      <p>작성자: {{ article.username }}</p>
      <hr>
    </div>

    <!-- <ArticleListItem v-if="selectedArticle" :article="selectedArticle" /> -->

  </div>
</template>

<script>
// import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    // ArticleListItem,
  },
  // data() {
  //   return {
  //     selectedArticle: null,
  //   };
  // },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
}
</script>

<style>

</style>