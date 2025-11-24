# Security Guidance Table of Contents

The table of contents on the Security Guidance website is currently in a beta state. It is in the process of being built and updated, and so may not work perfectly in all situations. This internal document should set out how the ToC is generated and how to update it.

## Files to be aware of

The `jekyll-baseline` directory controls the baseline layout for the website. Within this directory, the `_data`, `_includes`, and `_layouts` directories contain all of the base files that create the website structure and design. 

- `_layouts`: includes the `default.html` file that sets the default website layout. It should not be altered without proper care and attention, because the changes will be reflected on every page on the security guidance site.
- `_includes`: includes page elements that are incorporated into the layout by reference. Specifically, it includes the table of contents (`toc.html`), header (`header.html`), footer (`footer.html`), analytics (`analytics.html`), and javascript elements.
- `_data`: includes raw data files that is incorporated in other files. Specifically, it includes the `tocList.yml` file that controls the ordering of pages in the table of contents.

## Arranging the table of contents

The table of contents is created based on two key files:
1. The `toc.html` file contains a script that iterates across `tocList.yml` to build an ordered list that is used in `default.html` to incorporate the table of contents. Once complete, this file is not expected to change.
2. The `tocList.yml` file contains a list of files with additional properties that define where in the table of contents an item should be placed. When a new page is added to the table of contents, it should be added to the `tocList.yml` file.

## Understanding the tocList file

The tocList file includes a list where properties appear as below:

```
- title: Mobile device and remote working policy
  url: /mobile-device-and-remote-working-policy
  toc-position: 2
  subfolderitems:
    - title: Remote Working
      url: /remote-working
    - title: Personal Devices
      url: /personal-devices
```

This entry defines a top-level table of contents item named "Mobile device and remote working policy" with the specified URL, and a toc-position of 2. This means it is second in the table of contents. It also defines two 'child' topics that will sit under that heading. The child topics are titled "Remote working" and "Personal Devices" and each has a specified URL. 

The properties in this list are:
- `title`: This will define the text that appears in the table of contents.
- `url`: This defines that end of the URL for the clickable link in the table of contents. You do **not** need to specify the general security guidance homepage URL, only the subfolder that the page sits in. It is **very important** that you include a `/` at the start, as without this the link will break.
- `toc-position`: This property is only used for top-level table of contents entries. Entries that sit underneath another heading must not include this property. This number is used to order the table of contents when it is built by the script in `toc.html`.
- `subfolderitems`: This property is a container property that holds all of the child topics under a heading. Each child topic must include a `title` and `url` element in order to be displayed.

