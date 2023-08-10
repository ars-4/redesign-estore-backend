from rest_framework.authtoken.models import Token


def get_or_create_token(user):
    tokens = Token.objects.filter(user=user)
    token = ''
    if(len(tokens) <= 0):
        token = Token.objects.create(user=user)
    else:
        token = tokens[0].key

    return token
