package com.tt.idealog.customUI;

import android.content.Context;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;

import com.tt.idealog.R;

public class CustomizeSearchView extends LinearLayout implements TextWatcher, View.OnClickListener{

    private EditText etSearch;
    private Button btClear;

    public CustomizeSearchView(Context context, AttributeSet ars) {
        super(context,ars);
        LayoutInflater.from(context).inflate(R.layout.view_searchview,this,true);
        etSearch = findViewById(R.id.et_search);
        etSearch.addTextChangedListener(this);

        btClear = findViewById(R.id.bt_clear);
        btClear.setVisibility(GONE);
        btClear.setOnClickListener(this);
    }

    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    /****
     * 对用户输入文字的监听
     *
     * @param editable
     */
    @Override
    public void afterTextChanged(Editable editable) {
        //获取输入文字
        String input = etSearch.getText().toString().trim();
        if (input.isEmpty()) {
            btClear.setVisibility(GONE);
        } else {
            btClear.setVisibility(VISIBLE);
        }
    }

    @Override
    public void onClick(View view) {
        etSearch.setText("");
    }
}
