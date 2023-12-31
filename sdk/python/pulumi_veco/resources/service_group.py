# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ServiceGroupArgs', 'ServiceGroup']

@pulumi.input_type
class ServiceGroupArgs:
    def __init__(__self__, *,
                 icmp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]] = None,
                 icmp6: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupTcpArgs']]]] = None,
                 udp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupUdpArgs']]]] = None):
        """
        The set of arguments for constructing a ServiceGroup resource.
        """
        ServiceGroupArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            icmp=icmp,
            icmp6=icmp6,
            tcp=tcp,
            udp=udp,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             icmp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]] = None,
             icmp6: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]] = None,
             tcp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupTcpArgs']]]] = None,
             udp: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupUdpArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if icmp is not None:
            _setter("icmp", icmp)
        if icmp6 is not None:
            _setter("icmp6", icmp6)
        if tcp is not None:
            _setter("tcp", tcp)
        if udp is not None:
            _setter("udp", udp)

    @property
    @pulumi.getter
    def icmp(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]]:
        return pulumi.get(self, "icmp")

    @icmp.setter
    def icmp(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]]):
        pulumi.set(self, "icmp", value)

    @property
    @pulumi.getter
    def icmp6(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]]:
        return pulumi.get(self, "icmp6")

    @icmp6.setter
    def icmp6(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupIcmpArgs']]]]):
        pulumi.set(self, "icmp6", value)

    @property
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupTcpArgs']]]]:
        return pulumi.get(self, "tcp")

    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupTcpArgs']]]]):
        pulumi.set(self, "tcp", value)

    @property
    @pulumi.getter
    def udp(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupUdpArgs']]]]:
        return pulumi.get(self, "udp")

    @udp.setter
    def udp(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceGroupUdpArgs']]]]):
        pulumi.set(self, "udp", value)


class ServiceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 icmp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupIcmpArgs']]]]] = None,
                 icmp6: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupIcmpArgs']]]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupTcpArgs']]]]] = None,
                 udp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupUdpArgs']]]]] = None,
                 __props__=None):
        """
        Create a ServiceGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ServiceGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ServiceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ServiceGroupArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 icmp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupIcmpArgs']]]]] = None,
                 icmp6: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupIcmpArgs']]]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupTcpArgs']]]]] = None,
                 udp: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceGroupUdpArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceGroupArgs.__new__(ServiceGroupArgs)

            __props__.__dict__["icmp"] = icmp
            __props__.__dict__["icmp6"] = icmp6
            __props__.__dict__["tcp"] = tcp
            __props__.__dict__["udp"] = udp
            __props__.__dict__["service_group_id"] = None
        super(ServiceGroup, __self__).__init__(
            'veco:resources:ServiceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceGroup':
        """
        Get an existing ServiceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceGroupArgs.__new__(ServiceGroupArgs)

        __props__.__dict__["icmp"] = None
        __props__.__dict__["icmp6"] = None
        __props__.__dict__["service_group_id"] = None
        __props__.__dict__["tcp"] = None
        __props__.__dict__["udp"] = None
        return ServiceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def icmp(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceGroupIcmp']]]:
        return pulumi.get(self, "icmp")

    @property
    @pulumi.getter
    def icmp6(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceGroupIcmp']]]:
        return pulumi.get(self, "icmp6")

    @property
    @pulumi.getter(name="serviceGroupId")
    def service_group_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "service_group_id")

    @property
    @pulumi.getter
    def tcp(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceGroupTcp']]]:
        return pulumi.get(self, "tcp")

    @property
    @pulumi.getter
    def udp(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceGroupUdp']]]:
        return pulumi.get(self, "udp")

