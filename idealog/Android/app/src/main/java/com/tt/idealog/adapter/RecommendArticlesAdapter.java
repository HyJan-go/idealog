package com.tt.idealog.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.tt.idealog.R;
import com.tt.idealog.entity.RecommendArtiEntity;
import com.tt.idealog.utils.ToastUtil;

import java.util.ArrayList;
import java.util.List;

public class RecommendArticlesAdapter extends RecyclerView.Adapter {
    List<RecommendArtiEntity> items = new ArrayList<>();
    Context context ;


    public RecommendArticlesAdapter(Context context, List<RecommendArtiEntity> items) {
        this.items = items;
        this.context = context;
    }

    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.view_rv_item_main, parent, false);
        return new RecArtiViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
        RecommendArtiEntity recommandArtiItem = items.get(position);
        ((RecArtiViewHolder)holder).titleTextView.setText(recommandArtiItem.getTitle());
        ((RecArtiViewHolder)holder).contentTextView.setText(recommandArtiItem.getContent());
        ((RecArtiViewHolder)holder).writerTextView.setText(recommandArtiItem.getWriter());
        ((RecArtiViewHolder)holder).numOfLikesTextView.setText(recommandArtiItem.getNumOfLikes());
        ((RecArtiViewHolder)holder).numOfCommentTextView.setText(recommandArtiItem.getNumOfComment());
    }

    @Override
    public int getItemCount() {
        return items.size();
    }



    public class RecArtiViewHolder extends RecyclerView.ViewHolder{
        private TextView titleTextView;
        private TextView contentTextView;
        private TextView writerTextView;
        private TextView numOfLikesTextView;
        private TextView numOfCommentTextView;


       public RecArtiViewHolder(final View view){
           super(view);
           view.setOnClickListener(new View.OnClickListener() {
               @Override
               public void onClick(View v) {
                   //点击事件
               }
           });
           titleTextView = view.findViewById(R.id.tv_title);
            contentTextView = view.findViewById(R.id.tv_content);
            writerTextView = view.findViewById(R.id.tv_writer_name);
            numOfLikesTextView = view.findViewById(R.id.tv_num_of_like);
            numOfCommentTextView = view.findViewById(R.id.tv_num_of_comment);
        }
    }
}






