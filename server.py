from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return 'dojo'

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<name>')
def say_hi(name):
    print(name)
    return "Hi " + name

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/hello/<string:name>/<int:num>')
def say_hello(name,num):
    return f"Hello {name * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

