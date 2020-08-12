package com.tt.idealog.activity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.tt.idealog.R;
import com.tt.idealog.utils.ToastUtil;

public class ModifyPasActivity extends AppCompatActivity implements View.OnClickListener {
    private EditText oldPasEditText;
    private EditText newPasEditText;
    private EditText resurePasEditText;
    private Button confirmButton;
    private Button cancelButton;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_modify_pas);
        initView();
    }

    private void initView() {
        oldPasEditText = findViewById(R.id.ed_old_pas);
        newPasEditText = findViewById(R.id.ed_new_pas);
        resurePasEditText = findViewById(R.id.ed_resure_pas);
        confirmButton = findViewById(R.id.bt_modify_pas_confirm);
        confirmButton.setOnClickListener(this);
        cancelButton = findViewById(R.id.bt_modify_pas_cancel);
        cancelButton.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()){
            case R.id.bt_modify_pas_confirm:
               modifyPas();
                break;
            case R.id.bt_modify_pas_cancel:
                startActivity(new Intent(ModifyPasActivity.this,MainActivity.class));
                finish();
                break;
        }
    }
    private void modifyPas(){
        String oldPasString = oldPasEditText.getText().toString();
        String newPasString = newPasEditText.getText().toString();
        String resurePasString = resurePasEditText.getText().toString();
        if(oldPasString.isEmpty()||newPasString.isEmpty()||resurePasString.isEmpty()){
            ToastUtil.makeText(ModifyPasActivity.this,getResources().getString(R.string.pas_empty_error));
        }else if(!newPasString.equals(resurePasString)){
            ToastUtil.makeText(ModifyPasActivity.this,getResources().getString(R.string.pas_diff_error));
        }
    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        startActivity(new Intent(ModifyPasActivity.this,MainActivity.class));
        finish();
    }
}
