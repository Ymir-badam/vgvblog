# VGV Konsultancy — Django Site

A plain Django project (no Django REST Framework) for the VGV Konsultancy
website, with a "Posts" (Insights) feature you manage from the built-in
Django admin.

## What's included

- **website** app
  - `Post` model — title, category, excerpt, content, cover image, author,
    published date, published/draft flag
  - Home page (`/`) — the full firm site, plus a "Latest Insights" section
    showing the 3 most recent published posts
  - Insights list (`/insights/`) — paginated, filterable by category
  - Insight detail (`/insights/<slug>/`) — single post page with related posts
  - Django admin at `/admin/` to create/edit/delete posts (upload a cover
    image, write content, mark published or draft)
- All firm content (About, Founder, Office photos, Services, Why VGV,
  Industries, Mission/Vision, Contact) carried over from the original design,
  now rendered from Django templates instead of a static HTML file.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- `http://127.0.0.1:8000/` — the site
- `http://127.0.0.1:8000/insights/` — all posts
- `http://127.0.0.1:8000/admin/` — add/edit posts

## Demo data already included

This project ships with a SQLite database (`db.sqlite3`) that already has:
- A superuser: **username `admin`, password `vgvadmin123`** — change this
  immediately if you deploy this anywhere public.
- 3 sample posts under `/insights/` so the Insights section isn't empty.

Delete `db.sqlite3` and re-run `python manage.py migrate` if you'd rather
start from a clean database.

## Adding a post

1. Go to `/admin/`, log in.
2. Under **Website → Posts**, click **Add Post**.
3. Fill in title, category, content, optionally a cover image.
4. Leave **slug** and **excerpt** blank — both are auto-generated on save.
5. Make sure **Is published** is checked, then Save.

The post immediately appears on the homepage (if it's one of the 3 most
recent) and on `/insights/`.

## Project layout

```
vgv_project/        # Django project settings/urls
website/
  models.py          # Post model
  admin.py            # Post admin registration
  views.py            # home, post_list, post_detail (function-based, no DRF)
  urls.py              # app routes
  templates/website/  # base.html, home.html, post_list.html, post_detail.html
  static/website/
    css/style.css      # all site styling
    img/                # founder photo + office photos
```

## Notes

- No Django REST Framework is used anywhere — everything is server-rendered
  HTML via Django's template engine.
- `DEBUG = True` and a checked-in `SECRET_KEY` are fine for local use only.
  Before deploying, set `DEBUG = False`, move `SECRET_KEY` to an environment
  variable, and set `ALLOWED_HOSTS` to your real domain.
