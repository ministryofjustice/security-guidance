# Security guidance

## Overview

This repository contains best-practice guidance and - where appropriate - policy for Ministry of Justice (MoJ) technology security.

The information ranges from formal content, such as 'you must'-style documents, through to more informal help and suggestions, such as checklists.

The content is used to help build and operate products and services at the MoJ.

The work is performed in the open by intent, and for compliance with principle.
There is no specific aim or expectation of re-use of these materials outside of MoJ purposes - but people are welcome to do so if they wish in accordance with the published license.

*Note:* As a vibrant, dynamic, work-in progress, this material should not necessarily be treated as formal, finished, definitive, or accurate.

## Repository details

This repo is inspired by, and borrows from, [GDS's technical guidance][gds-way] site and [MoJ's technical guidance][technical-guidance].

Content in the `main` branch is created in [DITA](https://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture) format, and stored in the `dita` directory. When a build is required, the `builder.ant` script in the `buildUtils` directory is run. By default, it creates Markdown, PDF, and EPUB format output. The result output documents are put into a *clean* `docs` directory.

Content in the `docs` directory can be built and previewed using [Jekyll][], and hosted using [GitHub Pages][]. It incorporates HTML, SCSS, JavaScript, and images from [GDS's Tech Docs Template][tech-docs-template], reworked to use Jekyll instead of [Middleman][].

[gds-way]: https://github.com/alphagov/gds-way
[technical-guidance]: https://ministryofjustice.github.io/technical-guidance/
[Jekyll]: https://jekyllrb.com
[GitHub Pages]: https://pages.github.com
[tech-docs-template]: https://github.com/alphagov/tech-docs-template
[Middleman]: https://middlemanapp.com

All commits must be [signed](https://help.github.com/articles/signing-commits/).

Information about contributing is provided [here](#making-changes).

## Getting started

To preview the site locally, we need to use the terminal.

Install Ruby and [Bundler][bundler], preferably with a [Ruby version
manager][rvm].

[rvm]: https://www.ruby-lang.org/en/documentation/installation/#managers
[bundler]: http://bundler.io/

Once you have Ruby and Bundler set up, you can install this project's
dependencies by running the following in the `docs` directory:

```bash
bundle install
```

## Making changes

The **correct** way to make changes is by editing the appropriate DITA XML files in the `dita` directory. The `builder.ant` script in the `buildUtils` directory is used to create output content from the DITA source.

Any changes you want to suggest must be created in a branch, and submitted using a [pull request](https://help.github.com/articles/about-pull-requests/) when you want them to be reviewed and potentially published.

[kramdown]: https://kramdown.gettalong.org/syntax.html

The **tolerated** way of making changes is by editing an existing Markdown file in the `docs` directory. Be aware that changes made in the `docs` directory are non-persistent, and are overwritten by the build process.

## Previewing

We can preview content in the `docs` directory, locally, by running this command:

```bash
bundle exec jekyll serve --watch
```

This will create a local web server, probably at `http://127.0.0.1:4000`
(look for the `Server address:` line). This is only accessible on our
own computer, and won't be accessible to anyone else. It's also set up
to automatically update (thanks to `--watch`) when we make changes to
the working Markdown files.

## Publishing changes

Because we're using GitHub Pages, any changes merged into the `main`
branch `docs` directory will be published automatically. Every change should be reviewed
in a pull request, no matter how minor, and we've enabled [branch protection][] to enforce this.

[branch protection]: https://help.github.com/articles/about-protected-branches/

## Publishing on the Intranet

Every time a build run takes place, a working copy of the
Intranet material is placed in the [intranet](intranet) folder.

Whenever an Intranet publication is required, the following process is used:

1. Create an annotated tag for the repository, using the following template:
    `git tag -a YYYYMMDD -m "Intranet Snapshot YYYYMMDD"`
    The YYYYMMDD is the date of the snapshot. For example:
    `git tag -a 20210205 -m "Intranet Snapshot 20210205"`
2. Upload the tag into GitHub, using the following template:
    `git push origin YYYYMMDD`
    For example:
    `git push origin 20210205`
3. Create a `.zip` file containing the contents of the `intranet` folder.
4. Submit the zip file to the Comms team for publication.

To get a list of the annotated tags, use the command:
`git show`
