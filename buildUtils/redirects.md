# Redirecting published files

From time to time, it might be necessary to move files around within the build.
The problem is that some projects or services might expect the files to be in their old locations.

It is straightforward to enable a redirect **from** the old page location **to** the new page location.

This is made possible by a very useful plugin: [jekyll-redirect-from](https://github.com/jekyll/jekyll-redirect-from).

In this example, we will assume that the file:
```
https://ministryofjustice.github.io/security-guidance/guides/defensive-domain-registration/
```
... is being relocated to:
```
https://ministryofjustice.github.io/security-guidance/defensive-domain-registration/
```

In other words, the page has been moved 'up' a level.

To enable this redirection within the build, do the following:

1. Create a file in the `redirects` folder. The name of the file should be *exactly* the same as the name of the page being relocated, for example `defensive-domain-registration`. **Note:** The file name does **not** have a file type. For example, calling the file `defensive-domain-registration.md` **is incorrect**.
2. Open the file `defensive-domain-registration` in a text editor.
3. Add the following lines into the file:
  ```
  ---
  redirect_from:
    - /guides/defensive-domain-registration/
  ---

  ```
4. This tells the redirect system **the old page location**. Any requests for content at the old page location will be redirected automatically to the new location.


## Redirecting to an external site

Redirecting to an external website is generally **not preferred**. If we are redirecting to sources that we do not control, we are at the mercy of third-parties (even within the civil service) moving pages, adding their own redirects, or changing the content that we are linking to. 

In the event that we absolutely need to redirect a page to an external website, follow the above steps, but replace the redirect file contents with the following:

```
---
redirect_to: https://<url>.com
___
```

The above example will redirect our page to https://<url>.com.