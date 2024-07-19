#!/usr/bin/python3
import flask

def create_app():
    app = flask.Flask(__name__)

    # Define a simple function to reduce repetition
    def render(page):
        return flask.render_template(f'{page}.html')

    @app.route('/')
    def home():
        return render('index')

    @app.route('/about')
    def about():
        return render('about')

    @app.route('/contact')
    def contact():
        return render('contact')

    return app

app = create_app()

# Different approach to run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)