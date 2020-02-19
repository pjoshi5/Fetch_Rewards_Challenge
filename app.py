from flask import Flask, request
from Fetch_Rewards_Challenge import text_similarity



app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        str1 = None
        str2 = None
        try:
            str1 = str(request.form["str1"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["str1"])
        try:
            str2 = str(request.form["str2"])
        except:
            errors += "<p>{!r} is not a string.</p>\n".format(request.form["str2"])
        if str1 is not None and str2 is not None:
            result = text_sim(str1, str2)
            return '''
                <html>
                    <body>
                        <p>The similarity score for these two strings is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
    return '''
        <html>
            <body>
                <p>Enter your strings:</p>
                <form method="post" action=".">
                    <p><input name="str1" /></p>
                    <p><input name="str2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)

app.run()
