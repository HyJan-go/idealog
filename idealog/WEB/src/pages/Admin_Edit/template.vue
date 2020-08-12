<template>
  <div id="admin-edit">
    <h1>管理用户</h1>
    <div class="control-btns">
      <!-- <el-button class="select-btn" round @click="toggleSelection()">全选</el-button> -->
      <el-button round @click="confirm('封禁')" type="danger">封禁</el-button>
      <el-button round @click="confirm('正常')" type="primary">解封</el-button>
      <el-button class="add-btn" round @click="enterUserInfo()">录入</el-button>
    </div>
    <!-- ref="multipleTable" -->
    <!-- @selection-change="handleSelectionChange" -->
    <el-table class="user-list" :data="users" tooltip-effect="dark">
      <!-- <el-table-column type="selection" width="55"></el-table-column> -->
      <el-table-column prop="work_id" label="工号" width="80"></el-table-column>
      <el-table-column prop="nick_name" label="昵称" width="100"></el-table-column>
      <el-table-column prop="status" label="状态" width="80">
        <template slot-scope="scope">
          <el-tag
            :type="getTagType(scope.row.status)"
            close-transition
            size="small"
          >{{getTagName(scope.row.status)}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="90">
        <template slot-scope="scope">
          <el-button class="func-btn"
            v-if="scope.row.status=='0'"
            size="mini"
            type="danger"
            @click="handleEdit(scope.$index, scope.row);confirm('1')"
          >封禁</el-button>
          <el-button class="func-btn"
            v-else
            size="mini"
            type="primary"
            @click="handleDelete(scope.$index, scope.row);confirm('0')"
          >解封</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="pagi-wrapper" v-if="pagenavshow">
      <el-pagination class="pagi" background layout="prev, pager, next" :total="50"></el-pagination>
    </div>
  </div>
</template>

<script>
import { get, post } from "@/helpers/request";

export default {
  data() {
    return {
      sum: 100,
      curpage: "1",
      users: [],
      multipleSelection: []
    };
  },

  created() {
    admin.getUsers().then(res => {
      // console.log("userInfo res", res);
      if (res.length != 0) {
        this.users = res;
        this.flag = true;
      } else {
        this.$message.error("未查询到用户哦，录入一个呗");
      }
    });
  },

  methods: {
    //toggle
    toggleSelection() {
      this.$refs.multipleTable.toggleAllSelection();
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },

    //page navigation
    pageclick: function(item) {
      this.curpage = item;
      console.log(this.curpage);
    },

    //add user
    enterUserInfo() {
      this.$prompt("输入员工工号", "录入", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        inputPattern: /^[A-Z][0-9]{3}$/,
        inputErrorMessage: "工号格式S001 (字母大写)"
      }).then(({ value }) => {
        admin.addUser({ value }).then(res => {
          if (res.code == "200" || res.status == "200") {
            var user = {
              id: value,
              name: value,
              status: "0"
            };
            this.users.push(user);
            this.$message({
              type: "success",
              message: "成功录入工号" + value
            });
            setTimeout(() => {
              this.$router.push("/setUser");
            }, 1000);
          } else {
            this.$message.error(res.data.msg);
          }
        });
      });
      // .catch(() => {
      //   this.$message({
      //     type: "info",
      //     message: "取消录入"
      //   });
      // });
    },

    addRequest() {},

    confirm(state) {
      //state 1 封禁  0 解封
      // if (this.multipleSelection.length === 0) {
      //   this.$message.warning("请至少勾选一项，再进行操作");
      // } else {
      let confirmMsg = state === "1" ? "确认封禁?" : "确认解封?",
        successMsg = state === "1" ? "封禁成功" : "解封成功",
        cancelMsg = state === "1" ? "已取消封禁" : "已取消解封";
      this.$confirm(confirmMsg, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.$message({
            type: "success",
            message: successMsg
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: cancelMsg
          });
        });
      // }
    },

    //tag
    getTagType(status) {
      const typeMap = {
        0: "primary",
        1: "danger",
        null: ""
      };
      return typeMap[status];
    },
    getTagName(status) {
      const nameMap = {
        0: "正常",
        1: "封禁",
        null: "null"
      };
      return nameMap[status];
    },

    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    }
  },
  computed: {
    pagenavshow: function() {
      if (this.sum == 1) {
        return false;
      } else {
        return true;
      }
    },

    shownot: function() {
      if (this.sum < 12) {
        return true;
      } else {
        return false;
      }
    },
    firstsum: function() {
      if (this.curpage < 6) {
        return [1, 2, 3, 4, 5, 6, 7];
      } else {
        return 1;
      }
    },
    middlesum: function() {
      var cpage = this.curpage;
      if (this.curpage < 6 || this.curpage > this.sum - 4) {
        return false;
      } else {
        return [cpage - 2, cpage - 1, cpage, cpage + 1, cpage + 2];
      }
    },
    lastsum: function() {
      if (this.curpage < this.sum - 3) {
        return [this.sum];
      } else {
        return [
          this.sum - 5,
          this.sum - 4,
          this.sum - 3,
          this.sum - 2,
          this.sum - 1,
          this.sum
        ];
      }
    },
    secondpot: function() {
      if (this.curpage < 6 || this.curpage > this.sum - 4) {
        return false;
      } else {
        return true;
      }
    }
  }
};
</script>

<style scoped>
/* common */
#admin-edit {
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: 0;
  padding-bottom: 60px;
}
#admin-edit {
  line-height: 3;
}
@media (max-width: 640px) {
  #admin-edit {
    width: 90vw;
  }
}
.control-btns {
  margin-bottom: 10px;
}
/* .add-btn{
  padding: 0;
  width: 40px;
  height: 40px;
} */

.user-list {
  width: 600px;
}

.pagi-wrapper {
  margin: 20px 0;
}
.pagi-wrapper .pagi {
  font-family: "Microsoft Ya Hei";
  font-weight: normal;
}

/* diy element ui */
.control-btns .el-button {
  height: 30px;
  padding: 5px 20px;
  font-size: 12px;
}
.control-btns .el-button:hover {
  color: #fff;
  border-color: #fff;
}
.control-btns .add-btn,
.control-btns .add-btn:hover,
.control-btns .add-btn:focus {
  border-radius: 20px;
  color: #81d4fa;
  border-color: #81d4fa;
  outline: none;
}
.control-btns .add-btn:hover {
  background: #81d4fa30;
}
.func-btn{
  border-radius: 20px;
}
</style>

<style>
.el-table .el-table__body-wrapper table,
.el-table .el-table__footer-wrapper table,
.el-table .el-table__header-wrapper table {
  margin: auto;
  font-size: 12px;
}
</style>