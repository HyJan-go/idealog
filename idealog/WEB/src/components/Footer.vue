<template>
  <footer>
    <p class="footer-info">idealog 2019</p>
    <p style="cursor: default;" class="footer-info" @click="egg">powered by tt-mpc03</p>
  </footer>
</template>

<style scoped>
footer {
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 80px;
  width: 100vw;
  background: #fff;
  border-top: 1px solid #e6e6e6;
  position: fixed;
  bottom: 0;
  color: #c9c9c9;
  box-shadow: 0 -1px 5px 0 #e6e6e6;
  z-index: 5;
}
footer .footer-info {
  font-size: 12px;
  margin: 0;
  cursor: default;
}

@media (max-width: 500px) {
  footer {
    height: 60px;
    line-height: 1.5;
  }
  footer .footer-info {
    transform: scale(0.8);
  }
}
</style>

<script>
export default {
  methods: {
    egg() {
      this.$router.push({path:"/admin"});
    }
  }
};
</script>