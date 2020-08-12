<template>
  <div class="article-wrapper">
    <ul v-for="article in articles" :key="article.article_id" class="article-list">
      <Articleli class="article-item" v-if="flag" :article="article"></Articleli>
    </ul>
  </div>
</template>

<script>
import Articleli from "@/components/Articleli";
export default {
  data() {
    return {
      flag: false,
      articles: []
    };
  },
  created() {
    blog.getBlogs().then(res => {
      console.log("res", res);
      if (res.length != 0) {
        this.articles = res;
        this.flag = true;
      } else {
        this.$message.error("未查询到文章");
      }
    });
  },
  components: {
    Articleli
  }
};
</script>

<style>
.article-wrapper {
  margin-bottom: -20px;
}
</style>