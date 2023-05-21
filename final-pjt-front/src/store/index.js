import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],

  state: {
    useridx: null,
    username: null,
    token: null,
    articles: [],
    article: null,
    movies: [],
    moviesearch: null,
    moviedetail: null,
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },

  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    GET_ARTICLE_DETAIL(state, article) {
      state.article = article
    },

    GET_MOVIES(state, movies) {
      state.movies = movies
    },

    SAVE_TOKEN(state, token) {
      state.token = token
      // HomeView로 되돌아가기 
      router.push({ name: 'home' }) 
    },

    SAVE_USER_INFO(state, userinfo) {
      state.useridx = userinfo.pk
      state.username = userinfo.username
      // state.email = userinfo.email
      // state.firstname = userinfo.first_name
      // state.lastname = userinfo.last_name
    },
  },

  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then(res =>
          context.commit('GET_ARTICLES', res.data)
        )
        .catch(err =>console.log(err))
    },

    getArticleDetail(context, payload) {
      const articleId = payload.articleId

      axios({
        method: 'get',
        url: `${API_URL}/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
      })
        .then(res =>
          context.commit('GET_ARTICLE_DETAIL', res.data)
        )
        .catch(err =>console.log(err))
    },

    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then(res =>
          context.commit('GET_MOVIES', res.data)
        )
        .catch(err => console.log(err))
    },

    signUp(context, payload) {
      const username = payload.userid
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token)
          
          axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
              Authorization: `Token ${token}`
            }
          })
            .then((response) => {
              context.commit('SAVE_USER_INFO', response.data)
            })
            .catch((error) => {
              console.log(error)
            })
        })
    },

    signIn(context, payload) {
      const username = payload.userid
      const password = payload.password
      axios({
        method: 'post',
        // 주소가 signin으로 작성된 것에 유의 (login이 아니다)
        url: `${API_URL}/accounts/signin`, 
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => console.log(err))
    },


    // getUser(username) {
    //   axios({
    //     url: `${API_URL}/accounts/signin`
    //   })
    // }
  },

  modules: {
  }
})
