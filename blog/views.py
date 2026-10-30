from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import LoginForm, PostForm, SignUpForm
from .models import Category, Post


def post_list(request):
    posts = Post.objects.select_related("author", "category")
    page = Paginator(posts, 10).get_page(request.GET.get("page"))
    return render(
        request,
        "blog/post_list.html",
        {
            "page": page,
            "post_count": page.paginator.count,
            "category_count": Category.objects.count(),
        },
    )


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related("author", "category"), pk=pk)
    reading_minutes = max(1, (len(post.body.strip()) + 399) // 400)
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "reading_minutes": reading_minutes},
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "注册成功，可以开始写文章了。")
        return redirect("post_create")
    return render(request, "blog/signup.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        messages.success(request, "登录成功。")
        next_url = request.POST.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            return redirect(next_url)
        return redirect("post_list")
    return render(
        request,
        "blog/login.html",
        {"form": form, "next": request.GET.get("next", "")},
    )


def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "已退出登录。")
    return redirect("post_list")


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        category, _ = Category.objects.get_or_create(
            name=form.cleaned_data["category"].strip()
        )
        post = Post.objects.create(
            title=form.cleaned_data["title"],
            body=form.cleaned_data["body"],
            category=category,
            author=request.user,
        )
        messages.success(request, "文章已发布。")
        return redirect("post_detail", pk=post.pk)
    return render(
        request,
        "blog/post_form.html",
        {
            "form": form,
            "categories": Category.objects.values_list("name", flat=True),
        },
    )
