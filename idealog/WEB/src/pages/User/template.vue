<template>
  <div id="user">
    <section class="h-info">
      <div class="intro">
        <div class="avatar-wrapper">
          <!-- "`${info.avatar}`" -->
          <img src="http://192.168.195.10:5005/user/images/default.jpg" alt="avatar" />
        </div>
        <div class="info-text">
          <h2>{{info.nick_name}}</h2>
          <p>{{info.profile}}</p>
        </div>
      </div>
      <div class="follow-btn">
        <el-button v-if="`${info.back_status}`==true" type="danger" class="unfollow-btn">取消关注</el-button>
        <el-button v-else type="primary" class="follow-btn">关注</el-button>
      </div>
    </section>
    <section class="m-info">
      <section class="side-nav">
        <ul>
          <router-link :to="`/user/${user_id}/article`">
            <li class="nav-item">
              <i class="el-icon-location">&nbsp;文章</i>
            </li>
          </router-link>
          <router-link :to="`/user/${user_id}/follow`">
            <li class="nav-item">
              <i class="el-icon-menu">&nbsp;关注</i>
            </li>
          </router-link>
          <router-link :to="`/user/${user_id}/fans`">
            <li class="nav-item">
              <i class="el-icon-setting">&nbsp;粉丝</i>
            </li>
          </router-link>
        </ul>
      </section>
      <section class="list">
        <transition name="fade" mode="out-in">
          <router-view></router-view>
        </transition>
      </section>
    </section>
  </div>
</template>

<script>
export default {
  props: ["user_id"],
  data() {
    return {
      flag: false,
      info: []
    };
  },
  created() {
    user.getUserInfo().then(res => {
      console.log("userInfo res", res);
      if (res.length != 0) {
        this.info = res;
        this.flag = true;
      } else {
        this.$message.error("未查询到用户");
      }
    });
  }
};
</script>

<style scoped>
/* common */
#user {
  padding-top: 30px;
  padding-bottom: 120px;
  /* direction: flex;
  flex-direction: column; */
}
@media (max-width: 640px) {
  #user {
    width: 90vw;
  }
}

/* info header */
.h-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  margin-bottom: 20px;
  box-shadow: 0 0 4px 0 #e0e0e0;
  border-radius: 5px;
  line-height: 1.8;
}

.h-info .avatar-wrapper {
  width: 60px;
  height: 60px;
}
.h-info .avatar-wrapper img {
  width: 100%;
  height: 100%;
}
/* .h-info .avatar-wrapper i {
  line-height: 80px;
  font-size: 56px;
  text-align: center;
} */
.h-info .intro {
  display: flex;
  align-items: center;
  margin-left: 10px;
}
.h-info .info-text {
  text-align: left;
  font-size: 14px;
  margin-left: 20px;
}
.h-info .follow-btn {
  margin: 0 10px;
}
@media (max-width: 640px) {
  .h-info {
    padding: 10px;
  }
  .h-info .follow-btn .el-button {
    margin: 0;
  }
  .h-info .info-text {
    font-size: 12px;
    margin-left: 10px;
  }
}

/* info main */
.m-info {
  display: flex;
  box-shadow: 0 0 4px 0 #e0e0e0;
  position: relative;
  border-radius: 5px;
}
.m-info .side-nav {
  width: 180px;
  padding: 10px 0;
  border-right: 1px solid #efefef;
}
.m-info .nav-item {
  padding: 10px 20px 10px 15px;
}
.m-info .nav-item:hover {
  color: #81d4fa;
  cursor: pointer;
}
.m-info .nav-item i {
  font-size: 14px;
}
.m-info .list {
  width: 100%;
  padding: 20px;
}
@media (max-width: 640px) {
  .m-info .nav-item i {
    font-size: 12px;
  }
}
@media (max-width: 500px) {
  .m-info .side-nav {
    width: 100%;
    height: 70px;
    position: absolute;
    border-right: 0;
    border-bottom: 1px solid #efefef;
  }
  .m-info .side-nav ul {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .m-info .nav-item {
    padding: 10px 30px;
  }
  .m-info .list {
    width: 100%;
    padding-top: 90px;
  }
}
@media (max-width: 450px) {
  .m-info .nav-item {
    padding: 10px 25px;
  }
}
@media (max-width: 400px) {
  .m-info .nav-item {
    padding: 10px 20px;
  }
}
@media (max-width: 360px) {
  .m-info .nav-item {
    padding: 10px 15px;
  }
}
@media (max-width: 320px) {
  .m-info .nav-item {
    padding: 10px;
  }
}
</style>

<style>
/* diy el ui */
.el-button {
  border-color: #fff;
}
.el-button:hover {
  border-color: #fff;
  color: #fff;
}
</style>