import { createRouter, createWebHistory } from 'vue-router'
import ArticleList from '../components/ArticleList.vue'
import ArticleDetail from '../components/ArticleDetail.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: ArticleList },
    { path: '/article/:id', component: ArticleDetail }
  ]
})

export default router