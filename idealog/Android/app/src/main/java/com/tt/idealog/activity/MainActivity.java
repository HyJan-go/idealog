package com.tt.idealog.activity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.viewpager.widget.ViewPager;

import com.tt.idealog.R;
import com.tt.idealog.adapter.MainFragmentPagerAdapter;
import com.tt.idealog.fragment.FllowFragment;
import com.tt.idealog.fragment.HomeFragment;
import com.tt.idealog.fragment.NotificationFragment;
import com.tt.idealog.fragment.PersonalMesFragment;
import com.tt.idealog.utils.ToastUtil;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{
    private ViewPager viewPager;
    private MainFragmentPagerAdapter fragmentPagerAdapter;
    private List<Fragment> fragmentList = new ArrayList<>();

    //导航栏控件
    private ImageView homeImg;
    private ImageView fllowImg;
    private ImageView notifImg;
    private ImageView personalMesImg;
    private TextView homeText;
    private TextView fllowText;
    private TextView notifText;
    private TextView personalMesText;
    private RelativeLayout homeLayout;
    private RelativeLayout fllowLayout;
    private RelativeLayout notifLayout;
    private RelativeLayout personalMesLayout;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
        initFragmentList();
    }

    @Override
    protected void onResume() {
        super.onResume();
        initFragment();
    }

    /**
     * 注册控件
     */
    private void initView() {
        viewPager = (ViewPager)findViewById(R.id.vp_main);

        homeImg = findViewById(R.id.img_nav_home);
        homeText = findViewById(R.id.tv_nav_home);
        homeLayout = findViewById(R.id.lo_nav_home);
        homeLayout.setOnClickListener(this);

        fllowImg = findViewById(R.id.img_nav_fllow);
        fllowText = findViewById(R.id.tv_nav_fllow);
        fllowLayout = findViewById(R.id.lo_nav_fllow);
        fllowLayout.setOnClickListener(this);

        notifImg = findViewById(R.id.img_nav_notif);
        notifText = findViewById(R.id.tv_nav_notif);
        notifLayout = findViewById(R.id.lo_nav_notif);
        notifLayout.setOnClickListener(this);

        personalMesImg = findViewById(R.id.img_nav_per_mes);
        personalMesText = findViewById(R.id.tv_nav_per_mes);
        personalMesLayout = findViewById(R.id.lo_nav_per_mes);
        personalMesLayout.setOnClickListener(this);

    }

    /**
     * 初始化ViewPager并处理滑动事件
     */
    private void initFragmentList(){
        //将Fragment添加到fragmentList中
        fragmentList.add(new HomeFragment());
        fragmentList.add(new FllowFragment());
        fragmentList.add(new NotificationFragment());
        fragmentList.add(new PersonalMesFragment());
    }
    private void initFragment(){
        //将fragment列表传给Adapter
        fragmentPagerAdapter= new MainFragmentPagerAdapter(getSupportFragmentManager(),fragmentList);
        viewPager.setAdapter(fragmentPagerAdapter);
        //导航栏相应选项被选择后换成高亮图标
        viewPager.addOnPageChangeListener(new ViewPager.SimpleOnPageChangeListener() {
            @Override
            public void onPageSelected(int position) {
                super.onPageSelected(position);
                refreshViewPager();
                switch (position){
                    case 0:
                        homeImg.setImageResource(R.drawable.home_selected);
                        homeText.setTextColor(getResources().getColor(R.color.selected));
                        break;
                    case 1:
                        fllowImg.setImageResource(R.drawable.fllow_selected);
                        fllowText.setTextColor(getResources().getColor(R.color.selected));
                        break;
                    case 2:
                        notifImg.setImageResource(R.drawable.notification_sellected);
                        notifText.setTextColor(getResources().getColor(R.color.selected));
                        break;
                    case 3:
                        personalMesImg.setImageResource(R.drawable.personal_mes_selected);
                        personalMesText.setTextColor(getResources().getColor(R.color.selected));
                        break;
                    default:
                        break;
                }
            }
        });
    }
    /**
     * 将导航栏的所有图标设为未选中状态
     */
    private void refreshViewPager(){
        homeImg.setImageResource(R.drawable.home_unselect);
        fllowImg.setImageResource(R.drawable.fllow_unselect);
        notifImg.setImageResource(R.drawable.notification_unsellect);
        personalMesImg.setImageResource(R.drawable.personal_mes_unselect);
        homeText.setTextColor(getResources().getColor(R.color.unselect));
        fllowText.setTextColor(getResources().getColor(R.color.unselect));
        notifText.setTextColor(getResources().getColor(R.color.unselect));
        personalMesText.setTextColor(getResources().getColor(R.color.unselect));
    }

    /**
     * 处理点击事件
     * @param view
     */
    @Override
    public void onClick(View view) {
        switch (view.getId()){
            case R.id.lo_nav_home:
                viewPager.setCurrentItem(0);
                break;
            case R.id.lo_nav_fllow:
                viewPager.setCurrentItem(1);
                break;
            case R.id.lo_nav_notif:
                viewPager.setCurrentItem(2);
                break;
            case R.id.lo_nav_per_mes:
                viewPager.setCurrentItem(3);
                break;
        }
    }
    long waitTime = 2000;
    long touchTime = 0;
    @Override
    public void onBackPressed(){
        long currentTime = System.currentTimeMillis();
        if((currentTime-touchTime)>=waitTime) {
            //让Toast的显示时间和等待时间相同
            ToastUtil.makeText(this, "再按一次退出应用");
            touchTime = currentTime;
        }else {
            finish();
        }
    }
}
