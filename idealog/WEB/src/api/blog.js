import { get, post } from '@/helpers/request'

// const URL = {
//   GET_LIST: '/deliver',
//   GET_DETAIL: '/deliver/:blog_id',
//   CREATE: '/deliver',
//   UPDATE: '/deliver/:blog_id',
//   DELETE: '/deliver/:blog_id'
// }

export default {
  getBlogs({ user_id = "1", page_index = "1", item = "2" } = { user_id: "1", page_index: "1", item: "2" }) {
    return post("/art/list", {
      user_id: user_id,
      pageIndex: page_index,
      item: item,
    })
  },

  getBlogsByUserId(user_id) {
    return this.getBlogs({ user_id })
  },

  getBlogDetailById({ user_id = "1", article_id } = { user_id: "1", article_id }) {
    return post("/art/dtl", {
      user_id: user_id,
      article_id: article_id
    })
  }

  // getBlogsByUserId(user_id) {
  //   return this.getBlogs({ user_id })
  // },

  // getBlogId({ blog_id }) {
  //   return request(URL.GET_DETAIL.replace(':blog_id'), blog_id)
  // },

  // updateBlog({ blog_id }) {
  //   return request(URL.UPDATE.replace(':blog_id', blog_id), 'PATCH', blog_id)
  // },

  // deleteBlog({ blog_id }) {
  //   return request(URL.DELETE.replace(':blog_id', blog_id), 'DELETE')
  // },

  // createBlog({ title = '', article = '' } = { title: '', article: '' }) {
  //   return request(URL.CREATE, 'POST', { title, article });
  // }
}