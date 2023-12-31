// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Veco
{
    [VecoResourceType("pulumi:providers:veco")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// API key for the VCO
        /// </summary>
        [Output("vcoApiKey")]
        public Output<string> VcoApiKey { get; private set; } = null!;

        /// <summary>
        /// FQDN of the VCO
        /// </summary>
        [Output("vcoUrl")]
        public Output<string> VcoUrl { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("veco", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "vcoApiKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("vcoApiKey", required: true)]
        private Input<string>? _vcoApiKey;

        /// <summary>
        /// API key for the VCO
        /// </summary>
        public Input<string>? VcoApiKey
        {
            get => _vcoApiKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _vcoApiKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// FQDN of the VCO
        /// </summary>
        [Input("vcoUrl", required: true)]
        public Input<string> VcoUrl { get; set; } = null!;

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
