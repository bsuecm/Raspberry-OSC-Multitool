from webapp import app
from flask import render_template, flash, redirect
from webapp.forms import ConfigOSCForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/global_configuration', methods=['GET', 'POST'])
def global_configuration():
    form = ConfigOSCForm()
    if form.validate_on_submit():
        flash('IP {} applied, port {} applied.'.format(
            form.osc_server_ip.data, form.osc_server_port.data))
        return redirect('/index')
    return  render_template('global_configuration.html', 
                            title='Global OSC Configuration', 
                            form=form)