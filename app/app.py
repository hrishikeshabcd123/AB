from flask import Flask, render_template, request, send_file
import ipaddress
import zipfile
from pathlib import Path

app = Flask(__name__)

[...]

# generate configuration when data is received from generator form
@app.route('/result', methods=['POST', 'GET'])
def result():
    [...] some code, input checks, text manipulation

        # check folder content for .cfg files and add them to a zip archive
        with zipfile.ZipFile(temp_zipfile, mode='w') as z:
            for file in base_path.iterdir():
                if file.suffix == ".cfg":
                    try:
                        z.write(file, file, zipfile.ZIP_DEFLATED)
                    except:
                        continue
        # send the zip file to the user
        return send_file(temp_zipfile, as_attachment=True, mimetype='application/zip',attachment_filename="configurations.zip")
    # if HA is not used, send a cfg file directly
    elif result["cluster"] == "no":
        configfile = config_filepath + result["HOSTNAME"] + ".cfg"
        with open(configfile, "w+") as cfg:
            cfg.write(content)
        return send_file(configfile, as_attachment=True,attachment_filename='configurations.cfg')
