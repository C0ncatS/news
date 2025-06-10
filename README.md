# 📰 News App

A simple Django-based newspaper web application that allows users to read, write, comment on, and manage news articles.

## ✨ Features

* 🔐 **User Authentication**

  * ✅ Sign up and log in to access the application.
  * 🔓 Log out and 🔁 change password functionalities.

* 📝 **Article Management**

  * 👀 View all news articles.
  * ➕ Add new articles.
  * ✏️ Edit or 🗑️ delete articles (only by the article owner).

* 💬 **Comment System**

  * 💭 Users can comment on articles.
  * 🔒 Only the article owner can edit or delete their own articles; all users can comment.

* 🛠️ **Admin Dashboard**

  * 📊 Full Django admin interface for managing users, articles, and comments.

## 🔄 Application Flow

1. 🔐 **Authentication Required**:

   * Upon visiting the site, users must **sign up** or **log in**.

2. 👁️ **View Articles**:

   * After authentication, users can browse all existing articles.

3. 🆕 **Create Article**:

   * Users can submit a new article.

4. 🛠️ **Edit/Delete Article**:

   * If the user is the **author** of an article, they can edit or delete it.

5. 💬 **Commenting**:

   * Any logged-in user can comment on articles, regardless of authorship.

6. ⚙️ **Account Management**:

   * Users can **log out** or **change their password** via built-in features.

7. 🧑‍💼 **Admin Interface**:

   * Accessible via `/admin` for superusers to manage all data models.

## 🛠️ Installation & Setup

```bash
# Clone the repository
https://github.com/C0ncatS/news.git
cd news

# Create virtual environment and activate it
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## 🧰 Tech Stack

* 🐍 Python
* 🌐 Django
* 🗃️ SQLite (default DB, can be changed)
* 🎨 HTML/CSS (via Django templates)

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

🙌 Feel free to contribute, submit issues, or suggest improvements!
