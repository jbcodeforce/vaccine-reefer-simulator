from flask import Blueprint,render_template 

ui_blueprint = Blueprint("ui-spa", __name__,
    template_folder='dist',
    static_folder='dist',
    static_url_path='/'
)

@ui_blueprint.route("/")
def index():
    return render_template("index.html")

