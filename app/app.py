import os

from flask import Flask, render_template, request, jsonify

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY="dev"
  )

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  @app.route("/")
  def root():
    return jsonify(msg='success')

  @app.route("/ui")
  def home():
    return render_template('index.html')

  @app.route("/ui/about")
  def about():
    return render_template('about.html')

  import tesseract
  app.register_blueprint(tesseract.bp)

  import spacynlp
  app.register_blueprint(spacynlp.bp)

  import filemgmnt
  app.register_blueprint(filemgmnt.bp)

  return app
