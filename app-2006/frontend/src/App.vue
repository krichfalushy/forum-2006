<template>
  <div class="forum-container">
    <header class="header-2006">
      <h1>My Blog Forum</h1>
      <nav>
        <router-link to="/">Головна</router-link>
      </nav>
    </header>
    <router-view></router-view>
  </div>
</template>

<style>
/* Базовий стиль а-ля форум */
body { background-color: #e5e5e5; font-family: Verdana, sans-serif; font-size: 11px; }
.forum-container { width: 900px; margin: 0 auto; background: white; border: 1px solid #000; }
.header-2006 { background: #336699; color: white; padding: 10px; }
a { color: #336699; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
