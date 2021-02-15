package com.LibraryManagementGroup.LibraryManagement.common.utils;

import java.util.HashMap;

public class ValidationHandler {

    public static Boolean validateWithHashMap(String keys[], HashMap<String,String> request) throws Exception{
        Boolean status = false;
        try {
            for(int start = 0;start<keys.length;start++) {
                if(request.containsKey(keys[start])) {//not exist
                    if(request.get(keys[start]).equals("")){//if empty
                        throw new Exception(keys[start]+" không được trống");
                    }
                }else {
                    throw new Exception(keys[start]+" không tồn tại");
                }
            }
        }catch(Exception e) {
            e.printStackTrace();
            throw new Exception("Lỗi: " + e.getMessage());
        }
        status = true;
        return status;
    }

}
