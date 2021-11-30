from flask import Flask

app = Flask(__name__)
app.secret_key = "this_will_need_to_be_changed_in_production"

# pylint: disable=wrong-import-position
# pylint: disable=unused-import
import routes
# pylint: enable=unused-import
# pylint: enable=wrong-import-position
