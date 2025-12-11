<template>
  <div class="content-box" v-if="store.currentArticle">
    <h2>{{ store.currentArticle.title }}</h2>

    <div class="post-container">
        <div class="user-info">
            <b>{{ store.currentArticle.author_name }}</b><br>
            <img src="https://via.placeholder.com/100" alt="avatar"><br>
            User
        </div>
        <div class="post-content">
            <small>Додано: {{ store.currentArticle.publication_date }}</small>
            <hr>
            {{ store.currentArticle.text }}
        </div>
    </div>

    <h3>Коментарі:</h3>
    <div v-for="comment in store.currentArticle.comments" :key="comment.id" class="post-container comment">
        <div class="user-info">
            <b>{{ comment.author_name }}</b>
        </div>
        <div class="post-content">
            {{ comment.text }}
        </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBlogStore } from '../stores/blog'

const store = useBlogStore()
const route = useRoute()

onMounted(() => {
  store.fetchArticleById(route.params.id)
})
</script>

<style scoped>
.post-container { display: flex; border: 1px solid #336699; margin-bottom: 10px; background: white; }
.user-info { width: 150px; background: #e0e8f0; padding: 10px; border-right: 1px solid #336699; }
.post-content { padding: 10px; flex-grow: 1; }
</style>
