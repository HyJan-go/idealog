package com.tt.idealog.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


import androidx.annotation.Nullable;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.tt.idealog.R;
import com.tt.idealog.adapter.RecommendArticlesAdapter;
import com.tt.idealog.customUI.CustomizeSearchView;
import com.tt.idealog.entity.RecommendArtiEntity;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;

public class HomeFragment extends BaseFragment implements View.OnClickListener{
    private View homeView;
    private CustomizeSearchView searchView;

    //RecyclerView的相关控件
    private List<RecommendArtiEntity> list = new ArrayList<>();
    private RecyclerView recyclerView;
    private RecommendArticlesAdapter recommendArtiAdapter;
    private LinearLayoutManager linearLayoutManager;

    //其他界面控件
    private TextView newestTextView;
    private TextView hottestTextView;
    private TextView withinWeeks;
    private TextView withinMonths;
    //判断推荐里是选择了最新还是最热，默认最新
    private int recommendState = 0;
    //判断时限，是一周内0，还是一月内1
    private int timeLimit=0;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        homeView = inflater.inflate(R.layout.fragment_home,container,false);
        initView();
        initData();
        return homeView;
    }

    /**
     * 初始化recyclerView的数据
     */
    private void initData() {
        String test = "";
        //判断是最热还是最新
        if(recommendState==0){
            //按照最新排序
            test="newest";
        }else {
            //按照一周内热度排序
            if(timeLimit==0){
                test="hottest weeks";
            }else {
                test="hottest months";
            }

        }
        RecommendArtiEntity recommendArtiEntity = new RecommendArtiEntity("","","","","");
        list.clear();
        for(int i =0;i<10;i++){
            recommendArtiEntity.setTitle(test+"标题"+i);
            recommendArtiEntity.setContent("正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容正文内容"+i);
            recommendArtiEntity.setWriter("作者"+i);
            recommendArtiEntity.setNumOfLikes(""+i);
            recommendArtiEntity.setNumOfComment(""+i*2);
            list.add(recommendArtiEntity);
        }
        recommendArtiAdapter.notifyDataSetChanged();
    }

    @Override
    public void onStart() {
        super.onStart();
        initView();
    }

    private void initView() {
    searchView = homeView.findViewById(R.id.search_view);
    searchView.setOnClickListener(this);
    recyclerView = homeView.findViewById(R.id.rv_recommend_articles);
    newestTextView = homeView.findViewById(R.id.tv_newest);
    hottestTextView = homeView.findViewById(R.id.tv_hotest);
    withinWeeks = homeView.findViewById(R.id.tv_within_weeks);
    withinMonths = homeView.findViewById(R.id.tv_within_months);
    newestTextView.setOnClickListener(this);
    hottestTextView.setOnClickListener(this);
    withinWeeks.setOnClickListener(this);
    withinMonths.setOnClickListener(this);

    linearLayoutManager = new LinearLayoutManager(getActivity());
    recyclerView.setLayoutManager(linearLayoutManager);
    recommendArtiAdapter = new RecommendArticlesAdapter(getActivity(),list);
    recyclerView.setAdapter(recommendArtiAdapter);
    }


    @Override
    public void onClick(View view) {
        switch (view.getId()){
            //如果点击了最新
            case R.id.tv_newest:
                //如果是从最热到最新
                if(recommendState==1){
                    recommendState=0;
                    newestTextView.setTextColor(getResources().getColor(R.color.black));
                    hottestTextView.setTextColor(getResources().getColor(R.color.gray));
                    withinWeeks.setVisibility(View.INVISIBLE);
                    withinMonths.setVisibility(View.INVISIBLE);
                    //刷新data
                    initData();
                }
                break;
            case R.id.tv_hotest:
                //从最新到最热
                if(recommendState==0){
                    recommendState = 1;
                    newestTextView.setTextColor(getResources().getColor(R.color.gray));
                    hottestTextView.setTextColor(getResources().getColor(R.color.black));
                    withinWeeks.setVisibility(View.VISIBLE);
                    withinMonths.setVisibility(View.VISIBLE);
                    initData();
                }
                break;
            case R.id.tv_within_weeks:
                //从一个月内变一周内
                if(timeLimit==1){
                    timeLimit = 0;
                    withinWeeks.setTextColor(getResources().getColor(R.color.black));
                    withinMonths.setTextColor(getResources().getColor(R.color.gray));
                    initData();
                }
                break;
            case R.id.tv_within_months:
                //从一周内变一月内
                if(timeLimit==0){
                    timeLimit = 1;
                    withinWeeks.setTextColor(getResources().getColor(R.color.gray));
                    withinMonths.setTextColor(getResources().getColor(R.color.black));
                    initData();
                }
                break;
        }
    }
}
