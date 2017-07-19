from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/Page_1')

@app.route('/Page_1', methods=['GET','POST'])
def Page_1():
  return render_template('Page_1.html')

@app.route('/Page_2', methods=['GET','POST'])
def Page_2():
	return render_template('Page_2.html')

@app.route('/Page_3', methods=['GET','POST'])
def Page_3():
	return render_template('Page_3.html')

@app.route('/Page_4', methods=['GET','POST'])
def Page_4():
	return render_template('Page_4.html')

@app.route('/Page_5', methods=['GET','POST'])
def Page_5():
	return render_template('Page_5.html')

@app.route('/Page_6', methods=['GET','POST'])
def Page_6():
	return render_template('Page_6.html')

if __name__ == '__main__':
  app.run(port=33507)
