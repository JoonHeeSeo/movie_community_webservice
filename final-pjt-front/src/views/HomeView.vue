<template>
  <div>
    <h1>This is HomePage</h1>
    <MovieList/>
    
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
  components: {
    MovieList,
  },
  // created() {
  //   this.getMovies()
  // },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  }
}
</script>
