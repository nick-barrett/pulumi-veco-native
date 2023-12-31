# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_veco.config as __config
    config = __config
    import pulumi_veco.resources as __resources
    resources = __resources
else:
    config = _utilities.lazy_import('pulumi_veco.config')
    resources = _utilities.lazy_import('pulumi_veco.resources')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "veco",
  "mod": "resources",
  "fqn": "pulumi_veco.resources",
  "classes": {
   "veco:resources:AddressGroup": "AddressGroup",
   "veco:resources:ServiceGroup": "ServiceGroup"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "veco",
  "token": "pulumi:providers:veco",
  "fqn": "pulumi_veco",
  "class": "Provider"
 }
]
"""
)
