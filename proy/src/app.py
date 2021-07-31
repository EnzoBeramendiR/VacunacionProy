from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOusuario import DAOusuario


app = Flask(__name__)
app.secret_key ="Utec123"
db = DAOusuario()

@app.route('/')
def inicio():
    return render_template('index.html')

########################## ZONA DE DOCTOR ###################################
@app.route('/doctor/')
def doctor_index():
    data = db.read(None)
    return render_template("doctor/index.html",data = data)

@app.route('/doctor/add/')
def doctor_add():
    return render_template("doctor/add.html")

@app.route('/doctor/adddoctor',methods=['POST','GET']) 
def adddoctor():
    if request.method == 'POST' and request.form['save']:
        db.insert(request.form)
        return redirect(url_for("doctor_index"))

@app.route('/doctor/update/<int:id>/')
def doctor_update(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for("doctor_index"))
    else:
        session['update'] = id
    return render_template('doctor/update.html', data=data)

@app.route('/doctor/updatedoctor',methods=['POST'])
def updatedoctor():
    if request.method == 'POST' and request.form['update']:
        db.update_doc(session['update'], request.form)
        session.pop('update',None)
        return redirect(url_for("doctor_index"))

# @app.route('/doctor/update/<int:id>/')
# def doctor_update(id):
#     data = db.read(id)
#     if len(data) == 0:
#         return redirect(url_for("doctor_index"))
#     else:
#         session['update'] = id
#     return render_template("doctor/update.html", data=data)

# @app.route('/doctor/updatedoctor',methods=['POST'])
# def updatedoctor():
#     if request.method == 'POST' and request.form['update']:
#         db.update_doc(session['update'], request.form)
#         session.pop('update',None)
#         return redirect(url_for("doctor_index"))

@app.route('/doctor/deletedoctor',methods=['POST'])
def deletedoctor():
    if request.method == 'POST' and request.form['delete']:
        db.delete(session['delete'])
        session.pop('delete',None)
        return redirect(url_for("doctor_index"))

@app.route('/doctor/delete/<int:id>/')
def doctor_delete(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for("doctor_index"))
    else:
        session['delete'] = id
    return render_template("doctor/delete.html", data=data)

############################# PACIENTE ############################
@app.route('/paciente/')
def paciente_index():
    data = db.read(None)
    return render_template('paciente/index.html',data = data)

@app.route('/paciente/update/<int:id>/')
def paciente_update(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for("paciente_index"))
    else:
        session['update'] = id
    return render_template('paciente/update.html', data=data)

@app.route('/paciente/updatepaciente',methods=['POST'])
def updatepaciente():
    if request.method == 'POST' and request.form['update']:
        db.update_pac(session['update'], request.form)
        session.pop('update',None)
        return redirect(url_for("paciente_index"))

########################## ERROR #########################

@app.errorhandler(404)
def page_not_found():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000, host="0.0.0.0")