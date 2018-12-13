from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    name = StringField('岗位名称', validators=[DataRequired()])
    content = TextAreaField('岗位介绍', validators=[DataRequired()])
    submit = SubmitField('添加')
