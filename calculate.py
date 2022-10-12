# importing Flask and other modules
from flask import Flask, request, Response

# Creates flask app
app = Flask(__name__)


# Renders a page here instead of calling on a HTML page
@app.route('/')
def render_form():
    form = '''
            <div class="col-2">
                <h1 style="color: green; font-family: courier">Home</h1>
                <h3 style = "font-family: courier" >Enter an integer to see if it is even or odd:</h3>
                <form action="calculate" method="post">
                    <label for="number">Number: </label>
                    <input type="text" id="number" name="number" placeholder="Enter a number:">
                    <button type="submit">Submit</button>
                </form>
            </div>
        '''
    return Response(form)


@app.route('/calculate', methods=["POST", "GET"])


#Calculates if number is even, odd or neither
def calculate():
    if request.method == "POST":
        #takes in number from the HTML page
        number = request.form.get("number")

        # checking if nothing is inputted
        if not number:
            return 'No number provided.<br><a href="/">Back to home</a>'
        # checking if given input is string type (not an int)
        elif number.isalpha():
            return f'{number} is not an integer!<br><a href="/">Back to home</a>'
        # checking if given number is even
        if int(number) % 2 == 0:
            return f'{number} is even.<br><a href="/">Back to home</a>'
        # checking if number is odd
        else:
            return f'{number} is odd.<br><a href="/">Back to home</a>'


# Starts the flask app
if __name__ == '__main__':
    app.run()