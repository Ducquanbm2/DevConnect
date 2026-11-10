from sqlalchemy import CheckConstraint, ForeignKey, SmallInteger, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class Vote(Base, TimestampMixin):
    """
    Article Vote model (BR-05, BR-09):
    - Each user can cast at most 1 vote (+1 or -1) per article.
    """

    __tablename__ = "votes"
    __table_args__ = (
        UniqueConstraint("user_id", "article_id", name="uq_votes_user_article"),
        CheckConstraint("value IN (1, -1)", name="valid_vote_value"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    article_id: Mapped[int] = mapped_column(
        ForeignKey("articles.id", ondelete="CASCADE"), index=True, nullable=False
    )
    value: Mapped[int] = mapped_column(SmallInteger, nullable=False)
