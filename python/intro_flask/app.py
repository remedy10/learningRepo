
from flask import Flask, redirect, render_template, request
from adapter.base import Session
from model.task import Task

app=Flask(__name__)
session= Session()
@app.route('/',methods=['POST','GET'])
def index():
    """
    docstring
    """
    if request.method=="GET":
        tasks=session.query(Task).all()
        return render_template('index.html',tasks=tasks)
    else:
        content=request.form['content']
        try:
            session.add(Task(content))
            session.commit()
            session.close()
            return redirect("/")
        except Exception as e :
            return f"an error occured inserting database.{e}"
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task_to_update=session.query(Task).filter(Task.id==id).first()
    if request.method=='POST':
        task_to_update.task_name=request.form['update_content']
        try:
            session.commit()
            return redirect('/')
        except Exception as e:
            return f'an error occured update val. {e}'
    return render_template('update.html',task=task_to_update)

@app.route('/delete/<int:id>')
def delete(id):
    """
    docstring
    """
    task_to_delete=session.query(Task).filter(Task.id==id).first()
    session.delete(task_to_delete)
    session.commit()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)

