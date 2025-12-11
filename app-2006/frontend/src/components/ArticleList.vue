<template>
  <div class="content-box">
    <h2>Список тем (Статті)</h2>
    <div v-if="store.loading">Завантаження...</div>
    <table v-else class="forum-table" width="100%" cellspacing="1">
      <tr class="thead">
        <th>Назва теми</th>
        <th>Автор</th>
        <th>Дата</th>
      </tr>
      <tr v-for="article in store.articles" :key="article.id" class="row">
        <td>
            <router-link :to="'/article/' + article.id">
                {{ article.title }}
            </router-link>
        </td>
        <td>{{ article.author_name }}</td>
        <td>{{ article.publication_date }}</td>
      </tr>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBlogStore } from '../stores/blog'

const store = useBlogStore()

onMounted(() => {
  store.fetchArticles()
})
</script>

<style scoped>
.forum-table { background: #ccc; }
.thead th { background: #d1d7dc; padding: 4px; }
.row td { background: #fbfbfb; padding: 4px; border-bottom: 1px solid #ddd; }
</style>
