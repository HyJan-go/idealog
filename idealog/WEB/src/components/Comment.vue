<template>
  <transition name="fade" mode="out-in">
    <div class="comment-item" v-if="hasComment">
      <!--header username avatar-->
      <div class="comment-header">
        <router-link class="comment-user" to="/user">Alex</router-link>
      </div>
      <!--content-->
      <div class="comment-content">I like it. Please update quickly!</div>
      <!--footer btns-->
      <div class="comment-footer">
        <el-button @click="hasReplyBox = true">回复</el-button>
        <el-button @click="hasComment = false">删除</el-button>
      </div>
      <div class="comment-line"></div>
      <!--ReplyBox-->
      <transition name="fade" mode="out-in">
        <div class="reply-box" v-show="hasReplyBox">
          <el-input
            data-vue-emojiable="true"
            type="textarea"
            :rows="5"
            placeholder="来点评论吧"
            v-model="commentText"
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

      <div class="reply-list">
        <div class="reply-wrapper">
          <Reply />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import Reply from "./Reply";
export default {
  data() {
    return {
      commentText: "",
      hasComment: true,
      hasReply: true,
      hasReplyBox: false
    };
  },
  methods: {
    //comment box
    deliverReply(){

    }
  },
  components: {
    Reply
  }
};
</script>

<style>
.comment-item {
  padding-top: 10px;
}
.comment-header {
  margin: 10px 0;
}
.comment-content {
  font-size: 14px;
  margin: 10px 0;
}
.comment-footer {
  margin: 10px 0;
}
.comment-line {
  height: 1px;
  background: #e6e6e6;
  margin: 15px 0;
}
.reply-wrapper {
  padding-left: 30px;
}

/* comment */
.reply-box textarea{
  padding-top: 10px;
  resize: none;
}
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

.el-button:hover {
  border-color: #81d4fa;
  color: #81d4fa;
}

</style>
