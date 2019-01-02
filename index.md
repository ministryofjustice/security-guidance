# MOJ security  guidance

This site documents some of the security decisions that the
[Ministry of Justice](https://www.gov.uk/government/organisations/ministry-of-justice)
has made for the products we operate.

It complements the [technical guidance](https://ministryofjustice.github.io/technical-guidance/),
which covers technical decisions in the MOJ more widely.

## Principles

{% assign principle_groups = site.pages
  | where: "principle", true %}

{% for principle in principle_groups %}
- [{{ principle.title }}]({{ principle.url | relative_url }})
{% endfor %}

## Standards

{% assign standards = site.pages
  | where: "standard", true
  | group_by: "category" %}

{% for standard_group in standards %}
{% if standard_group.name != "" %}
### {{ standard_group.name }}
{% else %}
### General standards
{% endif %}

{% for standard in standard_group.items %}
- [{{ standard.title }}]({{ standard.url | relative_url }})
{% endfor %}
{% endfor %}

## Guides

{% assign guides = site.pages
  | where: "guide", true
  | group_by: "category" %}

{% for guide_group in guides %}
{% if guide_group.name != "" %}
### {{ guide_group.name }}
{% else %}
### General guides
{% endif %}

{% for guide in guide_group.items %}
- [{{ guide.title }}]({{ guide.url | relative_url }})
{% endfor %}
{% endfor %}

## Suppliers to MOJ

{% assign suppliers = site.pages
  | where: "suppliers", true
  | group_by: "category" %}

{% for supplier_group in suppliers %}
{% if supplier_group.name != "" %}
### {{ supplier_group.name }}
{% else %}
### Suppliers to MOJ
{% endif %}

{% for supplier in supplier_group.items %}
- [{{ supplier.title }}]({{ supplier.url | relative_url }})
{% endfor %}
{% endfor %}

## Mythbusting

{% assign mythbusting = site.pages
  | where: "mythbusting", true 
  | group_by: "category" %}

{% for myth_group in mythbusting %}
{% if myth_group.name != "" %}
### {{ myth_group.name }}
{% else %}
### Mythbusting
{% endif %}

{% for myth in myth_group.items %}
- [{{ myth.title }}]({{ myth.url | relative_url }})
{% endfor %}
{% endfor %}

## Reporting an incident

MOJ colleagues should visit https://intranet.justice.gov.uk/guidance/security/report-a-security-incident/ on the MOJ Intranet.

Suppliers to the MOJ should refer to provided methods/documentation and contact your usual MOJ points of contact.

## Adding new guidance

Create a new Markdown file that follows this pattern, add a link to it
from this page, and make a pull request:

```markdown
---
category: The broader area this fits into
expires: yyyy-mm-dd (6 months from now)
---
# Thing you're writing about

Introduction of a couple of paragraphs to explain why the thing you're
writing about is important. The [title should probably be a verb, not a
noun][good-services-are-verbs] (e.g. “Storing source code”, not “Code
repositories”).

[good-services-are-verbs]: https://designnotes.blog.gov.uk/2015/06/22/good-services-are-verbs-2/

## User needs

Why do we do this thing? Who is it helping?

## Principles

What broad approaches do we follow when we do this thing?

## Tools

What specific bits of software (commercial or open source) do
we use to help us do this thing?
```

The service manual has some useful information on
[learning about and writing user needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs).
