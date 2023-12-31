package config

import (
	"github.com/nick-barrett/pulumi-veco/provider/pkg/provider/api"
	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
)

type VecoConfig struct {
	Url    string `pulumi:"vcoUrl"`
	ApiKey string `pulumi:"vcoApiKey" provider:"secret"`

	client api.Client
}

var _ = (infer.CustomCheck[*VecoConfig])((*VecoConfig)(nil))

func (c *VecoConfig) Check(ctx p.Context, name string, oldInputs, newInputs resource.PropertyMap) (*VecoConfig, []p.CheckFailure, error) {
	c.Url = newInputs["vcoUrl"].StringValue()
	c.ApiKey = newInputs["vcoApiKey"].StringValue()

	return c, []p.CheckFailure{}, nil
}

var _ = (infer.Annotated)((*VecoConfig)(nil))

func (c *VecoConfig) Annotate(a infer.Annotator) {
	a.Describe(&c.Url, "FQDN of the VCO")
	a.Describe(&c.ApiKey, "API key for the VCO")
}

var _ = (infer.CustomConfigure)((*VecoConfig)(nil))

func (c *VecoConfig) Configure(ctx p.Context) error {
	c.client = api.NewClient(c.Url, c.ApiKey, 10)
	return nil
}

func (c *VecoConfig) Client() *api.Client {
	return &c.client
}
