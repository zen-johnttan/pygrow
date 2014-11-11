from . import build
from . import deploy
from . import extract
from . import init
from . import machine_translate
from . import routes
from . import run


def add(group):
  group.add_command(build.build)
  group.add_command(deploy.deploy)
  group.add_command(extract.extract)
  group.add_command(init.init)
  group.add_command(machine_translate.machine_translate)
  group.add_command(routes.routes)
  group.add_command(run.run)
