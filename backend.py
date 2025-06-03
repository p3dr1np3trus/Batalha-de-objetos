from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


# Página inicial
def home_view(request):
    return Response('<h1> Batalha de Objetos </h1><p>Seja bem-vindo, guerreiro!<br>☆*: .｡. o(≧▽≦)o .｡.:*☆</p>')


# Página de batalha
def batalha_view(request):
    return Response('<h1> Campo de Batalha </h1><p>Em breve... Objetos sairão na pancada!</p>')


# Página de sobre
def sobre_view(request):
    return Response('<h1>ℹ Sobre</h1><p>Este é um jogo onde objetos se enfrentam em turnos!</p>')


if __name__ == '__main__':
    with Configurator() as config:
        # Rotas
        config.add_route('home', '/')
        config.add_route('batalha', '/batalha')
        config.add_route('sobre', '/sobre')

        # Conectar rotas às funções
        config.add_view(home_view, route_name='home')
        config.add_view(batalha_view, route_name='batalha')
        config.add_view(sobre_view, route_name='sobre')

        # Criar app
        app = config.make_wsgi_app()

    # Rodar servidor local
    server = make_server('0.0.0.0', 6543, app)
    print("🔥 Servidor rodando em http://localhost:6543")
    server.serve_forever()
