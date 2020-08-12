package com.tt.idealog.adapter;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import java.util.List;

/**
 * 用于管理主活动碎片切换
 */
public class MainFragmentPagerAdapter extends FragmentPagerAdapter {
    //要切换的fragment 列表
    private List<Fragment> fragmentList;

    /**
     * 构造方法，接受一个FragmentManager 作为fragment的管理者来使用，并接受fragment列表，
     * 方便FragmentManager管理
     *
     * @param fragmentManager 管理者
     * @param fragmentList    要切换的fragment列表
     */
    public MainFragmentPagerAdapter(FragmentManager fragmentManager, List<Fragment> fragmentList) {
        //继承父类的一些特性
        super(fragmentManager);
        this.fragmentList = fragmentList;
    }


    /***
     * 下面两个方法是一定要实现的
     * 该方法是得到当前切换到的fragment对象
     * @param position 位置，从0开始
     * @return
     */
    @Override
    public Fragment getItem(int position) {
        return fragmentList.get(position);
    }

    /***
     * 这个方法是返回fragment的个数，管理起来不会出现越界的问题
     * @return
     */
    @Override
    public int getCount() {
        return fragmentList.size();
    }
}
