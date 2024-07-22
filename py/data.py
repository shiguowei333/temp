from flask import Flask, jsonify,request
from flask_cors import CORS
import random


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
    
book_list = [{
    'id': '84732',
    'bookname': '西游记',
    'author': '吴承恩',
    'publisher': '人民文学出版社'
},{
    'id': '84731',
    'bookname': '三国演义',
    'author': '罗贯中',
    'publisher': '人民文学出版社'
},{
    'id': '84730',
    'bookname': '水浒传',
    'author': '施耐庵',
    'publisher': '人民文学出版社'
}]

@app.route('/api/getBooks', methods=['GET'])
def get_books():
    return jsonify(book_list)

@app.route('/api/getBook', methods=['GET'])
def get_book():
    id = request.args.get('id')
    for item in book_list:
        if(item['id'] == id):
            return jsonify(item)

i = 84730
@app.route('/api/addBook', methods=['POST'])
def add_book():
    i = str(random.randint(0,99999)).zfill(5)
    data = request.get_json()
    bookname = data['bookname']
    author = data['author']
    publisher = data['publisher']
    book_list.append({
        'id': i,
        'bookname': bookname,
        'author': author,
        'publisher': publisher
    })
    return jsonify({'status':200})

@app.route('/api/deleteBook', methods=['GET'])
def delete_book():
    id = request.args.get('id')
    
    for i in range(len(book_list)):
        if(book_list[i]['id'] == id):
            del book_list[i]
            break            
    return jsonify({'status': 200,'msg': '新增成功'})


@app.route('/api/updateBook', methods=['POST'])
def update_book():

    data = request.get_json()
    id = data['id']
    bookname = data['bookname']
    author = data['author']
    publisher = data['publisher']
    for i in range(len(book_list)):
        if(book_list[i]['id'] == id):
            book_list[i]['bookname'] = bookname
            book_list[i]['author'] = author
            book_list[i]['publisher'] = publisher
            break
    print(book_list)
    return jsonify({'status':200})

@app.route('/api/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save("./static/" + file.filename)
    return jsonify({'status':200,'filePath':'/static/'+file.filename})

if __name__ == '__main__':
    app.run(debug=True)