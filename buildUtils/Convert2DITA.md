# Converting Markdown files to DITA

The DITA Open Toolkit 'understands' Markdown format. You can use the toolkit to convert content written using Markdown into a baseline DITA format.

The resulting DITA file will require some attention, but will be usable quickly and easily.

To illustrate the process, this guide will 'walk through' the conversion of a Markdown file, `markdown-content.md`.
The guide assumes that the Markdown file is already in a directory called `tmp`.

## Install and configure your build environment

1. Check that you have a working DITA Open Toolkit environment, as described in the [Setting up a DITA development and build environment](BuildEnvironment.md) document.
2. (Optional) Obtain and install the `xmllint` file formatting tool.

## Check and tidy the Markdown file content

The DITA Open Toolkit is very good at converting from markdown to DITA, but doing some simple 'cleaning' beforehand can make life simpler.

1. Remove any non-essential 'meta' data from the start of the markdown file, for example:
  ```
  ---
  title: My File
  ---

  ```
2. Ensure that headings increment and decrement logically. For example, going straight to a Level 2 `##` heading is an error for DITA conversion. Similarly, jumping straight from a Level 1 `#` to a Level 3 `###` heading is not permitted.

## Create a basic ditamap to manage the conversion

The ditamap provides information to the DITA Open Toolkit to help it understand the incoming source format.

Create a ditamap file called (for example) `convert.ditamap` in the `tmp` directory. It should look like this:
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd">

<map>
  <topicref href="markdown-content.md" type="topic" format="markdown"/>
</map>
```

Remember to change the name in the `href` attribute so that it refers to the file you want to convert.

## Run the conversion process

Use the following command to convert the markdown file:
```
dita --input=convert.ditamap --format=dita
```

If the process works correctly, a sub-directory (`tmp/out`) is created, containing a copy of the ditamap and _also_ a file called `markdown-content.md`.
If you open this file in an editor, you'll see that it contains DITA source.

if the process does not work correctly, pay attention to - and fix - the errors. Fix the first error first; an early problem encountered by the toolkit often produces subsequent errors. These go away when the first problem is fixed.

## Rename and reformat the DITA file

As a minimum, rename the `tmp/out/markdown-content.md` file to `tmp/markdown-content.dita`

However, if you have the `xmllint` tool installed, you can also reformat the DITA file to make it easier to read, using the following command:
```
xmllint --format out/markdown-content.md > markdown-content.dita
```

## Final step

The DITA Open Toolkit automatically included `specialization=""` attributes for some elements. If you are using specializations, these are helpful, and you'll know what to do with them.
However, for simple markdown to Dita conversion, these attributes are not required.

Remove them all from the DITA file by doing a global search-and-replace to remove all instances of the `specialization=""` attribute.

You now have a DITA version of the original markdown file, ready for inclusion in your content project.
