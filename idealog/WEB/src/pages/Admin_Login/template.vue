<template>
  <div id="admin-login">
    <h1>admin</h1>
    <el-form
      :model="aloginForm"
      :rules="aloginRule"
      ref="aloginForm"
      label-width="0"
      class="demo-ruleForm"
    >
      <el-form-item prop="account">
        <el-input
          placeholder="管理员"
          type="username"
          v-model="aloginForm.account"
          auto-complete="off"
        ></el-input>
      </el-form-item>
      <el-form-item prop="passwd">
        <el-input placeholder="密码" type="password" v-model="aloginForm.passwd" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import md5 from "js-md5";

export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      //ref and rule
      aloginForm: {
        account: "",
        passwd: ""
      },
      aloginRule: {
        account: [{ validator: validatePass, trigger: "blur" }],
        passwd: [{ validator: validatePass2, trigger: "blur" }]
      }
    };
  },
  methods: {
    onLogin() {
      this.$refs["aloginForm"].validate(valid => {
        if (valid) { //validate null or not
          console.log(this.aloginForm.account, this.aloginForm.passwd);
          auth.alogin({  //request
            username: this.aloginForm.account,
            password: this.aloginForm.passwd
          }).then(res => {  //get data
            console.log("res", res);
            if (res.code == 200 || res.status == 200) {
              this.$message.success("成功登录");
              setTimeout(() => {
                this.$router.push({
                  path: this.$route.query.redirect || "/setUser"
                });
              }, 800);
            } else {
              this.$message.error(res.msg);
            }
          });
        }
      });
    }
  }
};
</script>

<style scoped>
/* common */
#admin-login {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  /* height: 40vh; */
  /* z-index: -5; */
}
@media (max-width: 640px) {
  #admin-login {
    width: 90vw;
  }
}
#admin-login h1 {
  line-height: 3;
}

/* diy element ui */
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
