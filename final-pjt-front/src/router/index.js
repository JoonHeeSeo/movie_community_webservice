import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LogInView from '../views/LogInView.vue'
import SignUpView from '../views/SignUpView.vue'
import RecommendView from '../views/RecommendView.vue'
import SearchView from '../views/SearchView.vue'
import CommunityView from '../views/CommunityView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import ArticleListItem from '../components/ArticleListItem.vue'
import ArticleUpdateView from '../views/ArticleUpdateView'
import CommentUpdateView from '../views/CommentUpdateView'
import ProfileView from '../views/ProfileView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path:'/signup',
    name:'signup',
    component: SignUpView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/profile/:username',
    name: 'profile/:username',
    component: ProfileView
  },
  {
    path: '/article/:id',
    name: 'article/:id',
    component: ArticleListItem
  },
  {
    path: '/article/:id/update',
    name: 'article/:id/update',
    component: ArticleUpdateView,
  },
  {
    path: '/article/:id/comment/:commentid/update',
    name: 'article/:id/comment/:commentid/update',
    component: CommentUpdateView,
  },
  {
    path: '/articlecreate',
    name: 'articlecreate',
    component: ArticleCreateView
  },
  {
    path: '/moviedetail/:movie_id',
    name: 'moviedetail/:movie_id',
    component: MovieDetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
