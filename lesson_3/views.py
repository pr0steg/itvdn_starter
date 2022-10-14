from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, \
    HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.utils.decorators import method_decorator

from django.views import View

from django.template import loader

from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view.csrf_exempt = True
        return view

    def get(self, request):
        if request.GET.get('type') == "file":
            return FileResponse(open(static('img/user.png'), "rb+"), )
        elif request.GET.get('type') == "json":
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == "redirect":
            return HttpResponseRedirect("http://127.0.0.1:8000/admin")
        else:
            return HttpResponseNotAllowed("You shall not pass!!!")

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")

    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@csrf_exempt
def my_view(request, **kwargs):
    return HttpResponse()


my_view.csrf_exempt = True


def main(request):
    request = request
    # test_template = loader.render_to_string("main.html")
    #
    # return HttpResponse(test_template)
    # test_template = loader.get_template(template_name='templates_example.html')
    # print(test_template)
    # return render(request, 'templates_example.html')
    # test_template_list = loader.select_template(template_name_list=
    #                                             ['test',
    #                                              'templates_example.html',
    #                                              'test2'])
    # print(test_template_list)
    #
    # return HttpResponse(test_template_list.render())
    test_template = loader.render_to_string('templates_example.html', context={'str': 'Test string',
                                                                               'int': 12})
    return HttpResponse(test_template)

def text(request):
    return HttpResponse("This is text from backend to user interface")


def file(request):
    # with open() as file:
    #     work with file
    print(static('img/001.jpg'))
    return FileResponse(open(static('img/001.jpg'), "rb+"))


def redirect(request):
    return HttpResponseRedirect("http://www.google.com")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
