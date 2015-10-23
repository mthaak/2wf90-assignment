from distutils.core import setup
import py2exe
import _imports

setup(name="2WF90 Assignment",
      console=['main.py'],
      zipfile=None,
      description="test",
      options={'py2exe': {'bundle_files': 1, 'compressed': True}})
