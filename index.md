# MOJ security  guidance

This site documents some of the security decisions that the
[Ministry of Justice](https://www.gov.uk/government/organisations/ministry-of-justice)
has made for the products we operate and our relationships with suppliers.

[Technical guidance](https://ministryofjustice.github.io/technical-guidance/) covers technical decisions in the MOJ more widely.

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
  | where: "supplier", true
  | group_by: "category" %}

{% for supplier_group in suppliers %}
{% if supplier_group.name != "" %}
### {{ supplier_group.name }}
{% else %}
### General notes to suppliers
{% endif %}

{% for supplier in supplier_group.items %}
- [{{ supplier.title }}]({{ supplier.url | relative_url }})
{% endfor %}
{% endfor %}

## Mythbusting

{% assign mythbustings = site.pages
  | where: "mythbusting", true 
  | group_by: "category" %}

{% for myth_group in mythbustings %}
{% if myth_group.name != "" %}
### {{ myth_group.name }}
{% endif %}

{% for myth in myth_group.items %}
- [{{ myth.title }}]({{ myth.url | relative_url }})
{% endfor %}
{% endfor %}

## Technical Guidance

The [technical guidance](https://ministryofjustice.github.io/technical-guidance/) should be read together with this security-focused guidance.

## Getting in touch

{% assign contacts = site.pages
  | where: "contact", true
  | group_by: "category" %}

{% for contact_group in contacts %}
{% if contact_group.name != "" %}
### {{ contact_group.name }}
{% else %}
### General information
{% endif %}

{% for contact in contact_group.items %}
- [{{ contact.title }}]({{ contact.url | relative_url }})
{% endfor %}
{% endfor %}
