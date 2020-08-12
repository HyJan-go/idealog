package com.tt.idealog.fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.tt.idealog.R;
import com.tt.idealog.adapter.RecommendArticlesAdapter;
import com.tt.idealog.entity.RecommendArtiEntity;

import java.util.ArrayList;
import java.util.List;

public class ArticlesListFragment extends BaseFragment {
    private List<RecommendArtiEntity> list = new ArrayList<>();
    private RecyclerView recyclerView;
    private RecommendArticlesAdapter recommandArtiAdapter;
    private LinearLayoutManager linearLayoutManager;
    private View view;


    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.fragment_articles_list,container,false);
        initData();
        initView();
        return super.onCreateView(inflater, container, savedInstanceState);
    }

    /**
     * 初始化数据
     */
    private void initData() {
        RecommendArtiEntity recommandArtiEntity = new RecommendArtiEntity("","","","","");
        for(int i =0;i<10;i++){
            recommandArtiEntity.setTitle("标题"+i);
            recommandArtiEntity.setContent("正文内容"+i);
            recommandArtiEntity.setWriter("作者"+i);
            recommandArtiEntity.setNumOfLikes(""+i);
            recommandArtiEntity.setNumOfComment(""+i*2);
            list.add(recommandArtiEntity);
        }
    }

    /**
     * 初始化RecycleView并填充数据
     */
    private void initView() {
        linearLayoutManager = new LinearLayoutManager(getActivity());
        recyclerView.setLayoutManager(linearLayoutManager);
        recommandArtiAdapter = new RecommendArticlesAdapter(getActivity(),list);
        recyclerView.setAdapter(recommandArtiAdapter);
    }
}
