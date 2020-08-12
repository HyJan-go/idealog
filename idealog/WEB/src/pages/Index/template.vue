<template>
  <div id="index">
    <section class="left">
      <h1 style="line-height: 3;">Let's share</h1>
      <ul v-for="article in articles" :key="article.article_id" class="article-list">
        <Articleli v-if="flag" :article="article" ></Articleli>
      </ul>
    </section>
    <section class="card"></section>
  </div>
</template>

<script>
import Articleli from "@/components/Articleli";
import auth from "@/api/auth.js";
import blog from "@/api/blog.js";
import user from "@/api/user.js";
import comment from "@/api/comment.js";
import admin from "@/api/admin.js";

window.auth = auth;
window.blog = blog;
window.user = user;
window.comment = comment;
window.admin = admin;

export default {
  data() {
    return {
      flag: false,
      articles: []
    };
  },
  created() {
    blog.getBlogs().then(res => {
      console.log("indexBlogs res", res);
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

<style scoped>
/* common */
#index {
  padding-bottom: 90px;
  /* display: flex; */
}
@media (max-width: 800px) {
  #index {
    width: 60vw;
  }
}
@media (max-width: 640px) {
  #index {
    width: 85vw;
  }
  #index .left {
    display: flex;
    flex-direction: column;
  }
}
</style>