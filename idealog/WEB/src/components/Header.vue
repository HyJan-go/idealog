<template>
  <header>
    <el-menu class="el-menu-nav" router :default-active="$route.path" mode="horizontal">
      <div class="nav-left">
        <el-menu-item class="nav-index" index="/">主页</el-menu-item>
        <!-- <el-submenu index="2">
          <template class="nav-category" slot="title">分类</template>
          <el-menu-item style="padding-left:20px" index="2-1">前端</el-menu-item>
          <el-menu-item style="padding-left:20px" index="2-2">后端</el-menu-item>
          <el-menu-item style="padding-left:20px" index="2-3">移动端</el-menu-item>
        </el-submenu>-->
      </div>
      <el-menu-item style="border-bottom-color: transparent; cursor:auto" class="nav-search">
        <form>
          <input class="search-input" type="text" v-model="searchText" />
          <a class="search-btn" href="javascript:void(null)" @click="onSearch">
            <i class="el-icon-search"></i>
          </a>
        </form>
      </el-menu-item>

      <!-- <div :class="{login: isLogin, 'no-login': !isLogin}">
      <template v-if="!isLogin">-->
      <div>
        <!-- <template v-if="isLogin"> -->
        <template>
          <el-menu-item
            v-if="showWriteBtn()"
            style="border-bottom-color: transparent;"
            class="nav-write"
            index="/create"
          >
            <el-button class="write-btn" type="primary" icon="el-icon-edit">&nbsp;写文章</el-button>
            <!-- <img class="avatar" :src="user.avatar" :alt="user.username" :title="user.username"> -->
          </el-menu-item>
        </template>

        <template>
          <el-menu-item class="nav-login" index="/login">登录</el-menu-item>
        </template>
      </div>
    </el-menu>
    <!-- <h1>Let's share</h1> -->
    <!-- <div class="btns">
      <el-button>立即登录</el-button>
      <el-button>注册账号</el-button>
    </div>-->
  </header>
</template>

<script>
import { get, post } from "@/helpers/request";

export default {
  data() {
    return {
      searchText: ""
    };
  },
  methods: {
    onSearch() {
      console.log(this.searchText);
      post("/find", {
        title: "searchText"
      }).then(res => {
        console.log(res);
        this.$router.push({ path: this.$route.query.redirect || "/" });
      });
    },
    showWriteBtn() {
      return this.$router.path == "/";
    }
  }
};
</script>

<style scoped>
.el-menu-nav {
  display: flex;
  justify-content: space-between;
  box-shadow: 0 1px 5px 0 #e6e6e6;
  z-index: 5;
  width: 100%;
  position: fixed;
  top: 0;
}
.el-menu-nav div {
  display: flex;
}

@media (max-width: 500px) {
  header {
    width: 100vw;
  }
  .el-menu-nav {
    height: 60px;
    line-height: 1.5;
  }
  .el-menu-item {
    transform: scale(0.85);
  }
}

/* nav index style */
.el-menu-nav .nav-index {
  position: absolute;
  left: 20px;
}

/* .el-menu--horizontal > .el-submenu >>> .el-submenu__title {
  position: absolute;
  left: 120px;
} */

/* search form style */
.el-menu-nav .nav-search {
  z-index: 5;
  background: #fff;
  box-shadow: 5px 0 10px -5px #fff, -5px 0 10px -5px #fff;
}
.el-menu-nav .nav-search form {
  position: relative;
  top: -1px;
}
.el-menu-nav .search-input {
  height: 30px;
  width: 200px;
  background: transparent;
  border: 1px solid #9f9f9f;
  border-radius: 15px;
  color: #9f9f9f;
  padding: 0 20px 1px 10px;
}
.el-menu-nav .search-input:hover,
.el-menu-nav .search-input:focus {
  color: #81d4fa;
  border: 1px solid #81d4fa;
}
.el-menu-nav .search-input:focus {
  width: 300px;
  padding-left: 15px;
  /* transform: scale(1.2); */
  outline: none;
}
@media (max-width: 800px) {
  .el-menu-nav .search-input {
    width: 100px;
  }
  .el-menu-nav .search-input:focus {
    width: 160px;
  }
}
.el-menu-nav .search-btn {
  position: absolute;
  right: 0;
}
.el-menu-nav .search-btn i.el-icon-search {
  font-size: 16px;
  color: #9f9f9f;
}
.el-menu-nav .search-input:hover + .search-btn i.el-icon-search,
.el-menu-nav .search-input:focus + .search-btn i.el-icon-search {
  color: #81d4fa;
}

/* nav login style */
.nav-login {
  position: absolute;
  right: 20px;
  z-index: 3;
}
.nav-write:focus,
.nav-write:hover,
.nav-login:focus,
.nav-login:hover,
.nav-index:focus,
.nav-index:hover,
.el-submenu >>> .el-submenu__title:focus,
.el-submenu >>> .el-submenu__title:hover {
  background-color: transparent;
}

/* nav write style */
.nav-write {
  position: absolute;
  right: 100px;
  top: 1px;
  padding: 0 10px;
}
.nav-write:active {
  border: 0;
}
@media (max-width: 900px) {
  .nav-write {
    position: fixed;
    right: 10vw;
    bottom: 120px;
    top: auto;
  }
}
@media (max-width: 500px) {
  .nav-write {
    right: 6vw;
    bottom: 90px;
    top: auto;
  }
}
.nav-write .el-button--primary {
  height: 30px;
  border-radius: 20px;
  padding: 0 10px;
  background: #81d4fa;
  border: 0;
}

@media (max-width: 900px) {
  .nav-write .el-button--primary {
    /* width: 40px; */
    height: 40px;
    /* font-size: 20px; */
  }
}
.nav-write:hover .el-button--primary {
  color: #fff;
  background: #81d4fad0;
}
.nav-write:active .el-button--primary {
  background: #7ed1f8;
}
.nav-write .el-button--primary >>> i {
  color: #fff;
  font-size: 14px;
  margin: 0;
}
@media (max-width: 900px) {
  .nav-write .el-button--primary >>> i {
    font-size: 20px;
  }
}
.nav-write .el-button--primary >>> span {
  margin-left: 0;
  margin-right: 5px;
}

/* resolve nav align */
.nav-index,
.nav-login {
  top: 2px;
}

/* diy element ui */
.el-menu--horizontal > .el-submenu >>> .el-submenu__title,
.el-menu-item {
  color: #6f6f6f;
  padding: 0 30px;
}
.el-menu--horizontal > .el-submenu >>> .el-submenu__title:hover,
.el-menu--horizontal > .el-submenu:focus >>> .el-submenu__title,
.el-menu-item:hover,
.el-menu-item:focus {
  color: #81d4fa !important;
}
.el-menu-item.is-active {
  border-bottom-color: #81d4fa;
}
</style>