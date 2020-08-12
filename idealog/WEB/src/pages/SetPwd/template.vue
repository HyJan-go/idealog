<template>
  <div id="setPwd">
    <h1>Let's share</h1>
    <el-form
      :model="setPwdForm"
      :rules="rules2"
      ref="setPwdForm"
      label-width="0"
      class="demo-ruleForm"
    >
      <el-form-item prop="oldPass">
        <el-input
          placeholder="旧密码"
          type="password"
          v-model="setPwdForm.oldPass"
          auto-complete="off"
        ></el-input>
      </el-form-item>
      <el-form-item prop="pass">
        <el-input placeholder="新密码" type="password" v-model="setPwdForm.pass" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item prop="checkPass">
        <el-input
          placeholder="确认密码"
          type="password"
          v-model="setPwdForm.checkPass"
          auto-complete="off"
        ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="danger" @click="onUpdate">确定</el-button>
        <el-button type="primary" @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
// import { mapActions } from "vuex";
import { get, post } from "@/helpers/request";
import md5 from "js-md5";

export default {
  data() {
    var validateOldPass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入旧密码"));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入新密码"));
      } else if (value == this.setPwdForm.oldPass) {
        callback(new Error("新密码与旧密码相同!"));
      } else {
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.setPwdForm.pass) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    return {
      setPwdForm: {
        oldPass: "",
        pass: "",
        checkPass: ""
      },
      rules2: {
        oldPass: [{ validator: validateOldPass, trigger: "blur" }],
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }]
      }
    };
  },
  methods: {
    onUpdate() {
      console.log(this.setPwdForm.oldPass, this.setPwdForm.pass);
      post("/update_pwd", {
        user_id: "7",
        original_pwd: this.setPwdForm.oldPass,
        update_pwd: this.setPwdForm.pass
      }).then(res => {
        console.log(res);
        this.$message.success("修改成功");
        setTimeout(() => {
          this.$router.push({ path: this.$route.query.redirect || "/" });
        }, 800);
      });
    },
    cancel() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>

<style scoped>
/* common */
#setPwd {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  /* height: 40vh; */
}
@media (max-width: 640px) {
  #setPwd {
    width: 90vw;
  }
}
#setPwd h1 {
  line-height: 3;
}

.el-form-item {
  margin-bottom: 25px;
}
.el-button {
  height: 30px;
  padding: 5px 20px;
}
.el-button:hover {
  color: #fff;
  border-color: #fff;
}
</style>
