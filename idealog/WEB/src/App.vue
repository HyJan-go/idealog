<template>
  <div id="app">
    <Header id="header"></Header>
    <main id="main">
      <transition name="fade" mode="out-in">
        <router-view class="app-view" />
      </transition>
    </main>
    <Footer id="footer"></Footer>
  </div>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  name: "App",
  components: {
    Header,
    Footer
  }
  // data() {
  //   return {
  //     isRouterAlive: true
  //   };
  // },
  // methods: {
  //   reload() {
  //     this.isRouterAlive = false;
  //     this.$nextTick(() => (this.isRouterAlive = true));
  //   }
  // }
};
// request('auth/login', 'post',{username: 'hunger1', password:'123458'}).then(data=>{console.log(data)})
</script>

<style>
/* base */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  transition: 0.2s;
}
*::selection {
  background-color: #81d4fa;
  color: #fff;
}
ul,
ol {
  list-style: none;
}
a {
  text-decoration: none;
  color: inherit;
}
body {
  width: 100%;
}
/* common */
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  line-height: 2;
}
#main {
  padding: 0 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
@media (max-width: 1600px) {
  #main {
    padding: 0 20vw;
  }
}
/* @media (max-width: 800px) {
  #app {
    width: 800px;
    position: relative;
  }
  #main {
    padding: 0;
    width: 600px;
    position: absolute;
    margin: 0 auto;
  }
} */
@media (max-width: 640px) {
  #main {
    padding: 0 10px;
  }
}

.app-view {
  width: 100%;
}
@media (max-width: 1000px) {
  .app-view {
    width: 600px;
  }
}

/* diy element ui */
/* .comment-wrapper .comment-box .el-textarea textarea{
  padding-top: 30px;
  background: #eee;
} */
/* .el-button:hover {
  color: #fff;
  border-color: #fff;
} */
</style>

<style>
/* fade in out transition */
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}

@media (max-width: 640px) {
  .el-message-box {
    width: 90vw;
  }
}
</style>
