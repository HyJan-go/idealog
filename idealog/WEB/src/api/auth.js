import { get, post } from "@/helpers/request";

export default {
  login({ username, password }) {
    return post("/login", {
      user_account: username,
      user_password: password
    })
  },

  alogin({ username, password }) {
    return post("/ad/login", {
      admin_name: username,
      password: password
    })
  },

  // logout() {
  //   return request('/logout')
  // },

  // getInfo() {
  //   return request('/')
  // }
}