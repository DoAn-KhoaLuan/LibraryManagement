package common.utils;

import net.minidev.json.JSONObject;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class Util {
    public static JSONObject getProvincesToDBFromEtopApi() {
        String uri = "https://shop.d.etop.vn/api/etop.Location/GetProvinces";
        RestTemplate restTemplate = new RestTemplate();
        JSONObject request = new JSONObject();

        JSONObject provinces = restTemplate.postForObject( uri, request, JSONObject.class);
        return provinces;

    }

    public static JSONObject getDistrictsToDBFromEtopApi() {
        String uri = "https://shop.d.etop.vn/api/etop.Location/GetDistricts";
        RestTemplate restTemplate = new RestTemplate();
        JSONObject request = new JSONObject();

        JSONObject districts = restTemplate.postForObject( uri, request, JSONObject.class);
        return districts;

    }

    public static JSONObject getWardsToDBFromEtopApi() {
        String uri = "https://shop.d.etop.vn/api/etop.Location/GetWards";
        RestTemplate restTemplate = new RestTemplate();
        JSONObject request = new JSONObject();

        JSONObject wards = restTemplate.postForObject( uri, request, JSONObject.class);
        return wards;

    }
}
