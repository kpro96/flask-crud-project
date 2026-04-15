import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,template_folder=os.path.join(base_dir,'templates'))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Fixed: Capital 'I'
    name = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all() 

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
       
        user_input = request.form.get('content')
        if user_input:
            new_item = Item(name=user_input)
            db.session.add(new_item)
            db.session.commit()
        return redirect('/')
    
    
    
    all_data = Item.query.all()
    return render_template('datab1.html', items=all_data)


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Item.query.get_or_404(id)
    db.session.delete(item_to_delete)
    db.session.commit()                                     
    return redirect("/")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item =Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your item."
        
    
    return render_template('update.html', item=item)
if __name__ == "__main__":
    with app.app_context():
        if not Item.query.filter_by(name="mobile phone").first():
            new_item=Item(name="mobile phone")
            db.session.add(new_item)
            db.session.commit()
            print("successful")
            all_items=Item.query.all()
            for item in all_items:
                print(f"ID:  {item.id}  | Name:{item.name}")
app.run(debug=True,port=5001)
