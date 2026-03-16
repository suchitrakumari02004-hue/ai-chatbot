from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":

        user_message = request.form["message"]

        chat_history.append({"role": "user", "content": user_message})

        response = ollama.chat(
            model="phi3",
            messages=chat_history
        )

        ai_reply = response["message"]["content"]

        chat_history.append({"role": "assistant", "content": ai_reply})

    return render_template("index.html", chat_history=chat_history)


if __name__ == "__main__":
    app.run(debug=True)
