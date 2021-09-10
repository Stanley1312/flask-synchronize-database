from .model import db, User


# =============================================================================

def get_all_users():
    all_users = User.query.all()
    list_users = list(map(lambda x:x.to_dict(), all_users))

    return list_users