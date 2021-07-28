from flask import Flask, render_template
app = Flask(__name__)

posts= [
	{
		'author':'maxwell jones',
		'title': 'Blog post 1',
		'content':'First Post Content',
		'date_posted':'July 26th, 2021'
	},
	{
		'author':'Daniel pete',
		'title': 'Blog post 2',
		'content':'Second Post Content',
		'date_posted':'July 27th, 2021'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__=="__main__":
	app.run(debug=True)