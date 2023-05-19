d<template>
  <div>

    <h1>ArticleItem</h1>
    <hr>

    <p>글 번호 : {{ articleDetail.id }}</p>
    <p>작성자 : {{ articleDetail.username }}</p>
    <p>제목 : {{ articleDetail.title }}</p>
    <p>내용 : {{ articleDetail.content }}</p>
    <p>작성 시간 : {{ articleDetail.created_at }}</p>
    <p>수정 시간 : {{ articleDetail.updated_at }}</p>

    <hr>

    <p>총 {{ articleDetail.comment_count }}개의 댓글이 있습니다.</p>
    
    <div v-for="comment in articleDetail.comment_set" :key="comment.id">
      <p>댓글 번호 : {{ comment.id }}</p>
      <p>댓글 내용 : {{ comment.content }}</p>
      <p>댓글 작성 시간 : {{ comment.created_at }}</p>
      <p>댓글 수정 시간 : {{ comment.updated_at }}</p>
    </div>

    <CommentCreate/>


  </div>
</template>

<script>
import CommentCreate from '@/components/CommentCreate'

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
      articleId: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    articleDetail() {
      return this.$store.state.article;
    },
    // articles() {
    //   return this.$store.state.articles;
    // },
  },

  mounted() {
    this.articleId = this.$route.params.id;
  },
  
  methods:{
    getArticleDetail() {
      const articleId = this.$route.params.id

      const payload = {
        articleId
      }

      this.$store.dispatch('getArticleDetail', payload)
    }
  }
}
</script>

<style>

</style>
