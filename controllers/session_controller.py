from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("session", __name__)

@sessions_blueprint.route("/session")
def sessions():
    session = session_repository.select_all()
    return render_template("session/index.html", session = session)

@sessions_blueprint.route("/session/<id>")
def show(id):
    session = session_repository.select(id)
    member = session_repository.member(session)
    return render_template("session/show.html", session=session, member=member)