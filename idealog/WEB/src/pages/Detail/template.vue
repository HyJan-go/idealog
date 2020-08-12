<template>
  <div id="detail">
    <section class="left">
      <section class="article-wrapper">
        <h1 class="article-title">{{detail.title}}</h1>
        <div class="article-info">
          <router-link to="/user" class="author">{{detail.user_name}}</router-link>
          <span class="time">{{detail.send_time}}</span>
          <span class="view-num">
            <i class="el-icon-view"></i>
            阅读 215，不存在的，根本没人看啊
          </span>
          <ul class="tag-list">
            <li class="tag-item"></li>
            <li class="tag-item"></li>
            <li class="tag-item"></li>
          </ul>
        </div>
        <article>
          <p>假数据，好看点的数据</p>
          <p>我是一个特别爱惜时间的人。</p>
          <p>每天5:30起床，6:15到图书馆，这样的作息时间几乎持续了将近两年的光阴。</p>
          <p>后来，我对自己时间的把控越来越精准。</p>
          <p>如果有一天，我不小心睡过了头，那么我甚至可以准确预估出和平时相比，我会迟几分钟出现在图书馆。</p>
          <p>过去一年的考研时光，我将自己每月、每周、每天的安排都按照小时来划分。</p>
          <p>特别是每天的安排，我会根据平时学校的课程表画出一条时间刻度线，然后分成几个部分，将每天的任务分别对应到具体的时间段。</p>
          <p>甚至精确到从图书馆到上课班级，我需要花费多长的时间跑过去；下课结束之后，回到图书馆，我需要再看多长时间的书；午休休息多长时间，下午几点开始学习；晚上几点去吃晚饭.....</p>
          <p>年轻的时候，就要和时间进行赛跑，你对待时间的态度决定你生活的态度。</p>
          <p>真数据</p>
          <p>{{detail.content}}</p>
        </article>
        <div class="action">
          <i
            class="icon-ali-favor"
            :class="isFavor? 'has-favor':'not-favor'"
            id="icon-favor"
            @click="favor"
          >&nbsp;{{detail.fabulous_num}}</i>
          <el-button @click="follow" v-if="`${detail.status}`=='0'">+ 关注</el-button>
          <el-button
            @click="follow"
            v-else
            @mouseleave.native="fans_hint='已关注'"
            @mouseenter.native="fans_hint='取消关注'"
            :type="fans_hint=='已关注'?'primary':'danger'"
            class="unfollow-btn"
          >{{fans_hint}}</el-button>
        </div>
        <!-- <div class="reward"></div> -->
      </section>
      <section class="comment-wrapper">
        <div class="comment-box">
          <el-input
            data-vue-emojiable="true"
            type="textarea"
            :rows="5"
            placeholder="来点评论吧"
            @click.native="showToolbar"
          ></el-input>

          <transition name="fade" mode="out-in">
            <div class="toolbar" v-if="hasToolbar">
              <div class="left">
                <i class="icon-ali-bq"></i>
              </div>
              <!-- <vue-feedback-reaction v-model="feedback" /> -->
              <div class="right">
                <el-button @click="deliverComment">发表</el-button>
                <el-button @click="hideToolbar">取消</el-button>
              </div>
            </div>
          </transition>
        </div>

        <ul class="comment-list">
          <comment />
          <comment />
          <comment />
          <comment class="last-comment-item" />
        </ul>
      </section>
    </section>
    <section class="card"></section>
  </div>
</template>

<script>
import comment from "@/components/Comment";
import { get, post } from "@/helpers/request";
//emoji plugin
// import VueFeedbackReaction from "vue-feedback-reaction";

export default {
  data() {
    return {
      //emoji
      meid: this.global.meid,
      artid: this.$route.params.article_id,
      detail: "",

      fans_hint: "",

      hasToolbar: true,
      hasCommentTwoBox: true
    };
  },
  created() {
    // if(this.meid == ""){
    //   this.$message.error("请先登录")
    // }
    console.log(this.meid, this.artid);
    blog
      .getBlogDetailById({ user_id: this.meid, article_id: this.artid })
      .then(res => {
        console.log("blogDetail res", res);
        this.detail = res;
      });
  },
  methods: {
    //emoji
    myText(e) {
      console.log(e.data);
    },

    //user action function
    favor() {
      user
        .actFavor({
          user_id: this.meid,
          article_id: this.artid,
          like_status: this.detail.like_status
        })
        .then(res => {
          console.log("like res", res);
          if (res.code == "200" || res.status == "200") {
            if (this.isFavor == false) {
              this.favorNum += 1;
              this.isFavor = true;
              this.$message.success("点赞成功");
            } else {
              this.favorNum -= 1;
              this.isFavor = false;
              this.$message.success("取消点赞");
              setTimeout(() => {
                this.$router.push("/detail");
              }, 800);
            }
          } else {
            this.$message.error(res.msg);
          }
        });
    },
    follow() {
      post("/follow", {
        user_id: "1",
        followed_id: "8"
      }).then(res => {
        console.log("res", res);
        if (res.msg == "1") {
          this.$message.success("关注成功");
        } else if (res.msg == "0") {
          this.$message.success("取关成功");
        } else {
          this.$message.error(res.msg);
        }
      });
      // setTimeout(() => {
      //   this.$router.push("/user");
      // }, 1000);
    },

    //comment toolbar
    showToolbar() {
      this.hasToolbar = true;
    },
    hideToolbar() {
      this.hasToolbar = false;
    },

    //axios
    deliverComment() {}
  },
  components: {
    //emoji
    // VueFeedbackReaction,
    comment
  }
};
</script>

<style scoped>
/* common */
#detail {
  padding-bottom: 90px;
  text-align: left;
  display: flex;
}
@media (max-width: 640px) {
  #detail {
    width: 85vw;
    font-size: 14px;
  }
}
section.article-wrapper,
section.comment-wrapper {
  display: flex;
  flex-direction: column;
  margin: 30px 0;
  padding: 30px 40px;
  /* width: 800px; */
  box-shadow: 0 0 4px 0 #d0d0d0;
  border-radius: 5px;
}
section.comment-wrapper {
  padding: 40px 40px;
}

@media (max-width: 640px) {
  section.article-wrapper {
    padding: 20px 30px;
  }
  section.comment-wrapper {
    padding: 30px 30px;
  }
}

section.article-wrapper h1 {
  font-size: 30px;
  /* line-height: 3; */
}

/* article info -- author time */
section.article-wrapper .article-info {
  margin-bottom: 20px;
  color: #d0d0d0;
  font-size: 14px;
}
section.article-wrapper .article-info span {
  padding-left: 10px;
}
section.article-wrapper .article-info .author:hover {
  color: #81d4fa80;
}

/* article content style */
section.article-wrapper article p {
  margin: 10px 0;
  line-height: 2;
}

/* action button -- favor follow etc */
section.article-wrapper .action {
  margin: 20px 0;
}
/* favor button */
section.article-wrapper .action i {
  margin-right: 20px;
  padding: 5px 20px;
  font-size: 14px;
  display: inline-block;
  border: 1px solid #81d4fa;
  border-radius: 20px;
  color: #81d4fa;
  user-select: none;
}
section.article-wrapper .action i.has-favor {
  background: #81d4fa;
  color: #fff;
}
section.article-wrapper .action i:hover {
  background: #81d4fa30;
  cursor: pointer;
}
section.article-wrapper .action i.has-favor:hover {
  background: #81d4fac0;
  cursor: pointer;
}

/* follow button */
section.article-wrapper .action .el-button {
  width: 70px;
  height: 40px;
  padding: 0 10px;
  background: #fff;
  border: 1px solid #81d4fa;
  border-radius: 20px;
  color: #81d4fa;
  transition: 0.4s;
  font-size: 14px;
}
section.article-wrapper .action .el-button:hover {
  background: #81d4fa30;
  cursor: pointer;
}
section.article-wrapper .action .el-button:focus {
  outline: none;
}

/* comment */
.comment-box .toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.comment-box .left i {
  font-size: 20px;
  color: #d0d0d0;
}
.comment-box .left i:hover {
  color: #aaa;
  cursor: pointer;
}
.comment-box .right {
  display: flex;
  align-items: center;
}

/* diy element ui */
section.comment-wrapper .el-button {
  height: 30px;
  padding: 0 20px;
}
section.comment-wrapper .last-comment-item {
  border-bottom: 0;
}
.el-button {
  height: 30px;
  padding: 5px 20px;
}
.el-input {
  resize: none;
}

.el-textarea__inner:focus {
  border-color: #81d4fa;
}
</style>

<style>
.comment-wrapper .comment-box .el-textarea textarea {
  padding-top: 10px;
  resize: none;
}
</style>