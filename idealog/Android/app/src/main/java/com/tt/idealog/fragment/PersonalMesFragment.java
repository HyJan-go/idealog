package com.tt.idealog.fragment;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;

import com.tt.idealog.R;
import com.tt.idealog.activity.LoginActivity;
import com.tt.idealog.activity.ModifyPasActivity;

public class PersonalMesFragment extends BaseFragment implements View.OnClickListener{
    private View personalMesView;
    private Button modifyPasButton;
    private Button logoutButton;
    private TextView writeArticle;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
      personalMesView = inflater.inflate(R.layout.fragment_per_mes,container,false);
      initView();
      return personalMesView;
    }

    private void initView() {
        modifyPasButton = personalMesView.findViewById(R.id.bt_modify_pas);
        modifyPasButton.setOnClickListener(this);
        logoutButton = personalMesView.findViewById(R.id.bt_logout);
        logoutButton.setOnClickListener(this);
        writeArticle = personalMesView.findViewById(R.id.tv_white_article);
        writeArticle.setOnClickListener(this);
    }


    @Override
    public void onClick(View view) {
        switch (view.getId()){
            //跳转至修改密码
            case R.id.bt_modify_pas:
               startActivity(new Intent(getActivity(), ModifyPasActivity.class));

                break;
                //跳转至登录页面，同时清空登录数据
            case R.id.bt_logout:
                //后面补上清空登录数据操作
                startActivity(new Intent(getActivity(), LoginActivity.class));
                getActivity().finish();
                break;
            case R.id.tv_white_article:
                //跳转到编辑文章界面
                break;
        }
    }
}
