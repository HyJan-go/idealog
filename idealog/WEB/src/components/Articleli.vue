<template>
  <div class="article">
    <header class="article-title">
      <h2>
        <router-link
          :to="{path:`/detail/${article.article_id}`}"
        >{{article.title}}</router-link>
      </h2>
    </header>
    <p class="article-intro">
      {{article.content.slice(0,30)}}
      <router-link :to="`/detail/${article.article_id}`">
        <span style="color:#ccc">&nbsp;查看全文</span>
      </router-link>
    </p>
    <footer class="article-info">
      <span>{{article.send_time}}</span>
      <router-link :to="{path:`/user/${article.user_id}`}">{{article.user_name}}</router-link>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      art: this.article
    };
  },
  props: ["article"],
  watch: {
    article: function(n, o) {
      this.art = n;
    }
  }
};
</script>

<style>
.article {
  /* border: 1px solid #e6e6e6; */
  width: 100%;
  margin-bottom: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  text-align: left;
  line-height: 1.5;
  box-shadow: 0 0 4px 0 #d0d0d0;
  border-radius: 5px;
}
.article-title {
  font-size: 14px;
}
.article-title a:link {
  color: #2f2f2f;
}
.article-title a:visited {
  color: #9f9f9f;
}
.article-intro {
  padding: 15px 0;
  font-size: 14px;
}
@media (max-width: 800px) {
  .article {
    padding: 15px;
  }
  .article-intro {
    padding: 10px 0;
  }
}
@media (max-width: 640px) {
  .article {
    font-size: 12px;
  }
  .article p {
    font-size: 12px;
  }
  .article h2 {
    font-size: 16px;
  }
  .article-intro {
    padding: 5px 0;
  }
}
@media (max-width: 500px) {
  .article-intro {
    padding: 8px 0;
  }
}
</style>