# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..models import User
from flask import flash


class LoginForm(FlaskForm):
    number = StringField('学号', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    number = StringField('学号或教工号', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    role = RadioField('角色', choices=((1, '学生'), (2, '教师'), (3, '管理员')), coerce=int, validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            flash('学号或教工号已存在，请登录或修改密码。')
            raise ValidationError()

    def validate_number(self, field):
        if User.query.filter_by(number=field.data).first():
            flash('学号或教工号已存在，请登录或修改密码。')
            raise ValidationError()

    def validate_role(self, field):
        # 因为 RadioField 中 coerce=int 的修饰，使得当前的 field.data 的值为 int 类型
        if field.data == 1 and self.number.data.__len__() != 8:
            flash('请输入正确的8位学号')
            raise ValidationError()
        if field.data == 2 and self.number.data.__len__() != 10:
            flash('请输入正确的教工号')
            raise ValidationError()


