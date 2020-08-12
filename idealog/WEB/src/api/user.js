import { get, post } from "@/helpers/request";

export default {
  getFollows({ user_id = "1" } = { user_id: "1" }) {
    return post("/follow_list", {
      user_id: user_id
    })
  },

  getFans({ user_id = "1" } = { user_id: "1" }) {
    return post("/get_fans", {
      user_id: user_id
    })
  },

  getUserInfo({ user_id = "", host_id = "1" } = { user_id: "", host_id: "1" }) {
    return get("/get_user_profile", {
      visit_user_id: user_id,
      host_user_id: host_id
    })
  },

  actFavor({ user_id = "1", article_id, like_status } = { user_id: "1", article_id, like_status }) {
    return post("/like", {
      user_id: user_id,
      article_id: article_id,
      like_action: like_status == "1" ? "0" : "1"
    })
  },

  actFollow({ user_id = "1", followed_id } = { user_id: "1", followed_id }) {
    return post("/follow", {
      user_id: user_id,
      followed_id: followed_id
    })
  }
}