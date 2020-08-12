import axios from 'axios'
import Cookies from 'js-cookie'
import { Message } from 'element-ui'

//post header type
axios.defaults.headers.post['Content-Type'] = 'application/json'
// backend interface
axios.defaults.baseURL = 'http://192.168.195.10:5005'
// cookie
axios.defaults.withCredentials = false

//http request 拦截器
axios.interceptors.request.use(
  config => {
    const token = Cookies.get('token');
    if (token) {
      config.params = { 'token': token }
    }
    return config;
  },
  error => {
    return Promise.reject(err);
  }
);

//http response 拦截器
axios.interceptors.response.use(
  response => {
    console.log("response", res);
    if (response.data.status == 200) {
      console.log("success");
      return Promise.resolve(response);
    }else{
      console.log(response.data)
    }
  },
  error => {
    console.log('error')
    Message.error(error.data.msg)
    return Promise.reject(error)
  }
)

export function get(url, params) {
  return new Promise((resolve, reject) => {
    axios.get(url, {
      params: params
    }).then(res => {
      console.log(456)
      resolve(res.data)
    }).catch(err => {
      console.log(654)
      reject(err.data)
    })
  })
}

export function post(url, params) {
  return new Promise((resolve, reject) => {
    axios.post(url, params)
      .then(res => {
        console.log(123)
        resolve(res.data);
      })
      .catch(err => {
        console.log(32111)
        reject(err.data)
      });
  })
}



// console.log(this.loginForm.username, this.loginForm.password);
//   axios
//     .post(
//       "/login",
//       {
//         user_account: this.loginForm.username,
//         user_password: md5(this.loginForm.password)
//       },
//       {
//         headers: {
//           token: window.localStorage.getItem("token") //由于是多页面应用所以token存储在本地localStorage中
//         }
//       }
//     )
//     .then(res => {
//       console.log("response", res);
//       if (res.data.code == "200") {
//         this.$router.push({ path: this.$route.query.redirect || "/" });
//         // resolve(res.data);
//       } else {
//         Message.error(res.data.msg);
//         // reject(res.data);
//       }
//     })
//     .catch(err => {
//       Message.error("网络异常");
//       // reject({ msg: "网络异常" });
//     });