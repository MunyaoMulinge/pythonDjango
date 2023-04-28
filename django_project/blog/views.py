from django.shortcuts import render

posts = [
    {
        'author': 'Munyao',
        'title': 'Blogs',
        'content': 'firstContent',
        'datePosted': 12121990
    },
    {
        'author': 'Mary Jane',
        'title': 'Blogs2',
        'content': 'secondContent',
        'datePosted': 12121991
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
