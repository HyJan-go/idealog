<template>
  <div>
    <div class="titlec">粉丝</div>
    <ul v-for="fan in fans" :key="fan.user_id" class="fans-list">
      <Fansli v-if="flag" :fan="fan" :visitor="fan.user_id" />
    </ul>
  </div>
</template>

<script>
import Fansli from "@/components/Fansli";

export default {
  data() {
    return {
      flag: false,
      fans: []
    };
  },
  created() {
    user.getFans({ user_id: "2" }).then(res => {
      console.log("res", res);
      if (res.length != 0) {
        this.fans = res;
        this.flag = true;
      } else {
        // this.$message.error("未查询到粉丝");
      }
    });
  },
  components: {
    Fansli
  }
};
</script>

<style>
.titlec {
  font-size: 14px;
  padding-bottom: 20px;
  padding-left: 20px;
  text-align: left;
}
</style>