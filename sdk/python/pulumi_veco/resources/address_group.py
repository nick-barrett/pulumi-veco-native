# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AddressGroupArgs', 'AddressGroup']

@pulumi.input_type
class AddressGroupArgs:
    def __init__(__self__, *,
                 domains: pulumi.Input[Sequence[pulumi.Input[str]]],
                 prefixes: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The set of arguments for constructing a AddressGroup resource.
        """
        AddressGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domains=domains,
            prefixes=prefixes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domains: pulumi.Input[Sequence[pulumi.Input[str]]],
             prefixes: pulumi.Input[Sequence[pulumi.Input[str]]],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("domains", domains)
        _setter("prefixes", prefixes)

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter
    def prefixes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "prefixes")

    @prefixes.setter
    def prefixes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "prefixes", value)


class AddressGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a AddressGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddressGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AddressGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AddressGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddressGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AddressGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AddressGroupArgs.__new__(AddressGroupArgs)

            if domains is None and not opts.urn:
                raise TypeError("Missing required property 'domains'")
            __props__.__dict__["domains"] = domains
            if prefixes is None and not opts.urn:
                raise TypeError("Missing required property 'prefixes'")
            __props__.__dict__["prefixes"] = prefixes
            __props__.__dict__["address_group_id"] = None
        super(AddressGroup, __self__).__init__(
            'veco:resources:AddressGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AddressGroup':
        """
        Get an existing AddressGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AddressGroupArgs.__new__(AddressGroupArgs)

        __props__.__dict__["address_group_id"] = None
        __props__.__dict__["domains"] = None
        __props__.__dict__["prefixes"] = None
        return AddressGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressGroupId")
    def address_group_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "address_group_id")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def prefixes(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "prefixes")
