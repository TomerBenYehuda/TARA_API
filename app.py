from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knesset.db'
db = SQLAlchemy(app)


class KnessetModel(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100))
    gov_role = db.Column(db.String(255))
    kenesst_role = db.Column(db.String(255))
    party_role = db.Column(db.String(255))
    personal_phone = db.Column(db.Integer)
    office_phone = db.Column(db.Integer)
    email = db.Column(db.String(255))
    speaker_name = db.Column(db.String(100))
    speaker_phone = db.Column(db.Integer)
    head_office_name = db.Column(db.String(100))
    head_office_phone = db.Column(db.Integer)
    political_consultant_name = db.Column(db.String(100))
    political_consultant_phone = db.Column(db.Integer)
    # update_date = db.Column(db.Date())
    # facebook = db.Column(db.String(255))
    # instagram = db.Column(db.String(255))
    # twitter = db.Column(db.String(255))
    picture = db.Column(db.String(255))


db.create_all()

resource_fields = {
    'member_id': fields.Integer,
    'member_name': fields.String,
    'party': fields.String,
    'gov_role': fields.String,
    'knesset_role': fields.String,
    'party_role': fields.String,
    'personal_phone': fields.Integer,
    'office_phone': fields.Integer,
    'email': fields.String,
    'speaker_name': fields.String,
    'speaker_phone': fields.Integer,
    'head_office_name': fields.String,
    'head_office_phone': fields.Integer,
    'political_consultant_name': fields.String,
    'political_consultant_phone': fields.Integer,
    # 'update_date': fields.DateTime,
    # 'facebook': fields.String,
    # 'instagram': fields.String,
    # 'twitter': fields.String,
    'picture': fields.Url
}

knesset_member_put_args = reqparse.RequestParser()
knesset_member_put_args.add_argument("member_id", type=int, help="Put Knesset Member ID")
knesset_member_put_args.add_argument("member_name", type=str, help="Put Knesset Member Full Name")
knesset_member_put_args.add_argument("party", type=str, help="Put Knesset Party")
knesset_member_put_args.add_argument("gov_role", type=str, help="Put Knesset Gov Role")
knesset_member_put_args.add_argument("knesset_role", type=str, help="Put Knesset Knesset Role")
knesset_member_put_args.add_argument("party_role", type=str, help="Put Party Role")
knesset_member_put_args.add_argument("personal_phone", type=int, help="Put Personal Phone")
knesset_member_put_args.add_argument("office_phone", type=int, help="Put Office Phone")
knesset_member_put_args.add_argument("email", type=str, help="Put Email")
knesset_member_put_args.add_argument("speaker_name", type=str, help="Put Speaker Name")
knesset_member_put_args.add_argument("speaker_phone", type=int, help="Put Speaker Phone")
knesset_member_put_args.add_argument("head_office_name", type=str, help="Put Head Office Name")
knesset_member_put_args.add_argument("head_office_phone", type=int, help="Put Head Office Phone")
knesset_member_put_args.add_argument("political_consultant_name", type=str, help="Put Political Consultant Name")
knesset_member_put_args.add_argument("political_consultant_phone", type=int, help="Put Political Consultant Phone")
knesset_member_put_args.add_argument("picture", type=str, help="Put Picture URL")


class Server(Resource):
    @marshal_with(resource_fields)
    def get_by_id(self, member_id):
        result = KnessetModel.query.filter_by(member_id).first()
        return result

    @marshal_with(resource_fields)
    def get_by_full_name(self, full_name):
        result = KnessetModel.query.filter_by(full_name).first()
        return result

    @marshal_with(resource_fields)
    def post(self):
        args = knesset_member_put_args.parse_args()
        member = KnessetModel(member_id=args['member_id'],
                              member_name=args['member_name'],
                              party=args['party'],
                              gov_role=args['gov_role'],
                              knesset_role=args['knesset_role'],
                              party_role=args['party_role'],
                              personal_phone=args['personal_phone'],
                              office_phone=args['office_phone'],
                              email=args['email'],
                              speaker_name=args['speaker_name'],
                              speaker_phone=args['speaker_phone'],
                              head_office_name=args['head_office_name'],
                              head_office_phone=args['head_office_phone'],
                              political_consultant_name=args['political_consultant_name'],
                              political_consultant_phone=args['political_consultant_phone'],
                              picture=args['picture'])
        if member:
            abort(409, message='Member ID taken...')
        db.session.add(member)
        db.session.commit()
        return member, 201


api.add_resource(Server, "/Member/<int:member_id>")

if __name__ == "__main__":
    app.run(debug=True)
