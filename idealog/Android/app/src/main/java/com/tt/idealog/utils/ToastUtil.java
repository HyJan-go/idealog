package com.tt.idealog.utils;

import android.content.Context;
import android.widget.Toast;

/**
 * 在测试过程，发现如果不断弹出toast出来，可能会影响程序的进行，故设置该类，来防止一个类弹出过多的toast
 */
public class ToastUtil {
    private static Toast toast ;

    public  static void makeText(Context context, String messages){

        if(toast ==null){
            toast= Toast.makeText(context,messages,Toast.LENGTH_SHORT);
        }else{
            toast.setText(messages);
        }
        toast.show();
    }
}
