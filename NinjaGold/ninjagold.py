from flask import Flask,render_template,request,redirect,session, flash
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_money', methods =['POST'])
def addCoins():
    session['name'] = request.form.keys()[0]
    if 'total' not in session:
        session['total'] = 0

    if session['name'] == 'farm':
        session['num'] = random.randint(10,21)
        flash("You get " + str(session['num']) + " coins from farming.")
        print("You get " + str(session['num']) + " coins from farming.")
        session['total'] += session['num']
        return redirect('/')
    elif session['name'] == 'cave':
        session['num'] = random.randint(5,10)
        flash("You get " + str(session['num']) + " coins from searching the cave.")
        print("You get " + str(session['num']) + " coins from searching the cave.")
        session['total'] += session['num']
        return redirect('/')
    elif session['name'] == 'house':
        session['num'] = random.randint(2,5)
        flash("You get " + str(session['num']) + " coins from searching the house.")
        print("You get " + str(session['num']) + " coins from searching the house.")
        session['total'] += session['num']
        return redirect('/')
    elif session['name'] == 'casino':
        session['num'] = random.randint(-50,50)
        if session['num'] < 0:
            flash("You lose " + str(session['num']) + " coins from gambling in the casino.")
            print("You lose " + str(session['num']) + " coins from gambling in the casino.")
            session['total'] += session['num']
            return redirect('/')
        elif session['num'] > 0:
            flash("You win " + str(session['num']) + " coins from gambling in the casino.")
            print("You win " + str(session['num']) + " coins from gambling in the casino.")
            session['total'] += session['num']
            return redirect('/')
        elif session['num'] == 0:
            flash("You broke even from gambling in the casino.")
            print("You broke even from gambling in the casino.")
            session['total'] += session['num']
            return redirect('/')
    else:
        return redirect('/')
@app.route('/reset')
def reset():
    session['total'] = 0
    return redirect('/')

app.run(debug=True)
