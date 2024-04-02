from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class ConfigOSCForm(FlaskForm):
    osc_server_ip = StringField('IP address of the receiving OSC Device', validators=[DataRequired()])
    osc_server_port = IntegerField('Port number of the Receiving OSC Device', validators=[DataRequired()])
    submit = SubmitField('Apply')

class SwitchConfigForm(FlaskForm):
    switch1_pin = IntegerField("Switch 1 GPIO pin", validators=[DataRequired()], default=26)
    switch1_OSC_address = StringField('Switch 1 OSC Address', validators=[DataRequired()], default='/switch1')
    switch2_pin = IntegerField("Switch 1 GPIO pin", validators=[DataRequired()], default=19)
    switch2_OSC_address = StringField('Switch 1 OSC Address', validators=[DataRequired()], default='/switch2')
    switch3_pin = IntegerField("Switch 1 GPIO pin", validators=[DataRequired()], default=13)
    switch3_OSC_address = StringField('Switch 1 OSC Address', validators=[DataRequired()], default='/switch3')
    switch4_pin = IntegerField("Switch 1 GPIO pin", validators=[DataRequired()], default=6)
    switch4_OSC_address = StringField('Switch 1 OSC Address', validators=[DataRequired()], default='/switch4')
    debounce_time = FloatField('Switch debounce time', validators=[DataRequired()], default=0.05)
    submit = SubmitField('Run')