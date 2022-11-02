from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_

app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:*******@127.0.0.1:3306/flask_practice"
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
db = SQLAlchemy(app)


class Role(db.Model):
    """角色"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return "Role: %s" % self.name


class User(db.Model):
    """用户信息"""
    __tablename__ = "tbl_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User: %s" % self.name


if __name__ == '__main__':
    with app.app_context():
        print(db.metadata.sorted_tables)
        # 删除数据库中的所有表
        db.drop_all()
        # 创建表
        print(db.metadata.sorted_tables)
        db.create_all()
        role = Role(name="admin")
        db.session.add(role)
        db.session.commit()

        role2 = Role(name="stuff")
        db.session.add(role2)
        db.session.commit()

        us1 = User(name="wang", email="wang@163.com", password="123456", role_id=role.id)
        us2 = User(name="lin", email="lin@163.com", password="123456", role_id=role2.id)
        us3 = User(name="li", email="li@163.com", password="123455", role_id=role2.id)
        db.session.add_all([us1, us2, us3])
        db.session.commit()
        # 查询=========================================
        a = Role.query.all()
        b = Role.query.first()
        user_sum = User.query.count()
        #     过滤
        User.query.filter_by(name="wang")  # 得到一个查询对象 where
        User.query.filter_by(name="wang", id=1).all()  # 看对象的信息需要all where
        User.query.filter(User.name == "wang").all()
        User.query.filter(User.name != "wang").all()
        User.query.filter(and_(User.name == "wang", User.email.endwith("@163.com")))
        User.query.filter(or_(User.name == "wang", User.email.endwith("@163.com")))
        User.query.order_by(User.id)
        wang = User.query.filter_by(name="wang")
        print(wang.role)
        role1 = Role.query.get(1)
        print(role1.users)

        #     改===================================================
        User.query.filter_by(name="wang").update({"name": "zhang"})
        db.session.commit()
        #     删================================================
        user = User.query.get(1)
        db.session.delete(user)
        db.session.commit()

    # app.run(host="127.0.0.1", port=8080)
