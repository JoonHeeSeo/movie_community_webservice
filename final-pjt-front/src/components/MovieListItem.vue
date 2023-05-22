<template>
  <div>
    <div classs="main-container">
      <div class="poster-container">
        <img :src="getMoviePoster()" alt="movie_post" class="poster">
        <div class="ticket-container">
          <div class="ticket-content">
            <p class="ticket-movie-title">{{ movie.title }}</p>
            <p class="ticket-movie-vote">Rate: {{ movie.vote_average }}</p>
            <button class="ticket-detail-btn">자세히 보기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props: {
    movie: Object,
  },
  methods: {
    getMoviePoster() {
      return "https://image.tmdb.org/t/p/w200" + this.movie.poster_path
    }
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700&display=swap");

.main-container {
  width: 270px;
  height: 540px;
  position: relative;
  margin: 20px;
  align-items: center;
  justify-content: center;
}

body {
  background: #f4a7bb;
  font-family: "Roboto", sans-serif;
  display: flex;
  height: 100vh;
}

.poster-container {
  width: 230px;
  margin: 20px;
  position: relative;
  left: 30px;
  z-index: 9999
}

.poster {
  width: 100%;
  height: 330px;
  box-shadow: 0, 5px, 20px, rgba(0, 5px, 20px, 0.6);
  position: absolute;
  z-index: 1;

}

.ticket-container {
  background: #fff;
  width: 250px;
  height: 400px;
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  position: relative; left: -10px;
  top: 60px;
  box-shadow: 0 5px 20px 3px rgba(0, 0, 0, 0.6);
  opacity: 0;
}

.poster-container:hover .ticket-container {
  opacity: 1;
  animation: bounceIn 0.6s linear;
}

@keyframes bounceIn {
	0%,
	20%,
	40%,
	60%,
	80%,
	to {
		-webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
		animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
	}
	0% {
		opacity: 0;
		-webkit-transform: scale3d(0.3, 0.3, 0.3);
		transform: scale3d(0.3, 0.3, 0.3);
	}
	20% {
		-webkit-transform: scale3d(1.03, 1.03, 1.03);
		transform: scale3d(1.03, 1.03, 1.03);
	}
	40% {
		-webkit-transform: scale3d(0.9, 0.9, 0.9);
		transform: scale3d(0.9, 0.9, 0.9);
	}
	60% {
		opacity: 1;
		-webkit-transform: scale3d(1.01, 1.01, 1.01);
		transform: scale3d(1.01, 1.01, 1.01);
	}
	80% {
		-webkit-transform: scale3d(0.97, 0.97, 0.97);
		transform: scale3d(0.97, 0.97, 0.97);
	}
	to {
		opacity: 1;
		-webkit-transform: scaleX(1);
		transform: scaleX(1);
	}
}

.ticket-content {
	width: 100%;
	position: absolute;
	bottom: 0;
	text-align: center;
}

.ticket-movie-title {
  color:#2f2f2f;
	text-transform: uppercase;
  font-size: 20px;
  font-weight:bold;
	margin-bottom: 5px;
}

.ticket-movie-vote {
  margin-right:20px;
  text-align: right;
	color: #999;
	font-size: 0.9rem;
	margin-bottom: 20px;
}

.ticket-detail-btn {
	cursor: pointer;
	width: 100%;
	background: #2f2f2f;
	color: white;
	padding: 15px 0;
	font-size: 1rem;
	font-weight: bold;
	text-transform: uppercase;
	border: 0;
	border-bottom-left-radius: 5px;
	border-bottom-right-radius: 5px;
}

</style>