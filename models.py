# coding=utf-8
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class HubUser(UserMixin, db.Model):
    """
    HubUser Table
    """

    __tablename__ = 'hubusers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<HubUser: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return HubUser.query.get(int(user_id))

class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    hubusers = db.relationship('HubUser', backref='role',
                               lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


# CCT tables

class CCTData(db.Model):
    '''
    Creat a CCTData table
    '''
    __tablename__= 'cctdatas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.Text)
    brand = db.Column(db.String(64))
    type = db.Column(db.Integer, db.ForeignKey('typeofmaterials.id'))
    ingredient = db.Column(db.JSON)
    cctimage = db.Column(db.String(512))
    criticalpoint = db.Column(db.JSON)
    metallography = db.Column(db.JSON)

    hardness = db.Column(db.String(512))
    delectflag = db.Column(db.Boolean)

    def __repr__(self):
        return '<CCTData: {}>'.format(self.name)

class Typeofmaterial(db.Model):
    """
    Material Type
    """
    __tablename__ = 'typeofmaterials'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    type = db.Column(db.Integer, db.ForeignKey('typeofhub.id'))
    cctdata = db.relationship('CCTData', backref='typeofmaterial',
                              lazy='dynamic')
    fld = db.relationship('FLD', backref='typeofmaterial',
                          lazy='dynamic')
    fat = db.relationship('Fat', backref='typeofmaterial',
                          lazy='dynamic')
    cor = db.relationship('Corrosion', backref='typeofmaterial',
                          lazy='dynamic')


    def __repr__(self):
        return '<Typeofmaterial: {}'.format(self.name)


class FLD(db.Model):
    """
    FLD Model
    """
    __tablename__ = 'fldtests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    source = db.Column(db.String(64))
    sernm = db.Column(db.Text)
    description = db.Column(db.Text)
    brand = db.Column(db.String(64))
    type = db.Column(db.Integer, db.ForeignKey('typeofmaterials.id'))
    stretch = db.Column(db.Text)                                          # image first
    fldimg = db.Column(db.Text)
    flddes = db.Column(db.Text)


    def __repr__(self):
        return '<FLD: {}'.format(self.name)

# class TypeOfFld(db.Model):
#     """
#     FLD type Model
#     """
#     __tablename__ = 'typeofflds'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     description = db.Column(db.Text)
#     fld = db.relationship('FLD', backref='typeoffld',
#                               lazy='dynamic')
#
#     def __repr__(self):
#         return '<TypeofFld: {}'.format(self.name)

class Fat(db.Model):
    """
    fatigue test Model
    """
    __tablename__ = 'fattests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    source = db.Column(db.String(64))
    description = db.Column(db.Text)
    brand = db.Column(db.String(64))
    type = db.Column(db.Integer, db.ForeignKey('typeofmaterials.id'))
    fatsnimg = db.Column(db.Text)
    fatsndes = db.Column(db.Text)

    def __repr__(self):
        return '<Fat: {}'.format(self.name)

# class TypeOffat(db.Model):
#     """
#     fatigue type Model
#     """
#     __tablename__ = 'typeoffats'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     description = db.Column(db.Text)
#     fat = db.relationship('Fat', backref='typeoffat',
#                               lazy='dynamic')
#
#     def __repr__(self):
#         return '<Typeoffat: {}'.format(self.name)


class Corrosion(db.Model):
    """
    corrosion test table,
    vrv 点蚀电压 粗糙度 腐蚀速率
    ecodes 电化学腐蚀试验方案
    eccor 电化学腐蚀对比图片
    coecurve 极化曲线图片
    hldes 高低温腐蚀试验方案
    dlcon试验条件
    """
    __tablename__ = 'cortests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    source = db.Column(db.String(64))
    brand = db.Column(db.String(64))
    type = db.Column(db.Integer, db.ForeignKey('typeofmaterials.id'))
    vrv = db.Column(db.String(64))
    ingredient = db.Column(db.String(1000))
    eccdes = db.Column(db.Text)
    eccor = db.Column(db.Text)
    ecocurve = db.Column(db.Text)
    hldes = db.Column(db.Text)
    hlvec = db.Column(db.Text)
    hltest = db.Column(db.Text)
    xrddes = db.Column(db.Text)
    xrd = db.Column(db.Text)

    def __repr__(self):
        return '<Corrosion: {}'.format(self.name)

class HubType(db.Model):
    """
    Type of Hub for cct cors fat etc.
    """

    __tablename__ = 'typeofhub'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(512))
    description = db.Column(db.Text)

    materialtype=db.relationship('Typeofmaterial', backref='typeofhub',
                              lazy='dynamic')
    def __repr__(self):
        return '<HubType: {}'.format(self.name)





class Config(db.Model):
    """
    This table is for Config App

    """
    __tablename__ = 'configs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    value = db.Column(db.Text)

    def __repr__(self):
        return '<Config: {}'.format(self.name)

class Commondata(db.Model):
    """
    Common Data
    """

    __tablename__ = 'commondatas'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(512))
    value = db.Column(db.Text)

class Timeline(db.Model):
    """
    This table is for recording timeline

    """

    __tablename__= 'timeline'
    id = db.Column(db.Integer,primary_key=True)
    content =  db.Column(db.Text)
    datetime = db.Column(db.DateTime)

    def __repr__(self):
        return '<Timeline: {0} {1}>'.format(self.datetime,self.content)