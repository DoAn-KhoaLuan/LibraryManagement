package com.LibraryManagementGroup.LibraryManagement;
import com.LibraryManagementGroup.LibraryManagement.entity.Province;
import com.LibraryManagementGroup.LibraryManagement.repository.ProvinceRepository;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import springfox.documentation.swagger2.annotations.EnableSwagger2;




@SpringBootApplication
@EnableSwagger2
public class LibraryManagementApplication {
	public static void main(String[] args) {
		SpringApplication.run(LibraryManagementApplication.class, args);
	}
}
