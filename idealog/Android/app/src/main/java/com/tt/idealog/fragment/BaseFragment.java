package com.tt.idealog.fragment;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.tt.idealog.utils.LogUtil;

/**
 * 这个类是所有Fragment的父类，主要用于查看和管理Fragment
 */
public class BaseFragment extends Fragment {
    //对应的fragment的名字
    private String fragmentName = getClass().getSimpleName();

    /**
     * 碎片于活动关联的时候调用
     *
     * @param context
     */
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        LogUtil.d(fragmentName, "- - - - - - - -> onAttach()");
    }

    /***
     * 活动创建中，但是没有成功创建完的时候调用，一般用于恢复子fragment的状态的
     * @param savedInstanceState
     */
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LogUtil.d(fragmentName, "- - - - - - - -> onCreate() ");
    }

    /**
     * 关联加载对应的view
     *
     * @param inflater
     * @param container
     * @param savedInstanceState
     * @return
     */
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return super.onCreateView(inflater, container, savedInstanceState);
    }

    /**
     * 活动创建成功后，可以使fragment于活动之间交互数据等操作
     *
     * @param savedInstanceState
     */
    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        super.onActivityCreated(savedInstanceState);
        LogUtil.d(fragmentName, "- - - - - - - -> onActivityCreated() ");
    }

    /**
     * 和活动的onstart状态是一致的
     */
    @Override
    public void onStart() {
        super.onStart();
        LogUtil.d(fragmentName, "- - - - - - - -> onStart()");
    }

    /**
     * 用户可以见状态和可以交互的状态
     */
    @Override
    public void onResume() {
        super.onResume();
        LogUtil.d(fragmentName, "- - - - - - - -> onResume()");
    }

    /**
     * 暂停状态，但是任然可见，不能交互
     */
    @Override
    public void onPause() {
        super.onPause();
        LogUtil.d(fragmentName, "- - - - - - - -> onPause()");
    }

    /**
     * 停止状态，fragment不可见不可交互
     */
    @Override
    public void onStop() {
        super.onStop();
        LogUtil.d(fragmentName, "- - - - - - - -> onStop()");
    }

    /**
     * 视图的销毁，但是本身的一些状态任然保存在内存中的，一般与FragmentPageAdapter结合使用的时候会通过
     * fragmentManager保存当前的fragment的一些东西，不会被销毁掉，知识销毁视图
     */
    @Override
    public void onDestroyView() {
        super.onDestroyView();
        LogUtil.w(fragmentName, "- - - - - - - -> onDestroyView()");
    }

    /**
     * 真正销毁视图等，不在内存中保留，只被保存state等信息，通过下一次savedInstanceState恢复，与
     * fragmentPagerStateAdapter结合使用就会这样
     */
    @Override
    public void onDestroy() {
        super.onDestroy();
        LogUtil.e(fragmentName, "- - - - - - - -> onDestroy()");
    }

    /**
     * 解绑当前活动与fragment的关系
     */
    @Override
    public void onDetach() {
        super.onDetach();
        LogUtil.d(fragmentName, "- - - - - - - -> onDetach()");
    }
}
