# Create review list of content

From time to time, it is healthy to review published content.
This helps to ensure ongoing quality of the information.
The challenge is to know what content to review, and when.

One way of identifying candidate content for review is by the simple assessment
of when the content was last modified.
While not perfect as a method,
it does provide a useful and consistent hint.

In the `buildUtils` folder, a script called `reviewList.sh` provides
a list of `.dita` files within the repository (current branch),
sorted by reverse date order.

So, the last files listed are the ones that have not been modified for some time.

## Running the script

1. Open a terminal window.
2. Use `git` to checkout the `main` branch:<br/>`git checkout main`
3. Run the script from a command prompt:<br/>`sh buildUtils/reviewList.sh`
