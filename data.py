from flask import Flask, jsonify,request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/api/getProvince', methods=['GET'])
def get_data():
    data = {
        "message": "获取省份成功",
        "status": "success",
        "list": [
            '北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', 
            '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', 
            '海南省', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区', 
            '香港特别行政区', '澳门特别行政区', '台湾省'
        ]
    }
    return jsonify(data)

# 假设这是从数据库或文件加载的数据
provinces_data = {
    '河北': ['石家庄市', '唐山市', '秦皇岛市', '邯郸市', '邢台市', '保定市', '张家口市', '承德市', '沧州市', '廊坊市', '衡水市'],
    '山西': ['太原市', '大同市', '阳泉市', '长治市', '晋城市', '朔州市', '晋中市', '运城市', '忻州市', '临汾市', '吕梁市'],
    # ... 更多省份
}
@app.route('/api/getCities', methods=['GET'])
def get_cities():
    province_name = request.args.get('province')
    if province_name in provinces_data:
        cities = provinces_data[province_name]
        data = {
        "message": "获取城市成功",
        "status": "success",
        "list": cities
    }
        return jsonify(data)
    else:
        return jsonify({"error": "Province not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)