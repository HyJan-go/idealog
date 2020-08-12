package com.tt.idealog.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;

import com.tt.idealog.R;

public class NotificationFragment extends BaseFragment {
    private View notifView;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        notifView = inflater.inflate(R.layout.fragment_notification,container,false);
        return notifView;
    }
}
