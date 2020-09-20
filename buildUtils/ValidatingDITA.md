# Checking you have valid DITA


DITA is an XML format. In addition to being well-formed (balancing `<p>` and `</p>` tags, for example), the XML must be valid according to the DITA schema.

Checking that you have valid DITA is a time-saver when trying to debug why a DITA build might not be working correctly.


The resulting DITA file will require some attention, but will be usable quickly and easily.

To illustrate the process, this guide will 'walk through' the conversion of a Markdown file, `markdown-content.md`.
The guide assumes that the Markdown file is already in a directory called `tmp`.

## Install and configure your build environment

1. Check that you have a working DITA Open Toolkit environment, as described in the [Setting up a DITA development and build environment](BuildEnvironment.md) document.
2. Add the DITA XML validator plugin, by running this command:<br/>`dita install com.here.validate.svrl`

## Check your DITA files

1. Navigate to the `dita` directory where your content source is stored.
2. (Optional) The Validator tool does not expect duplicate DITA files in subdirectories, and might fail with a RegExp error. If this happens, try removing the `out` sub-directory.
3. Locate the ditamap that structures your content during a build. We'll assume the ditamap is called `moj-guidance.ditamap`.
4. Run the validator, using a command similar to the following:<br/>`dita -f svrl -i moj-guidance.ditamap`
5. Any problems are reported, with an indication of where the problem is located in a given file.

The Validator warns you of problems that might affect later versions of DITA. For example, the `navtitle` attribute in a `topicref` element will be deprecated in later versions of DITA. You can safely ignore this warning. 

## For more information...

See the Validator project page, [here](https://dita-validator-for-dita-ot.readthedocs.io/en/latest/).

The Validator is one of (many) DITA [plugins](https://www.dita-ot.org/plugins).
