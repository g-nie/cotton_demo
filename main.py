from django.template.response import TemplateResponse
from nanodjango import Django


app = Django(
    EXTRA_APPS=["django_cotton"],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["templates"],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            }
        }
    ],
    STATICFILES_DIRS=[],
)


@app.route('/')
def home(request):
    return TemplateResponse(request, 'home.html')
