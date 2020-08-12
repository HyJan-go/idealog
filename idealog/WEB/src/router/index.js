import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/pages/Index/template.vue'
import Login from '@/pages/Login/template.vue'
import Create from '@/pages/Create/template.vue'
import Detail from '@/pages/Detail/template.vue'
import Edit from '@/pages/Edit/template.vue'
import Info from '@/pages/Info/template.vue'
import Register from '@/pages/Register/template.vue'
import User from '@/pages/User/template.vue'
import UserArticle from '@/pages/User/UserArticle.vue'
import UserFollow from '@/pages/User/UserFollow.vue'
import UserFans from '@/pages/User/UserFans.vue'
import Adminlogin from '@/pages/Admin_Login/template.vue'
import SetUser from '@/pages/Admin_Edit/template.vue'
import SetPass from '@/pages/SetPwd/template.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/create',
      name: 'create',
      component: Create
    },
    {
      path: '/detail/:article_id',
      name: 'detail',
      component: Detail
    },
    {
      path: '/edit',
      name: 'edit',
      component: Edit
    },
    {
      path: '/info',
      name: 'info',
      component: Info
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/user/:user_id',
      name: 'user',
      component: User,
      children:[
        {
          path: '/user/:user_id/article',
          name: 'userArticle',
          component: UserArticle
        },
        {
          path: '/user/:user_id/follow',
          name: 'userFollow',
          component: UserFollow
        },
        {
          path: '/user/:user_id/fans',
          name: 'userFans',
          component: UserFans
        }
      ]
    },
    {
      path: '/admin',
      name: 'adminlogin',
      component: Adminlogin
    },
    {
      path: '/setuser',
      name: 'setUser',
      component: SetUser
    },
    {
      path: '/setpass',
      name: 'setPass',
      component: SetPass
    },
  ]
})
