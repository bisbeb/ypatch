#!/bin/env python

import sys
import yaml
from optparse import OptionParser

class YamlAction:
  def __init__(self, action):
    ACTION_FX_LOOKUP = {"create":self.__create,"update":self.__update,"delete":self.__delete}
    self.action = ACTION_FX_LOOKUP[action]

  def __create(self, expr):
    pass

  def __update(self, expr):
    pass

  def __delete(self, expr):
    pass

class YamlPatcher:
 
  def __init__(self, opts):
    if opts["create"]:
      self.yaml_action = YamlAction("create")
      self.expr = opts["create"]
    elif opts["update"]:
      self.yaml_action = YamlAction("update")
      self.expr = opts["update"]
    elif opts["delete"]:
      self.yaml_action = YamlAction("delete")
      self.expr = opts["delete"]

    print self.expr

    if opts["file"] == "-":
      tmp_yaml = ""
      for line in sys.stdin:
        tmp_yaml += line
      self.yaml = yaml.load(tmp_yaml, Loader=yaml.FullLoader)
    else:
      stream = file(opts["file"], 'r')
      self.yaml = yaml.load(stream, Loader=yaml.FullLoader)

  def tokenize_expr(self):
    pass
    
if __name__ == "__main__":
  usage = """
Tool to patch yaml files on the fly.
  
`expression`:
a valid path within the yaml file structure
  """
  cmd_parser = OptionParser(usage=usage)
  cmd_parser.add_option("-c", "--create", dest="create", metavar="expression", help="create element")
  cmd_parser.add_option("-u", "--update", dest="update", metavar="expression", help="update element")
  cmd_parser.add_option("-d", "--delete", dest="delete", metavar="expression", help="delete element")
  cmd_parser.add_option("-p", "--pretty", dest="pretty", default=True, action="store_false", help="pretty output")
  cmd_parser.add_option("-f", "--file",   dest="file",   metavar="filename",   help="filename to read from, use - to read from stdin")

  (opts, args) = cmd_parser.parse_args()
  cmd_opts = vars(opts)
  yaml_patcher = YamlPatcher(cmd_opts)

