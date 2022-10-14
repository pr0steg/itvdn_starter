from django.contrib.auth.models import User
from django.http import HttpResponse

from lesson_5.models import Flower, Bouquet, Client
from uuid import uuid4
from decimal import Decimal

from django.core.files import File


def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = "Роза является представителем семейства Разноцветных," \
                       " рода Шиповник. Растение в большинстве случаев " \
                       "представляет собой разветвленный кустарник, стебли" \
                       " которого покрыты шипами, роза имеет зеленые листья" \
                       " и большие ароматные цветы самого разного окраса"
    rose.could_use_in_bouquet = True
    rose.wiki_page = "ссылка на википедию"
    rose.name = "Роза красная"
    rose.save()
    return HttpResponse("Created!")


def create_client(request):
    # with open('requirements.txt', 'r') as _file:
    #     tmp_file = _file.read()

    client = Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin3.com',
        'name': 'MyName3',
        # 'invoice': tmp_file,
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.00052'),
        'client_ip': '192.0.2.3',
    })
    # print(client)
    # return HttpResponse('Created!')
    return HttpResponse(client)


def get_flower(request):
    # return HttpResponse('Flower')
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)
