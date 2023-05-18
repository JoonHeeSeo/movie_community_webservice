<template>
  <div>
    <h3>{{ article.id }}</h3>
    <!-- link로 만들어야함  -->
    <p>{{ article.title }}</p>
    
    <!-- <router-link :to="{
      name: 'DetailView',
      params: {id: article.id }}">
      [DETAIL]
    </router-link> -->
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
