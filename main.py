from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'do your homework',
        'description': u'you have to do french and sanskrit and hindi',
        'done': False
    },
    {
        'id': 2,
        'title': u'do your homework cause idk',
        'description': u'you have to do geography and history and civics',
        'done': False
    }
]


@app.route("/")
def printdata():
    return jsonify({
        "data": tasks
    })


@app.route("/addtask", methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "pls provide the task or this thing will not work"
        })
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "the task has been added succesfully!"
    })


if __name__ == "__main__":
    app.run(debug=True)
