// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("veco");

/**
 * API key for the VCO
 */
export declare const vcoApiKey: string | undefined;
Object.defineProperty(exports, "vcoApiKey", {
    get() {
        return __config.get("vcoApiKey");
    },
    enumerable: true,
});

/**
 * FQDN of the VCO
 */
export declare const vcoUrl: string | undefined;
Object.defineProperty(exports, "vcoUrl", {
    get() {
        return __config.get("vcoUrl");
    },
    enumerable: true,
});

