import { get, post } from "@/helpers/request";

export default {
  getUsers({ page_index = "1" } = { page_index: "1" }) {
    return post("/user_list_slice", {
      pageIndex: page_index
    })
  },

  addUser({work_id}){
    return post("/setUser", {
      work_id: work_id,
      name: work_id
    })
  }

  // logout() {
  //   return request('/logout')
  // },

  // getInfo() {
  //   return request('/')
  // }
}