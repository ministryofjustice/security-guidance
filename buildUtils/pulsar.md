# Setting up an Pulsar development and build environment

## Obtain and configure the DITA 1.2 DTDs

1. Download an archive containing the DITA version 1.2 DTDs. This can be found here: [http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip](http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip).
2. Unzip the archive into a convenient folder, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Do _not_ have any spaces in any part of the path or filename.
3. In your local copy of the `buildUtils` folder of this repository, copy the file `catalog-dita-template.xml` to `catalog-dita.xml`.
4. Open the `catalog-dita.xml` file in any text editor of your choice.
5. Do a global search and replace: replace all instances of `DTDLOCATION` in `catalog-dita.xml` with the full location where you extracted the DITA version 1.2 DTDs, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Don't forget the ending '`/`' character!
6. Save the `catalog-dita.xml` file.
7. Note the full pathname for this file, for example: `/home/MySpace/MyData/security-guidance/buildUtils/catalog-dita.xml`.

## Install Pulsar

1. Go to the [Pulsar](pulsar-edit.dev) website.
2. Download an installation package.
3. Run the normal install for a package on your platform.
4. Start Pulsar.
5. Click `Edit` then `Preferences` then `Updates`. Click `Check for Updates`. Ensure that all the Pulsar packages are up-to-date. (Remember to repeat this check at regular intervals, to keep your installation secure and patched with all the latest fixes.)
6. Close (quit) the Pulsar editor.

## Enable DITA awareness in Pulsar

1. Open a terminal.
2. Run the command:<br/>`pulsar -p install linter-autocomplete-jing`.<br/>Note: You do _not_ need to be a system administrator to install the package.
3. Run the command:<br/>`pulsar -p install linter`.
4. Run the command:<br/>`pulsar -p install linter-ui-default`.
5. Start Pulsar. You might be asked to install other dependencies. These are necessary, so click `Yes`. Afterwards, close (quit) the Pulsar editor.
6. Start Pulsar.
7. Click `Edit` then `Preferences` then `Packages`. The 'linter-autocomplete-jing' package should appear in the list of 'Community Packages'. Click the `Settings` option for the package.
8. Scroll down to the `XML Catalog` field, and enter the full pathname for the `catalog-dita.xml` you created earlier, for example: `/home/MySpace/MyData/security-guidance/buildUtils/catalog-dita.xml`.
9. Close the 'Settings' tab.
10. Click `Edit` then `Config`.
11. Under the `core:` settings, add an entry for `customFileTypes` that reads:
```
"*":
  core:
    customFileTypes:
      "text.xml": [
        "dita"
        "ditamap"
        "ditaval"
      ]
```
12. Save your changes, then close the `config.cson` tab.
13. Close (quit) the Pulsar editor.

## Test the XML awareness in Pulsar

1. Open Pulsar, then click `File` then `Open`. Navigate to one of the DITA files in your repository.
2. If you make modifications to the file that are invalid XML, or that are invalid DITA, you will now get an error or warning within Pulsar.
