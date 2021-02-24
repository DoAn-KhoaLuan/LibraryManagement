package com.LibraryManagementGroup.LibraryManagement.service.AppService;

import com.LibraryManagementGroup.LibraryManagement.entity.Category;
import com.LibraryManagementGroup.LibraryManagement.repository.CategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;

@Service
public class AppService implements IAppService {
    @Autowired
    CategoryRepository categoryRepository;

    @Override
    public void insertCategories() {
        Category cate = new Category();
        cate.setCategoryName("Điện thoại - Máy tính bảng");
        cate.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate.setCreateAt(new Date().toString());
        cate.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate1 = new Category();
        cate1.setCategoryName("Điện tử - Điện lạnh");
        cate1.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate1.setCreateAt(new Date().toString());
        cate1.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate2 = new Category();
        cate2.setCategoryName("Phụ kiện - Thiết bị số");
        cate2.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate2.setCreateAt(new Date().toString());
        cate2.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate3 = new Category();
        cate3.setCategoryName("Laptop - Thiết bị IT");
        cate3.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate3.setCreateAt(new Date().toString());
        cate3.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate4 = new Category();
        cate4.setCategoryName("Máy ảnh - Quay phim");
        cate4.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate4.setCreateAt(new Date().toString());
        cate4.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate5 = new Category();
        cate5.setCategoryName("Điện gia dụng");
        cate5.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate5.setCreateAt(new Date().toString());
        cate5.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate6 = new Category();
        cate6.setCategoryName("Nhà cửa đời sống");
        cate6.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate6.setCreateAt(new Date().toString());
        cate6.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate7 = new Category();
        cate7.setCategoryName("Hàng tiêu dùng - Thực phẩm");
        cate7.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate7.setCreateAt(new Date().toString());
        cate7.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate8 = new Category();
        cate8.setCategoryName("Đồ chơi - Mẹ & Bé");
        cate8.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate8.setCreateAt(new Date().toString());
        cate8.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate9 = new Category();
        cate9.setCategoryName("Làm đẹp - Sức khỏe");
        cate9.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate9.setCreateAt(new Date().toString());
        cate9.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate10 = new Category();
        cate10.setCategoryName("Thời trang - Phụ kiện");
        cate10.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate10.setCreateAt(new Date().toString());
        cate10.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate11 = new Category();
        cate11.setCategoryName("Thể thao - Dã ngoại");
        cate11.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate11.setCreateAt(new Date().toString());
        cate11.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate12 = new Category();
        cate12.setCategoryName("Xe máy, oto, xe đạp");
        cate12.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate12.setCreateAt(new Date().toString());
        cate12.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate13 = new Category();
        cate13.setCategoryName("Hàng quốc tế\", \"MÔ tả điênh thoại máy tính bảng");
        cate13.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate13.setCreateAt(new Date().toString());
        cate13.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate14 = new Category();
        cate14.setCategoryName("Sách, VPP & Qùa tặng");
        cate14.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate14.setCreateAt(new Date().toString());
        cate14.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category cate15 = new Category();
        cate15.setCategoryName("Voucher, Dịch vụ, Thẻ cào");
        cate15.setDescription("MÔ tả điênh thoại máy tính bảng");
        cate15.setCreateAt(new Date().toString());
        cate15.setNote("GHI CHÚ MÁY TINH BẢNG");

        Category[] cates = {cate,cate1,cate2,cate3,cate4,cate5,cate6,cate7,cate8,cate9,cate10,cate11,cate12,cate13,cate14,cate15};
        for (Category category : cates) {
            categoryRepository.save(category);
        }
    }
}
