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
    searchInput: null,
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
      // 이런 것을 추가할 수도 있다
      // state.email = userinfo.email
      // state.firstname = userinfo.first_name
      // state.lastname = userinfo.last_name
    },

    DELETE_TOKEN_AND_USER_INFO(state) {
      state.useridx = null
      state.username = null
      state.token = null
      location.reload()
    },
    
    CONNECT_API(state, movies) {
      state.movies = movies
      console.log(movies)
    },
    
    SAVE_SEARCH_INPUT(state, searchInput) {
      state.searchInput = searchInput
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
    
    connetApi(context) {
      axios({
        method: 'get',
        // url: `${API_URL}/movies/get/movies/`,
        url: `${API_URL}/movies/get/movies/`
      })
        .then(res =>
          context.commit('CONNECT_API', res.data)
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
          const token = res.data.key;
          context.commit('SAVE_TOKEN', token)
    
          // return으로 promising
          return axios({
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
        .catch((error) => {
          if (error.response && error.response.status === 400) {
            alert('ID 중복인 것 같다.. 아닐수도 ㅎ')
          } else {
            console.log(error)
          }
        })
    },

    logIn(context, payload) {
      const username = payload.userid
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`, 
        data: {
          username, password
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token)
          
          return axios({
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

        .catch((error) => {
          if (error.response && error.response.status === 400) {
            alert('아이디 또는 비밀번호가 일치하지 않습니다.')
          } else {
            console.log(error)
          }
        })
    },


    logOut(context, token) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`, 
        headers: {
          Authorization: `Token ${token}`
        }
      })
      .then((res) => {
        context.commit('DELETE_TOKEN_AND_USER_INFO')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },  

    saveSearchInput(context, searchInput) {
      context.commit('SAVE_SEARCH_INPUT', searchInput)
    },

  },
  

  modules: {
  }
})
