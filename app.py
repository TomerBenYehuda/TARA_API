from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knesset.db'
db = SQLAlchemy(app)


class KnessetModel(db.Model):
    member_id = db.Column(db.Integer(), primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100))
    gov_role = db.Column(db.String(255))
    kenesst_role = db.Column(db.String(255))
    party_role = db.Column(db.String(255))
    personal_phone = db.Column(db.Integer())
    office_phone = db.Column(db.Integer())
    email = db.Column(db.String(255))
    speaker_name = db.Column(db.String(100))
    speaker_phone = db.Column(db.Integer())
    head_office_name = db.Column(db.String(100))
    head_office_phone = db.Column(db.Integer())
    political_consultant_name = db.Column(db.String(100))
    political_consultant_phone = db.Column(db.Integer())
    update_date = db.Column(db.Date())
    facebook = db.Column(db.String(255))
    instagram = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    picture = db.Column(db.String(255))

    def __repr__(self):
        return f"name is {self.member_name}, my ID is {self.member_id}"


resource_fields = {
    'id': fields.String
}


class Server(Resource):
    def get(self, member_id):
        result = KnessetModel.query.get(id=member_id)
        return result

    def post(self):
        pass


api.add_resource(Server)

if __name__ == "__main__":
    app.run(debug=True)
