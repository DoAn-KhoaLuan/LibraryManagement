package com.LibraryManagementGroup.LibraryManagement;
import common.utils.Util;
import net.minidev.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class LibraryManagementApplication {
	public static void main(String[] args) {
		JSONObject districts = Util.getDistrictsToDBFromEtopApi();
//		SpringApplication.run(LibraryManagementApplication.class, args);
	}

}
