<template>
  <div>
    <h1>
      MovieDetailView
      <br>
      {{ moviedetail }}
      {{ movie }}
    </h1>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "https://api.themoviedb.org/3/search/movie?api_key=af5292844a6af1d68203e1c0b3104130&query="

export default {
  name:'MovieDetailView',
  data(){
    return{
      movie: null
    }
  },
  updated() {
    axios({
      method:'get',
      url: `${API_URL}`+this.$store.state.moviedetail
    })
    .then(res =>
    this.movie = res.data.results
    )
    .catch(err => console.log(err))
  },
  computed: {
    moviedetail: function() {
      return this.$store.state.moviedetail
    }
  }
}
</script>

<style>

</style>