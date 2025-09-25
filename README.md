# Security guidance

## Overview

This repository contains best-practice guidance and - where appropriate - policy for Ministry of Justice (MoJ) technology security.

The information ranges from formal content, such as 'you must'-style documents, through to more informal help and suggestions, such as checklists.

The content is used to help build and operate products and services at the MoJ.

The work is performed in the open by intent, and for compliance with principle.
Re-use of these materials outside of MoJ purposes must be in accordance with the published license.

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

Information about setting up the build environment,
and building content,
is [here](buildUtils/BuildEnvironment.md).

You must set up the build environment to work with this repository.

To preview the site locally, after it is built, we need to use the terminal.

Install Ruby and [Bundler][bundler], preferably with a [Ruby version
manager][rbenv].
Ruby version 2.7.3 is known to work well for local builds.

[rbenv]: https://github.com/rbenv/rbenv#readme
[bundler]: http://bundler.io/

To specify where Ruby gems are installed for use by bundler, use a command similar to:
`bundle config set --local path '<location>'`

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

For more information about contributing content,
see [this description](buildUtils/contributingContent.md).
Please ask if you have questions or would like help - issues are the best way to contact the content team.

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
`git tag`

## The `encrypted` folder

Occasionally, there might be times when we need to work with material that is
sensitive in some way.
A good example is material that might be marked as `OFFICIAL-SENSITIVE`,
such as personal information.
Such material is still `OFFICIAL`,
but has the additional handling indicator ('`SENSITIVE`') to show that this
material should be treated with extra care.
A good rule of thumb is that the information is 'need to know',
and should not be shared in public.

This material can be stored in the `encrypted` folder,
where it is protected (encrypted) using the
[`git-crypt`](https://github.com/AGWA/git-crypt) tools.

Use of [`git-crypt`](https://github.com/AGWA/git-crypt) is normally for
repositories with only a small number of encrypted files;
the majority of files in the repository are plain text.
For this MoJ security-guidance repository,
it is expected that encrypted files will be exceptional,
rather than a common or frequent occurrence.
As a working measure,
the number of encrypted source files should not exceed 1% of the number of
source files in the repository.
If the 1% value is exceeded,
the use of [`git-crypt`](https://github.com/AGWA/git-crypt) will be reviewed.

You do not need to have [`git-crypt`](https://github.com/AGWA/git-crypt)
available to work with the majority
of materials in this repository.
If you don't have [`git-crypt`](https://github.com/AGWA/git-crypt),
the files in the `encrypted` directory are protected;
you can see they exist,
but you won't be able to see or work with the contents of the file.

### Getting access to the encrypted materials

For the vast majority of tasks,
there is no need to access or view the contents of the `encrypted` folder.

If you *really* feel there is a need to access the materials,
do the following:

1. Read about [`git-crypt`](https://github.com/AGWA/git-crypt).
2. Follow the [instructions](https://github.com/AGWA/git-crypt) to enable [`git-crypt`](https://github.com/AGWA/git-crypt) on your system.
3. Generate a GPG key - this will be used to enable your access to the `encrypted` folder.
4. Send an email request to [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk), indicating that you'd like access to the `encrypted` folder, and providing a very good business justification.
5. If your request is approved, you'll need to provide the GPG key generated in step 3.
