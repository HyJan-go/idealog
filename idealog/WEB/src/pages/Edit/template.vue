<template>
  <div id="edit">
    <h1 @click="publish">编辑博客</h1>

    <el-form class="blogForm">
      <el-form-item class="title-item">
        <el-input
          v-model="title_text"
          placeholder="输入标题（限30个字）"
          type="input"
          oninput="if(value.length>30)value=value.slice(0,30)"
        ></el-input>
      </el-form-item>

      <el-form-item class="tag-item">
        <el-tag
          :key="tag"
          v-for="tag in dynamicTags"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)"
        >{{tag}}</el-tag>
        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
        ></el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
      </el-form-item>

      <el-form-item class="article-item">
        <el-input v-model="article_text" placeholder="正文（至少20个字）" type="textarea" rows="15"></el-input>
      </el-form-item>
    </el-form>
    <div class="edit-btn">
      <el-button @click="publish">发布</el-button>
      <el-button @click="save">保存</el-button>
      <el-button>取消</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title_text: "你住的巷子里",
      article_text: "我租了一间公寓",
      //element ui -- tag
      dynamicTags: ["Java", "Python", "Go", "C++", "C#", "JavaScript"],
      inputVisible: false,
      inputValue: ""
    };
  },
  methods: {
    publish() {
      this.$message.success("发布成功");
      setTimeout(() => {
        this.$router.push("/detail");
      }, 1000);
    },
    save() {
      this.$message.success("保存成功");
    },
    //element ui -- tag
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    //input tag
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = "";
    }
  }
};
</script>

<style>
/* common */
#edit {
  padding-bottom: 100px;
}
#edit h1 {
  line-height: 3;
}
@media (max-width: 640px) {
  #edit {
    width: 80vw;
  }
}

.tag-item {
  text-align: left;
}

/* diy element ui */
.el-textarea__inner {
  padding: 10px 14px;
  font-family: "Microsoft Ya Hei";
}

.edit-btn .el-button,
.edit-btn .el-button:hover,
.edit-btn .el-button:focus {
  height: 30px;
  padding: 5px 20px;
  color: #81d4fa;
  border-color: #81d4fa;
  outline: none;
}
.edit-btn .el-button:hover{
  background: #81d4fa30;
}

/* element ui -- tag */
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>
