<template>
  <div id="login">
    <h1>Let's share</h1>
    <el-form
      :model="loginForm"
      :rules="loginRule"
      ref="loginForm"
      label-width="0"
      class="demo-ruleForm"
    >
      <el-form-item prop="username">
        <el-input
          placeholder="用户名"
          type="username"
          v-model="loginForm.username"
          auto-complete="off"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input placeholder="密码" type="password" v-model="loginForm.password" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
// import { mapActions } from "vuex";
import md5 from "js-md5";

export default {
  data() {
    var validateUser = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入用户名"));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      loginForm: {
        username: "",
        password: ""
      },
      loginRule: {
        username: [{ validator: validateUser, trigger: "blur" }],
        password: [{ validator: validatePass, trigger: "blur" }]
      }
    };
  },
  methods: {
    onLogin() {
      this.$refs["loginForm"].validate(valid => {
        if (valid) {
          console.log(this.loginForm.username, this.loginForm.password);
          auth.login({
            username: this.loginForm.username,
            password: md5(this.loginForm.password)
          }).then(res => {
            console.log("res", res);
            if (res.code == 200 || res.status == 200) {
              this.$message.success("登录成功");
              this.global.meid = res.id;
              setTimeout(() => {
                this.$router.push({ path: this.$route.query.redirect || "/" });
              }, 800);
            } else {
              this.$message.error(res.msg);
            }
          });
        }
      });
    }

    // ...mapActions(["login"]),

    // onLogin() {
    //   this.login({
    //     user_account: this.loginForm.username,
    //     user_password: this.loginForm.password
    //   }).then(() => {
    //     this.$router.push({ path: this.$route.query.redirect || "/" });
    //   });
    // console.log(
    //   "info: " + this.loginForm.username + ":" + this.loginForm.password
    // );
    // }

    // submitForm(formName) {
    //   this.$refs[formName].validate(valid => {
    //     if (valid) {
    //       this.$message.success("请求合法");
    //     } else {
    //       this.$message.error("请求不合法!");
    //       setTimeout(() => {
    //         return false;
    //       }, 500);
    //     }
    //   });
    // }
  }
};
</script>

<style scoped>
/* common */
#login {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  /* height: 40vh; */
}
@media (max-width: 640px) {
  #login {
    width: 90vw;
  }
}
#login h1 {
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
.el-button:hover {
  color: #fff;
}
</style>
