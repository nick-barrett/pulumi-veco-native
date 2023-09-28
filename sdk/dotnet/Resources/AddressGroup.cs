// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Veco.Resources
{
    [VecoResourceType("veco:resources:AddressGroup")]
    public partial class AddressGroup : global::Pulumi.CustomResource
    {
        [Output("addressGroupId")]
        public Output<int> AddressGroupId { get; private set; } = null!;

        [Output("domains")]
        public Output<ImmutableArray<string>> Domains { get; private set; } = null!;

        [Output("prefixes")]
        public Output<ImmutableArray<string>> Prefixes { get; private set; } = null!;


        /// <summary>
        /// Create a AddressGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AddressGroup(string name, AddressGroupArgs args, CustomResourceOptions? options = null)
            : base("veco:resources:AddressGroup", name, args ?? new AddressGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AddressGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("veco:resources:AddressGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AddressGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AddressGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AddressGroup(name, id, options);
        }
    }

    public sealed class AddressGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("domains", required: true)]
        private InputList<string>? _domains;
        public InputList<string> Domains
        {
            get => _domains ?? (_domains = new InputList<string>());
            set => _domains = value;
        }

        [Input("prefixes", required: true)]
        private InputList<string>? _prefixes;
        public InputList<string> Prefixes
        {
            get => _prefixes ?? (_prefixes = new InputList<string>());
            set => _prefixes = value;
        }

        public AddressGroupArgs()
        {
        }
        public static new AddressGroupArgs Empty => new AddressGroupArgs();
    }
}
