// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Veco.Resources.Inputs
{

    public sealed class ServiceGroupTcpArgs : global::Pulumi.ResourceArgs
    {
        [Input("portEnd", required: true)]
        public Input<int> PortEnd { get; set; } = null!;

        [Input("portStart", required: true)]
        public Input<int> PortStart { get; set; } = null!;

        public ServiceGroupTcpArgs()
        {
        }
        public static new ServiceGroupTcpArgs Empty => new ServiceGroupTcpArgs();
    }
}
