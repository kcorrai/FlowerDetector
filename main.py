from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flowerdata import flowerdataset, image_names
from flowerdetector import flowerdetector
from speechrecognition import tur_spe_recog
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70))
    textarea = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<User {self.id}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    search_layout = True
    if request.method == 'POST':
        user = request.form.get('flowers')
        flower_name, color, petal_count, bloom_Season, height_cm, info, latin_name, common_use, growing_conditions = flowerdataset(user)
        image = image_names[flower_name]
        search_layout = False

        return render_template('index.html',
                               flower_name=flower_name,
                               color=color,
                               petal_count=petal_count,
                               bloom_Season=bloom_Season,
                               height_cm=height_cm,
                               info=info,
                               search_layout=search_layout,
                               latin_name=latin_name,
                               common_use=common_use,
                               growing_conditions=growing_conditions,
                               image=image)

    else:
        return render_template('index.html',
                               search_layout=search_layout)
        
@app.route('/flower-detector', methods=['GET', 'POST'])
def flowerdetect():
    if request.method == 'POST':
        try:
            fimage = request.files['fimage']
            fimage.save(f'static/uploads/{fimage.filename}')
            class_name, confidence_score = flowerdetector(f'static/uploads/{fimage.filename}')
            new_confidence_score = round(confidence_score * 100, 2)
            print(fimage.filename)
            
            return render_template('flowerdetect.html',
                                class_name=class_name[:-1],
                                confidence_score=new_confidence_score,
                                filename=fimage.filename)
        except Exception as a:
            print(a)
            return render_template('flowerdetect.html')
    else:
        return render_template('flowerdetect.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        textarea = request.form['idea']
        
        contact = User(name=name, email=email, textarea=textarea)
        db.session.add(contact)
        db.session.commit()
        
        return redirect('/')
    
    else:
        return render_template('contact.html')
    
@app.route('/voice')
def voice():  
    voice = tur_spe_recog()
      
    return render_template('contact.html', voice=voice)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)