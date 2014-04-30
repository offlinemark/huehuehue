#!/usr/bin/env python

from flask import Flask, render_template, request
import pyhue

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ip = request.form['ip']
        user = request.form['user']

        bridge = pyhue.Bridge(ip, user)

        if 'off' in request.form.keys():
            for light in bridge.lights:
                light.on = False
        if 'on' in request.form.keys():
            for light in bridge.lights:
                light.on = True

        return render_template('index.html', ip=ip, user=user)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
