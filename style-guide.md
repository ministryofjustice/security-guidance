# Ministry of Justice - Security Guidance and Policy Style Guide

## Audience

This guide is for anyone who is drafting and reviewing security material for the Ministry of Justice.

## Goal

Writing and reviewing guidance and policy content can be a time-consuming activity. This guide sets out some principles to help ensure that the content you help create is of a suitable quality for easy review, quick publication, and - most importantly - achieves what you intend and helps to keep the MoJ more secure.

## Style Guide

We follow the approach that the Government Digital Service (GDS) [Writing for GOV.UK](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) guide, and the GOV.UK [Style Guide](https://www.gov.uk/guidance/style-guide) recommends.

## Drafting Approach

Before starting to draft content it is helpful to think about what goal you wish to achieve. For example, it is not sensible to start with "I need to write guidance on Bluetooth", but instead to think about the goals you're trying to achieve - and more importantly, which user communities within the MoJ we want to help do something. So for this we might instead think:

- What approach should our system administrators take to Bluetooth devices when configuring their systems?
- What do our end users need to know about Bluetooth devices and how to stay secure when using them?

## Call to action

It can be tempting to write down everything you know about a topic, but accidentally forget to include an action for your reader to take. This is a good way to frustrate our readers, and write content that's hard to maintain. Always ensure you include a clear action for the reader to take!

## Keep it simple

Dazzingly readers with your knowledge and expertise is _lovely_ but can often confuse the simple message we want to communicate. Less is indeed more! A rule of thumb is if you can cross out every other word and things still make sense, you can cut some more!

## Look for opportunities to reuse

If there's content we've got that works, then reuse it through inclusion!

## The hard bit

Our documentation uses [DITA](https://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture) as the source format.
DITA enables us to re-use content more easily, build output in a variety of formats, and significantly improve the Accessibility of content.

### The content creation process

DITA source is stored in the `dita` folder. The content files are written using an XML editor, that is 'DITA aware'. For more information, see [Setting up a DITA development and build environment](./buildUtils/BuildEnvironment.md).

When a build is required, or for preview purposes, the `builder.ant` script in the `buildUtils` directory is run. By default, it will create Markdown, PDF, and EPUB format output. The result output documents are put into the `docs` directory.

*Note:* The `docs` directory is cleaned out and rebuilt freshly for each build. This means that issuing a GitHub Pull Request that creates or modifies content in the `docs` directory will always require additional effort; this is factored in to the evaluation of the PR.
