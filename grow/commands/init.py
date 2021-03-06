from grow.pods import commands
from grow.pods import pods
from grow.pods import storage
import click
import os


@click.command()
@click.argument('theme')
@click.argument('pod_path', default='.')
@click.option('--force', default=False, is_flag=True,
              help='Whether to overwrite existing files.')
def init(theme, pod_path, force):
  """Initializes a pod with a theme."""
  root = os.path.abspath(os.path.join(os.getcwd(), pod_path))
  pod = pods.Pod(root, storage=storage.FileStorage)
  commands.init(pod, theme, force=force)
