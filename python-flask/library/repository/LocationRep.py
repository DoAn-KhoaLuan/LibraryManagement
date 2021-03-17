from library import db
from library.common.util import ConvertModelListToDictList
from library.miration.models import Province, District, Ward


def createProvince(province):
    provinceModel = Province((province["code"]), province["name"], province["region"]);
    db.session.add(provinceModel)
    db.session.commit()


def createDistrict(district):
    districtModel = District((district["code"]), district["name"], district["province_code"]);
    db.session.add(districtModel)
    db.session.commit()


def createWard(ward):
    wardModel = Ward((ward["code"]), ward["name"], ward["district_code"]);
    db.session.add(wardModel)
    db.session.commit()


def getProvinces():
    modelProvinces = Province.query.all();
    return ConvertModelListToDictList(modelProvinces)


def getDistricts():
    modelDistricts = District.query.all();
    return ConvertModelListToDictList(modelDistricts)

def getWards():
    modelWards = Ward.query.all();
    return ConvertModelListToDictList(modelWards)