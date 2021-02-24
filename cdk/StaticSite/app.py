#!/usr/bin/env python3

from aws_cdk import core

from static_site.static_site_stack import StaticSiteStack

Domains = ["adamw-build-sig-staticsite-test1", "adamw-build-sig-staticsite-test2"]

app = core.App()
for d in Domains:
    id = "static-site" + d
    StaticSiteStack(app, id, d)

app.synth()
