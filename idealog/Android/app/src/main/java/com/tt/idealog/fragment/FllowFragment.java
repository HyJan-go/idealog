package com.tt.idealog.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;

import com.tt.idealog.R;

public class FllowFragment extends BaseFragment {
    private View fllowView;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        fllowView = inflater.inflate(R.layout.fragment_fllow,container,false);
        return fllowView;
    }
}
