package com.tt.idealog.activity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.tt.idealog.R;
import com.tt.idealog.utils.ToastUtil;

/**
 * 该活动为登录页面
 */
public class LoginActivity extends AppCompatActivity implements View.OnClickListener{
    private Button loginButton;
    private EditText jobNumEditText;
    private EditText pasEditText;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        initView();
    }

    /***
     * 初始化控件
     */
    private void initView() {
        loginButton = findViewById(R.id.bt_login);
        loginButton.setOnClickListener(this);
        jobNumEditText = findViewById(R.id.ed_job_num);
        pasEditText = findViewById(R.id.ed_pas);
    }

    /**
     * 处理点击事件
     * @param view
     */
    @Override
    public void onClick(View view) {
        switch (view.getId()){
            //处理登录逻辑
            case R.id.bt_login:
                //后面补上网络请求和处理
                //doLogin();
                login("","");
                break;
        }
    }

    /**
     * 对登录做处理工作,以及发起登录请求
     */
    private void doLogin(){
        //首先判断输入的合法性
        String jobNumString = jobNumEditText.getText().toString();
        String pasString = pasEditText.getText().toString();
        if(jobNumString.isEmpty()||pasString.isEmpty()){
            ToastUtil.makeText(LoginActivity.this,getResources().getString(R.string.login_empty_error));
        }else {
            //此处发起登录请求，验证密码以及工号是否正确
        }
    }
    //登录成功跳转页面
    private void login(String jobNumString,String pasString){
        //保存登录成功后的账号和密码，方便下次登录不用输密码和账号
//       SharedPreferences share = getSharedPreferences("login", MODE_PRIVATE);
//       SharedPreferences.Editor editor = share.edit();
//       editor.putString("jobNum", jobNumString);
//       editor.putString("password", pasString);
//       editor.putBoolean("successLogin", true);
//       editor.apply();
        Intent intent = new Intent(LoginActivity.this,MainActivity.class);
        startActivity(intent);
        LoginActivity.this.finish();
    }
    long waitTime = 2000;
    long touchTime = 0;
    @Override
    public void onBackPressed(){
        long currentTime = System.currentTimeMillis();
        if((currentTime-touchTime)>=waitTime) {
            //让Toast的显示时间和等待时间相同
            ToastUtil.makeText(this, "再按一次退出");
            touchTime = currentTime;
        }else {
            finish();
        }
    }
}
