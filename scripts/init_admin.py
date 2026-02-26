from core.database import SessionLocal, init_db
from models.user import User
from models.role import Role
from core.security import hash_password

def create_admin():
    session = SessionLocal()

    # Check if admin role exists
    admin_role = session.query(Role).filter_by(name="Admin").first()
    if not admin_role:
        admin_role = Role(name="Admin")
        session.add(admin_role)
        session.commit()

    # Check if admin user exists
    admin_user = session.query(User).filter_by(username="admin").first()
    if not admin_user:
        new_admin = User(
            username="admin",
            password_hash=hash_password("admin123"),
            role_id=admin_role.id
        )
        session.add(new_admin)
        session.commit()
        print("Admin user created.")
    else:
        print("Admin already exists.")

    session.close()

if __name__ == "__main__":
    init_db()
    create_admin()