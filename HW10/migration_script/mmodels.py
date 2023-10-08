import json
from sys import exit
from datetime import datetime
from mongoengine import EmbeddedDocument, Document, connect
from mongoengine.fields import DateField, EmbeddedDocumentField, ListField, StringField, ReferenceField

# -----------------------------------------------------------------


class Author(Document):
    fullname = StringField()
    born_date = DateField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()


# -----------------------------------------------------------------
