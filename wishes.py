from flask import Flask, request

app = Flask(__name__)  # Create Flask app

@app.route("/", methods=["GET", "POST"])
def birthday_wish():
    if request.method == "POST":
        name = request.form["name"]  # Get name from form
        return f"<h2>🎉 Happy Birthday, {name}! 🎂🎁 Have a great day! 🎊</h2>"
    
    # HTML form to enter the name
    return '''
        <form method="post">
            <label>Enter your name:</label>
            <input type="text" name="name" required>
            <button type="submit">Wish</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
