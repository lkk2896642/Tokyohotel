from flask import Flask, render_template, url_for, request, redirect
import model

app = Flask(__name__)


@app.route('/')
def index():
    hotels = model.get_hotels()
    return render_template("index.html", hotels=hotels)


@app.route('/detail/<id>')
def detail(id):
    hotel = model.get_hotel_by_id(id)
    return render_template("detail.html", hotel=hotel)


@app.route('/add', methods=['GET'])
def get_add():
    districts = model.get_districts()
    return render_template(
        'input.html',
        message="ホテルの情報を入力してください。",
        districts=districts
    )


@app.route('/add', methods=['POST'])
def post_add():
    name = request.form['name']
    name_en = request.form["name_en"]
    img_src = request.form["img_src"]
    district_id = int(request.form["district_id"])
    address = request.form["address"]
    price = int(request.form["price"])
    station = request.form["station"]
    summary = request.form["summary"]
    introduction = request.form["introduction"]
    room_size = int(request.form["room_size"])
    max_ppl = int(request.form["max_ppl"])
    equipments = request.form["equipments"]

    model.add_hotel(
        name=name,
        name_en=name_en,
        img_src=img_src,
        district_id=district_id,
        address=address,
        price=price,
        station=station,
        summary=summary,
        introduction=introduction,
        room_size=room_size,
        max_ppl=max_ppl,
        equipments=equipments
    )

    return redirect(url_for("index"))


@app.route('/update/<id>', methods=['GET'])
def get_update(id):

    hotel = model.get_hotel_by_id(id)
    districts = model.get_districts()
    return render_template(
        'update_input.html',
        message="ホテルの情報を更新してください。",
        districts=districts,
        hotel=hotel
    )


@app.route('/update', methods=['POST'])
def post_update():
    id = int(request.form["id"])
    name = request.form["name"]
    name_en = request.form["name_en"]
    img_src = request.form["img_src"]
    district_id = int(request.form["district_id"])
    address = request.form["address"]
    price = int(request.form["price"])
    station = request.form["station"]
    summary = request.form["summary"]
    introduction = request.form["introduction"]
    room_size = int(request.form["room_size"])
    max_ppl = int(request.form["max_ppl"])
    equipments = request.form["equipments"]

    model.update_hotel(
        id=id,
        name=name,
        name_en=name_en,
        img_src=img_src,
        district_id=district_id,
        address=address,
        price=price,
        station=station,
        summary=summary,
        introduction=introduction,
        room_size=room_size,
        max_ppl=max_ppl,
        equipments=equipments
    )

    return redirect(url_for("index"))


@app.route('/delete/<id>', methods=['GET'])
def get_delete(id):

    hotel = model.get_hotel_by_id(id)
    districts = model.get_districts()
    return render_template(
        'delete_input.html',
        message="ホテルの情報を削除よろしいでしょうか？",
        districts=districts,
        hotel=hotel
    )


@app.route('/delete', methods=['POST'])
def post_delete():
    id = int(request.form['id'])
    model.delete_hotel(
        id=id,
    )


    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
