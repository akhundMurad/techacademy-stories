from modeltranslation.translator import translator, TranslationOptions
from blog.models import Post


class PostTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Post, PostTranslationOptions)
