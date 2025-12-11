import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    host: true,
    proxy: {
      '/api': {
        target: 'http://web:8000', // Ім'я сервісу Django з docker-compose
        changeOrigin: true,
      }
    }
  }
})
