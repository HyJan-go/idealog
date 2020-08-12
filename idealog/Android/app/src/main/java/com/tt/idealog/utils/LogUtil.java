package com.tt.idealog.utils;

import android.util.Log;

/**
 * 该类用于输出和管理日志，方便调试
 */
public class LogUtil {
    private static final int VERBOSE = 1;
    private static final int DEBUG = 2;
    private static final int INFO = 3;
    private static final int WARNNING = 4;
    private static final int ERROR = 5;
    private static final int NOTHING = 6;

    //等级为VERBOSE时说明是调试时
    private  static  int level = VERBOSE;
//    private static  int level=NOTHING;

    /**
     * verbose
     * @param tag  标识活动
     * @param message 日志信息
     */
    public static  void v(String tag,String message){
        if(level<=VERBOSE){
            Log.v(tag,message);
        }
    }

    public static void d(String tag, String message) {
        if (level <= DEBUG) {
            Log.d(tag, message);
        }
    }

    public static void i(String tag, String message) {
        if (level <= INFO) {
            Log.i(tag, message);
        }
    }

    public static void w(String tag, String message) {
        if (level <= WARNNING) {
            Log.w(tag, message);
        }
    }

    public static void e(String tag, String message) {
        if (level <= ERROR) {
            Log.e(tag, message);
        }
    }
}