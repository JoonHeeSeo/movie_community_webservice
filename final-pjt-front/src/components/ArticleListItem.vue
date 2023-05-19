<template>
  <div>

    <h1>ArticleItem</h1>
    <p>{{ articleId }}번 글</p>

    <div v-for="article in articles" :key="article.id">
      <div v-if="article.id === articleId">
        <p>제목 : {{ article.title }}</p>
        <p>내용 : {{ article.content }}</p>
        <p>작성 시간 : {{ article.created_at }}</p>
        <p>마지막 수정 시간 : {{ article.updated_at }}</p>
        <p>작성자 : {{ article.username }}</p>
      </div>
    </div>
    <hr>

    <CommentList/>


  </div>
</template>

<script>
import CommentList from '@/components/CommentList'

export default {
  name: 'ArticleListItem',
  components: {
    CommentList,
  },
  props: {
    article: Object,
  },
  data() {
    return {
      articleId: null
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
  mounted() {
    this.articleId = this.$route.params.id;
  },
}
</script>

<style>

</style>
