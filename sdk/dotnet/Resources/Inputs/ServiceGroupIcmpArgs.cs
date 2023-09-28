// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Veco.Resources.Inputs
{

    public sealed class ServiceGroupIcmpArgs : global::Pulumi.ResourceArgs
    {
        [Input("codeHigh", required: true)]
        public Input<int> CodeHigh { get; set; } = null!;

        [Input("codeLow", required: true)]
        public Input<int> CodeLow { get; set; } = null!;

        [Input("icmpType", required: true)]
        public Input<int> IcmpType { get; set; } = null!;

        public ServiceGroupIcmpArgs()
        {
        }
        public static new ServiceGroupIcmpArgs Empty => new ServiceGroupIcmpArgs();
    }
}
