# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request
import google.auth
from google.cloud import translate

import array as array
e = array.array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
s = array.array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
ig = array.array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', '-', '-', 'h', 'i', 'j', 'k', '-', 'l', 'm', 'n', 'ŋ', '-', 'o', 'ɔ', 'ɵ', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z', '-', '-', '-'])
y = array.array('u', ['a', 'b', 'd', 'e', 'ẹ', 'f', 'g', '-', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ọ', 'p', 'r', 's', 'ṣ', 't', 'u', 'w', 'y'])
ij = array.array('u', ['a', 'B', 'D', 'e', 'é', 'F', 'G', 'H', 'I', 'í', 'K', 'L', 'M', 'N', 'o', 'ò', 'P', 'R', 'S', 'T', 'u', 'ú', 'V', 'W', 'Y', 'Z'])

app = Flask(__name__)
#_, PROJECT_ID = google.auth.default()
#TRANSLATE = translate.TranslationServiceClient()
#PARENT = 'projects/{}'.format(PROJECT_ID)
#SOURCE, TARGET = ('en', 'English'), ('es', 'Spanish')


@app.route('/', methods=['GET', 'POST'])
def translate():
    """
    main handler - show form and possibly previous translation
    """

    # Flask Request object passed in for Cloud Functions
    # (use gcf_request for GCF but flask.request otherwise)
    #local_request = gcf_request if gcf_request else request

    # form submission and if there is data to process (POST)
    if request.method == 'POST':
        language = request.form.get("lang")
        number = request.form.get("num")
        

        if language == "English":
            if number <= 26 and number >= 1:
                return e[number - 1]
            else:
                return "Number entered is out of range."

        elif language == "Spanish":
            if number <= 27 and number >= 1:
                return s[number - 1]
            else:
                return "Number entered is out of range."
        elif language == "Igbo":
            if number == 8:
                return "gb"
            elif number == 9:
                return "gh"
            elif number == 14:
                return "kp"
            elif number == 19:
                return "ny"
            elif number == 31:
                return "gw"
            elif number == 32:
                return "kw"
            elif number == 33:
                return "nw"
            elif number <= 33 and b >= 1:
                return ig[number - 1]
            else:
                return "Number entered is out of range."
        elif language == "Yoruba":
            if number == 8:
                return "gb"
            elif number <= 25 and number >= 1:
                return y[number - 1]
            else:
                return "Number entered is out of range."
        elif language == "Ijaw":
            if number <= 26 and number >= 1:
                return ij[number - 1]
            else:
                return "Number entered is out of range."
        else:
            return "Language entered is not supported."
            

    # create render template
    return render_template('index.html')


if __name__ == '__main__':
    import os
    app.run(debug=True, threaded=True, host='0.0.0.0',
            port=int(os.environ.get('PORT', 8080)))
