<template>
  <div class="userli">
    <div class="intro">
      <div class="avatar-wrapper">
        <!-- <img :src="`${followi.avatar}`" alt /> -->
        <img src="http://192.168.195.10:5005/user/images/default.jpg" alt="avatar" />
        <!-- <i class="icon-ali-avatar"></i> -->
      </div>
      <div class="info-text">
        <h3>{{followi.followed_id}} {{followi.nick_name}}</h3>
        <p>intro my self, my intro self</p>
      </div>
    </div>
    <div class="follow-btn">
      <transition name="fade" mode="out-in">
        <el-button @click="follow" v-if="status==='0'" type="primary" class="unfollow-btn">+ 关注</el-button>
        <el-button
          @click="follow"
          v-else
          @mouseleave.native="follow_hint='已关注'"
          @mouseenter.native="follow_hint='取消关注'"
          :type="follow_hint=='已关注'?'primary':'danger'"
          class="unfollow-btn"
        >{{follow_hint}}</el-button>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      status: this.follower.back_status,
      follow_hint: "已关注",
      followi: this.follower
    };
  },
  props: ["follower"],
  watch: {
    follower: function(n, o) {
      this.followi = n;
    }
  },
  methods: {
    follow() {
      user
        .actFollow({
          user_id: "1",
          followed_id: this.followi.followed_id
        })
        .then(res => {
          console.log("res", res);
          if (res.msg == "1") {
            this.$message.success("关注成功");
            this.status = "1";
            this.$emit("onfollow");
          } else if (res.msg == "0") {
            this.$message.success("取关成功");
            this.status = "0";
          } else {
            this.$message.error(res.msg);
          }
        });
    }
  }
};
</script>

<style scoped>
.userli {
  width: 100%;
  padding: 20px;
  margin-bottom: -1px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  text-align: left;
  line-height: 1.5;
  /* box-shadow: 0 0 4px 0 #d0d0d0; */
  border-top: 1px solid #efefef;
  border-bottom: 1px solid #efefef;
  border-radius: 5px;
}
.userli .intro {
  display: flex;
  align-items: center;
}
.userli .avatar-wrapper {
  width: 30px;
}
.userli .avatar-wrapper img{
  width: 100%;
}
.userli .avatar-wrapper i {
  font-size: 32px;
}
.userli .info-text {
  font-size: 12px;
  margin: 0 20px;
}

.userli .follow-btn {
  margin-left: 10px;
}
.userli .follow-btn .el-button {
  width: 70px;
  height: 28px;
  padding: 1px 10px 0;
  font-size: 12px;
}
</style>
