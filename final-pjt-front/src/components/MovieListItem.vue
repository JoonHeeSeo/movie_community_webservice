<template>
  <div>
    <p>
      영화 제목 : {{  movie.title  }}  
      <br>
  
      영화 평점 : {{  movie.vote_average }}
    </p>
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props: {
    movie: Object,
  }

}
</script>

<style>

</style>