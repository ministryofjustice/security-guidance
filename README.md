# Security guidance

## Overview

This repository contains best-practice guidance and - where appropriate - policy for Ministry of Justice (MOJ) technology security.

The information ranges from formal content such as 'you must'-style documents, through to more informal help and suggestions, such as checklists.

The content is used to help build and operate products at the MOJ.

The work is performed in the open by intent and for compliance with principle.
There is no specific aim or expectation of re-use of these materials outside of MOJ purposes - but people are welcome to do so if they wish in accordance with the published license.

Note: As a vibrant, dynamic, work-in progress, this the material should not necessarily be treated as formal, finished, definitive, accurate, etc.

## Repository details

This repo is inspired by, and borrows from, [GDS's technical guidance][gds-way] site and [MOJ's technical guidance][technical-guidance].

Content in the `master` branch is built using [Jekyll][], and hosted using [GitHub Pages][]. It incorporates HTML, SCSS, JavaScript, and images from [GDS's Tech Docs Template][tech-docs-template], and reworks them to work with Jekyll instead of [Middleman][].

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
dependencies by running the following in this directory:

```bash
bundle install
```

## Making changes

To make changes, edit the appropriate Markdown files in this project.
Jekyll (and therefore this site) uses [kramdown][] for its Markdown
processing.

Make sure to make changes in a branch, and issue a [pull request](https://help.github.com/articles/about-pull-requests/) when
you want them to be reviewed and published.

[kramdown]: https://kramdown.gettalong.org/syntax.html

## Previewing

We can preview our changes locally by running this command:

```bash
bundle exec jekyll serve --watch
```

This will create a local web server, probably at `http://127.0.0.1:4000`
(look for the `Server address:` line). This is only accessible on our
own computer, and won't be accessible to anyone else. It's also set up
to automatically update (thanks to `--watch`) when we make changes to
the working Markdown files.

## Publishing changes

Because we're using GitHub Pages, any changes merged into the `master`
branch will be published automatically. Every change should be reviewed
in a pull request, no matter how minor, and we've enabled [branch protection][] to enforce this.

[branch protection]: https://help.github.com/articles/about-protected-branches/
