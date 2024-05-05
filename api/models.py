import sqlalchemy as sa
from typing import List
import sqlalchemy.orm as so
from api import db
import datetime
# from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    user_id: so.Mapped[int] = so.mapped_column(sa.Integer, unique=True, primary_key=True, autoincrement=True)
    login: so.Mapped[str] = so.mapped_column(sa.String(20), unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    analysis_results: so.Mapped[List["AnalysisResult"]] = so.relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.login)


class AnalysisResult(db.Model):
    __tablename__ = "analysis_result"

    analysis_id: so.Mapped[int] = so.mapped_column(sa.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('user.user_id'))
    user: so.Mapped["User"] = so.relationship(back_populates="analysis_results")

    # sa.BLOB
    created_dttm: so.Mapped[datetime.datetime] = so.mapped_column(sa.TIMESTAMP)
    segmentation_image: so.Mapped[str] = so.mapped_column(sa.String(40))
    detection_image: so.Mapped[str] = so.mapped_column(sa.String(40), nullable=True)
    original_image: so.Mapped[str] = so.mapped_column(sa.String(40))

    def __repr__(self):
        return '<Result_id {0} User> {1}'.format(self.analysis_id, self.user_login)
