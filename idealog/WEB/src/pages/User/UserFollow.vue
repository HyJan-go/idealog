<template>
  <div>
    <div class="titlec">关注</div>
    <ul v-for="follower in follows" :key="follower.user_id" class="follows-list">
      <Followli v-if="flag" :follower="follower" @onfollow="refresh" />
    </ul>
  </div>
</template>

<script>
import Followli from "@/components/Followli";
export default {
  data() {
    return {
      flag: false,
      follows: []
    };
  },
  created() {
    user.getFollows({ user_id:"1" }).then(res => {
      console.log("res", res);
      if (res.length != 0) {
        this.follows = res;
        this.flag = true;
      } else {
        // this.$message.error("未查询到关注");
      }
    });
  },
  methods:{
    refresh(){
      this.$router.go(0);
    }
  },
  components: {
    Followli
  }
};
</script>

<style>

</style>