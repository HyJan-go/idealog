<template>
  <transition name="fade" mode="out-in">
    <div class="reply-item" v-if="hasReply">
      <div class="reply-header">
        <router-link class="reply-user" to="/user">Bob</router-link>
      </div>
      <div class="reply-content">Shut up!</div>
      <div class="reply-footer">
        <el-button @click="hasReplyBox = true">回复</el-button>
        <el-button @click="hasReply = false">删除</el-button>
      </div>
      <div class="reply-line"></div>
      <transition name="fade" mode="out-in">
        <div class="reply-box" v-show="hasReplyBox">
          <el-input
            data-vue-emojiable="true"
            type="textarea"
            :rows="5"
            placeholder="来点评论吧"
            v-model="replyText"
          ></el-input>

          <div class="toolbar">
            <div class="left">
              <i class="icon-ali-bq"></i>
            </div>
            <!-- <vue-feedback-reaction v-model="feedback" /> -->
            <div class="right">
              <el-button @click="deliverReply">发表</el-button>
              <el-button @click="hasReplyBox = false" transition="fade">取消</el-button>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </transition>
</template>

<script>
export default {
  data() {
    return {
      replyText: "",
      hasReply: true,
      hasReplyBox: false
    };
  },
  methods: {
    //reply box
    deliverReply() {}
  }
};
</script>

<style>
/* .reply-item {
  padding: 10px 0;
} */
.reply-header {
  margin: 10px 0;
}
.reply-user{
  color: #000;
}
.reply-content {
  font-size: 14px;
  margin: 10px 0;
}
.reply-footer {
  margin: 10px 0;
}
.reply-line{
  height: 1px;
  background: #e6e6e6;
  margin: 15px 0;
}
/* reply */
/* .reply-box .el-textarea >>> .el-textarea__inner{
  margin: 10px 0;
} */
.reply-box .toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.reply-box .left i {
  font-size: 20px;
  color: #d0d0d0;
}
.reply-box .left i:hover {
  color: #aaa;
  cursor: pointer;
}
.reply-box .right {
  display: flex;
  align-items: center;
}

.el-button {
  height: 30px;
  padding: 5px 20px;
}
.el-button:hover {
  border-color: #81d4fa;
  color: #81d4fa;
}

</style>
