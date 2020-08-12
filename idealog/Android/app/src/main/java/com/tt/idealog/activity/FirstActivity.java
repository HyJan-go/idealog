package com.tt.idealog.activity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.tt.idealog.R;

/***
 * 整个应用的启动页
 */
public class FirstActivity extends AppCompatActivity {
    //跳转至主界面的标记
    private static final int GO_TO_MAIN_ACTIVITY = 1;
    //跳转至登录界面的标记
    private static final int GO_TO_LOGIN_ACTIVITY = 2;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first);
        initView();
    }

    private Handler handler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                //跳到主界面
                case GO_TO_MAIN_ACTIVITY:
                    startActivity(new Intent(FirstActivity.this, MainActivity.class));

                    break;
                //跳到登录界面
                case GO_TO_LOGIN_ACTIVITY:
                    startActivity(new Intent(FirstActivity.this, LoginActivity.class));
                    finish();
                    break;
            }
        }
    };

    //读取SharePreference是否有存好的账号密码，如果有，直接提交跳去主界面，否则跳转登陆页面
    private void initView() {
//        SharedPreferences sharedPreferences = getSharedPreferences("login", MODE_PRIVATE);
//        if(sharedPreferences.getBoolean("successLogin",false)){
//            //验证登录，如果成功则跳转至主页面
//           goToMainActivity();
//        }else {
//            goToLoginActivity();
//
//        }
        goToMainActivity();
    }

    /**
     * 延迟1.5秒跳转至登录界面
     */
    private void goToLoginActivity() {
        Message message = Message.obtain();
        message.what = GO_TO_LOGIN_ACTIVITY;
        handler.sendMessageDelayed(message, 1500);
    }

    /**
     * 延迟1.5秒跳转至主界面
     */
    private void goToMainActivity() {
        Message message = Message.obtain();
        message.what = GO_TO_MAIN_ACTIVITY;
        handler.sendMessageDelayed(message, 1500);
    }
    @Override
    protected void onPause() {
        super.onPause();
        finish();
    }
}
