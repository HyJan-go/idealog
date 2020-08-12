<template>
  <div id="info">
    <ul class="option">
      <li class="top-line">
        <div class="cell cell-left">头像</div>
        <div class="cell cell-info">
          <i class="icon-ali-avatar"></i>
          <!-- :data="uploadData" -->
          <el-upload
            name="avatar"
            class="avatar-uploader"
            :action="`http://192.168.195.10:5005/user/images/${user_id}.jpg`"
            
            :before-upload="beforeAvatarUpload"
            :on-success="handleAvatarSuccess"
            ref="newupload"
          >
            <el-button type="file" class="avatar-btn">更改头像</el-button>
          </el-upload>
        </div>
        <!-- <div class="cell cell-btn">
          <el-button></el-button>
        </div>-->
      </li>
      <li class="id-line">
        <div class="cell cell-left">工号</div>
        <div class="cell cell-info">S001</div>
        <!-- <div class="cell cell-btn">
          <el-button></el-button>
        </div>-->
      </li>
      <li class="nick-line">
        <div class="cell cell-left">昵称</div>
        <div class="cell cell-info">
          <el-input
            v-model="nick_name"
            placeholder
            type="input"
            oninput="if(value.length>10)value=value.slice(0,10)"
            clearable
          >Takai</el-input>
        </div>
      </li>
      <li class="intro-line">
        <div class="cell cell-left">个人简介</div>
        <div class="cell cell-info">
          <el-input type="textarea" :rows="4" placeholder="请输入内容" v-model="intro_text"></el-input>
        </div>
        <!-- <div class="cell cell-btn">
          <el-button></el-button>
        </div>-->
      </li>
      <li>
        <div class="cell">
          <el-button @click="saveInfo" class="save-btn">保存</el-button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id: "1",
      nick_name: "Takai",
      intro_text: "balabala巴拉巴拉balabala巴拉巴拉balabala巴拉巴拉"
    };
  },
  methods: {
    saveInfo() {
      this.$message.success("保存成功");
    },
    //el-upload
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    }
  }
};
</script>

<style>
/* common */
#info {
  padding-top: 20px;
  padding-bottom: 90px;
}
@media (max-width: 640px) {
  #info {
    width: 90vw;
  }
}
ul.option {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
ul.option li {
  display: flex;
  justify-content: center;
  align-items: center;
}

.option .cell {
  padding: 20px 20px;
  font-size: 14px;
  text-align: left;
  display: flex;
  align-items: center;
}
.option .cell i.icon-ali-avatar {
  font-size: 28px;
}
.option .cell-left {
  color: #c6c6c6;
  width: 100px;
}
.option .cell-info {
  color: #666;
  width: 300px;
}

/* diy element ui */
.save-btn,
.save-btn:hover,
.save-btn:focus {
  border-radius: 20px;
  color: #85ce61;
  border-color: #85ce61;
  outline: none;
}
.save-btn:hover{
  background: #85ce6130;
}

.avatar-btn,
.avatar-btn:hover,
.avatar-btn:focus {
  border-radius: 20px;
  margin-left: 30px;
  color: #81d4fa;
  border-color: #81d4fa;
  outline: none;
}
.avatar-btn:hover{
  background: #81d4fa30;
}

.el-textarea__inner {
  padding: 10px 14px;
  font-size: 14px;
  font-family: "Microsoft Ya Hei";
  color: inherit;
  resize: none;
}
</style>
