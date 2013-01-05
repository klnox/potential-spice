from pyramid.config import Configurator
from pyramid.response import Response


def root(request):
    """
    """
    return {}


def main(global_config, **settings):
    """
    """
    config = Configurator()
    config.add_route('root', '/')
    config.add_view(root, route_name='root',
         renderer='pythonpackages:templates/root.mak')
    return config.make_wsgi_app()