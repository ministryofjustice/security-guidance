# Setting up an Atom development and build environment

## Obtain and configure the DITA 1.2 DTDs

1. Download an archive containing the DITA version 1.2 DTDs. This can be found here: [http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip](http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip).
2. Unzip the archive into a convenient folder, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Do _not_ have any spaces in any part of the path or filename.
3. In your local copy of the `buildUtils` folder of this repository, copy the file `catalog-dita-template.xml` to `catalog-dita.xml`.
4. Open the `catalog-dita.xml` file in any text editor of your choice.
5. Do a global search and replace: replace all instances of `DTDLOCATION` in `catalog-dita.xml` with the full location where you extracted the DITA version 1.2 DTDs, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Don't forget the ending '`/`' character!
6. Save the `catalog-dita.xml` file.
7. Note the full pathname for this file, for example: `/home/MySpace/MyData/security-guidance/buildUtils/catalog-dita.xml`.

## Install Atom

1. Go to the [Atom](atom.io) website.
2. Download an installation package.
3. Run the normal install for a package on your platform.
4. Start atom.
5. Click `Edit` then `Preferences` then `Updates`. Click `Check for Updates`. Ensure that all the Atom packages are up-to-date. (Remember to repeat this check at regular intervals, to keep your installation secure and patched with all the latest fixes.)
6. Close (quit) the Atom editor.

## Enable DITA awareness in Atom

1. Open a terminal.
2. Run the command:<br/>`apm install linter-autocomplete-jing`.<br/>Note: You do _not_ need to be a system administrator to install the 'autocomplete' package.
3. Start Atom. You'll be asked if you want to install the `linter` dependency. This is necessary, so click `Yes`. Afterwards, close (quit) the Atom editor.
4. Start Atom. You'll be asked if you want to install `linter-ui-default` and some other dependencies. These are necessary, so click `Yes`. Afterwards, close (quit) the Atom editor.
5. Start Atom.
6. Click `Edit` then `Preferences` then `Packages`. The 'linter-autocomplete-jing' package should appear in the list of 'Community Packages'. Click the `Settings` option for the package.
7. Scroll down to the `XML Catalog` field, and enter the full pathname for the `catalog-dita.xml` you created earlier, for example: `/home/MySpace/MyData/security-guidance/buildUtils/catalog-dita.xml`.
8. Close the 'Settings' tab.
9. Click `Edit` then `Config`.
10. Under the `core:` settings, add an entry that reads:
```
customFileTypes:
      "text.xml": [
        "dita"
        "ditamap"
        "ditaval"
  ]
```
11. Save your changes, then close the `config.cson` tab.
12. Close (quit) the Atom editor.

## Test the XML awareness in Atom

1. Open Atom, then click `File` then `Open`. Navigate to one of the DITA files in your repository.
2. If you make modifications to the file that are invalid XML, or that are invalid DITA, you will now get an error or warning within Atom.
