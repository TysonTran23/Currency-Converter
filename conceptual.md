### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
###### Python
* Backend Language
* For server-side scripting
* Simple, easier syntax than Javascript
###### JavaScript
* Client-side scripting
* Frontend Development
* Not the easiest syntax/code
* Run javascript on web browsers
  
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
1. Using the get() method, if the value is there it will grab it, if not it returns 'Not Found'
2. Setdefault(), if the key is not in the dictionary, it will create it

- What is a unit test?
* Used to test pieces of code, typically a single function or method
  
- What is an integration test?
* Testing of multiple units to make sure everything is working smoothly together
  
- What is the role of web application framework, like Flask?
* Role is to help aid in web development, support applications
* This can include web API's, functionality, efficiency in writing code
  
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
* URL route are used to identify a specific/single resource
* URL query params are used to filter and sort data/Multiple resources

- How do you collect data from a URL placeholder parameter using Flask?
Ex

@app.route('/user/<username>')
def show_user_profile(username):

return f"User: {username}"

- How do you collect data from the query string using Flask?
Ex

@app.route('/data')
def get_data():

request.args.get('data')

- How do you collect data from the body of the request using Flask?
Ex

@app.route('/data', methods=['POSTS'])
def process_data():
data = request.json

- What is a cookie and what kinds of things are they commonly used for?
* Cookies are used to store small pieces of data
* Example could be favourite_muffin = 'Chocolate Muffin'
* This starts from the server, telling the browser about this new cookie
* Browser than continues to remind the server about the cookie
* Cookies are commonly used to keep track of the specific user attributes
* Ex Login ID Number

- What is the session object in Flask?
* Session object in flask is used to store information in the session
* A cookie is than created of 'session' stored in the browser and is remembered
* Anything stored in the session will be turned into a cookie

- What does Flask's `jsonify()` do?
* Converts a Python object into a JSON response
* Takes one or more python objects as arugments and returns a Flask response object with a JSON representation of the provided data
