from flask import Flask, request, render_template_string, make_response

app = Flask(__name__)


def staticTempalte(user_input=None):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8">
        <title>SSTI Demo</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>SSTI Playground</h1>
        <form method="POST" action="/">
            <label for="user_input">Enter template input:</label><br>
            <input type="text" id="user_input" name="user_input" size="50"/><br><br>
            <button type="submit">Submit</button>
        </form>
        
        {
            "<div class='output'><h1>Output:</h1>" + user_input + "</div>" if user_input is not None else ""
        }
        
    </body>
    </html>
    """


@app.route("/", methods=["GET", "POST"])
def home():
    try:
        user_input = request.form.get("user_input", None)
        return render_template_string(staticTempalte(user_input))
    except Exception as e:
        # return 500
        return make_response("Internal Server Error", 500)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
