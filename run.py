#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:44:32 2022

@author: anirvachniya
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    draft_details = {'Type': ['CA', 'CB', 'CD', 'CE', 'CF'],
                     'Features': ['deli', 'dti', 'fic', 'insta', 'rate'],
                     'Values': ['1.1', '0.5', '6.4', '0.7', '0.5']
    }
    return render_template('template.html', my_string="Wheeeee!", draft_details=draft_details)


if __name__ == '__main__':
    app.run(debug=True)

