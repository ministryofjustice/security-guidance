# Contributing content

## Overview

Contributions to the content are welcome.
The contributions should normally be in [DITA](https://en.wikipedia.org/wiki/Darwin_Information_Typing_Architecture) format.
Submissions in other formats are also acceptable, but take longer to review and - if accepted - merged into the build.

Content in DITA format should be submitted for inclusion in the `dita` folder.
Content in other formats,
such as [GitHub Flavored Markdown](https://github.github.com/gfm/) (GFM),
should be submitted for inclusion in the appropriate source folder.
If you are not sure which format or folder to use,
please [open an issue](https://github.com/ministryofjustice/security-guidance/issues).

All contributions into GitHub must be [signed.](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).

# Step-by-step

The basic process is as follows:

1.  Fork a copy of the [MoJ Security Guidance repository](https://github.com/ministryofjustice/security-guidance) within GitHub.
2.  Create a [feature branch](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) from the `main-preproduction` branch.
3.  Make your suggested changes, making sure that all commits are [signed](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).
4.  Submit the changes as a [GitHub Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) (PR).

When the PR is received, your suggestions are reviewed.
If they are accepted, the PR is accepted and merged into the `main-preproduction` content.
This places your suggested content into the source folder,
but does *not* immediately result in any changes to the published content.

Behind the scenes,
a further process is initiated when the PR is accepted.
A repository owner will:

1.  Create a fresh feature branch to bring your source content into the published build.
2.  A local build is run using the feature branch, to confirm that the changes are correct and do not adversely or incorrectly impact existing approved and published content.
3.  A 'Request Approval to Publish' (RAP) issue is opened, and marked for the attention of the content owner.
4.  The content owner approves the publication of the changes.
5.  The feature branch is merged into the `main` branch.
6.  A local build is run, creating 'camera ready' publication content.
7.  The new build is pushed to GitHub; this publishes the new material.
8.  (Optional) A note is added to the original PR, advising that publication has taken place.
