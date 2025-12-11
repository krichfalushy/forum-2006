import { defineStore } from 'pinia'
import axios from 'axios'

export const useBlogStore = defineStore('blog', {
  state: () => ({
    articles: [],
    currentArticle: null,
    loading: false
  }),
  actions: {
    async fetchArticles() {
      this.loading = true
      try {
        // Звертаємось до /api/articles/ (проксі перекине на Django)
        const response = await axios.get('/api/articles/')
        this.articles = response.data
      } catch (error) {
        console.error("API Error:", error)
      } finally {
        this.loading = false
      }
    },
    async fetchArticleById(id) {
      this.loading = true
      try {
        const response = await axios.get(`/api/articles/${id}/`)
        this.currentArticle = response.data
      } catch (error) {
        console.error("API Error:", error)
      } finally {
        this.loading = false
      }
    }
  }
})
