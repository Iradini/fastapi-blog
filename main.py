from fastapi import FastAPI, HTTPException, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "autor": "Maria Iradini",
        "title": "FastAPI is awesomme",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2026",
    },
    {
            "id": 2,
            "autor": "Jane Doe",
            "title": "Python is great for web development",
            "content": "Python is a great language for web development, and FastAPI makes it even better.",
            "date_posted": "April 21, 2026",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "home": home})


@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
                return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")