"""
# https://stackify.com/dependency-injection/
The 4 roles in dependency injection
    If you want to use this technique, you need classes that fulfill four basic roles. These are:

- The service you want to use. (webserver.py and database.py)
- The client that uses the service. (core.py)
- An interface that’s used by the client and implemented by the service. (interface mostra quais métodos as dependencias devem ter, para que possam ser utilizadas no core)
- The injector which creates a service instance and injects it into the client. (class DependencyInjection: pass)
"""

from types import SimpleNamespace
from core import CreateCore
from unit_test import UnitTest


core = CreateCore()  # Executa o core com as config padrão

try:
    core.start()
    core.stop()
except Exception as e:
    print(e)

# %% EXEMPLO 2
"""
Usando um Database diferente
para isso, o database tem que ter os métodos que o core está utilizando
"""


class DependencyInjection:
    pass  # Jeito de criar um objeto onde posso ir moldando ele, adicionando atributos e métodos


di = DependencyInjection()
di.database = UnitTest().DifferentDatabaseConnection()

core = CreateCore(di)  # Posso mudar as config, desde que satifaçam os métodos utilizados em CreatCore()

try:
    core.start()
    core.stop()
except Exception as e:
    print(e)
# %% EXEMPLO 3
"""
Usando um Database e um WebServer diferente
"""


class DependencyInjection:
    pass  # Jeito de criar um objeto onde posso ir moldando ele, adicionando atributos e métodos


di = DependencyInjection()
di.database = UnitTest().DifferentDatabaseConnection()
di.webserver = UnitTest().DifferentWebserver()


core = CreateCore(di)  # Posso mudar as config, desde que satifaçam os métodos utilizados em CreatCore()

try:
    core.start()
    core.stop()
except Exception as e:
    print(e)

# %% EXEMPLO 4 - Usando o SimpleNamespace
"""
O SimpleNamespace é uma forma mais "bonita"(ver docs) que o Python fez para substituir o
class DependencyInjection: pass
"""
# Jeito 1 de declarar
di = SimpleNamespace()
di.database = UnitTest().DifferentDatabaseConnection()
di.webserver = UnitTest().DifferentWebserver()

# Jeito 2 de declarar
di = SimpleNamespace(
    database=UnitTest().DifferentDatabaseConnection(),
    # webserver=UnitTest().DifferentWebserver()
)


core = CreateCore(di)  # Posso mudar as config, desde que satifaçam os métodos utilizados em CreatCore()

try:
    core.start()
    core.stop()
except Exception as e:
    print(e)
