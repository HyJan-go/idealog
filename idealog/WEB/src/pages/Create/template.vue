<template>
  <div id="create">
    <h1 @click="publish">创建博客</h1>

    <el-form :model="createForm" :rules="createRule" ref="createForm" class="blogForm">
      <el-form-item class="title-item">
        <el-input
          v-model="createForm.title_text"
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
        <el-input
          v-model="createForm.content_text"
          placeholder="正文（至少20个字）"
          type="textarea"
          rows="15"
        ></el-input>
      </el-form-item>
    </el-form>
    <el-button @click="publish">发布</el-button>
    <el-button @click="save">保存</el-button>
    <el-button @click="cancel">取消</el-button>
  </div>
</template>

<script>
import { get, post } from "@/helpers/request";

export default {
  data() {
    var validateTitle = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("标题别空着呀"));
      } else {
        callback();
      }
    };
    var validateContent = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("写点内容呗"));
      } else {
        callback();
      }
    };
    return {
      //ref and rule
      createForm: {
        title_text: "",
        content_text: ""
      },
      createRule: {
        title_text: [{ validator: validateTitle, trigger: "blur" }],
        content_text: [{ validator: validateContent, trigger: "blur" }]
      },

      //element ui -- tag
      dynamicTags: ["Java", "Python", "Go", "C++", "C#", "JavaScript"],
      inputVisible: false,
      inputValue: ""
    };
  },
  methods: {
    publish() {
      this.$refs["createForm"].validate(valid => {
        if (valid) {
          post("/deliver", {
            user_id: "8",
            title: this.createForm.title_text,
            content: this.createForm.content_text,
            tag_id: "5",
            category_id: "3",
            tag_name: "python"
          }).then(res => {
            console.log(res);
            this.$message.success("发布成功");

            setTimeout(() => {
              this.$router.push("/detail");
            }, 800);
          });
        }
      });
    },
    save() {
      this.$message.success("保存成功");
    },
    cancel() {
      this.$confirm("确定取消?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      }).then(() => {
        this.$message({
          type: "success",
          message: "已取消"
        });
        this.$router.push("/");
      });
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

<style scoped>
/* common */
#create {
  padding-bottom: 100px;
}
#create h1 {
  line-height: 3;
}
@media (max-width: 640px) {
  #create {
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

/* element ui -- tag */
.el-tag {
  margin-right: 10px;
}
.button-new-tag {
  margin-right: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-right: 10px;
  vertical-align: bottom;
}
</style>
