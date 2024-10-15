# Setting up a Visual Studio Code development and build environment

## Obtain and configure the DITA 1.2 DTDs

1. Download an archive containing the DITA version 1.2 DTDs. This can be found here: [http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip](http://docs.oasis-open.org/dita/v1.2/os/DITA1.2-dtds.zip).
2. Unzip the archive into a convenient folder, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Do _not_ have any spaces in any part of the path or filename.
3. In your local copy of the `buildUtils` folder of this repository, copy the file `catalog-dita-template.xml` to `catalog-dita.xml`.
4. Open the `catalog-dita.xml` file in any text editor of your choice.
5. Do a global search and replace: replace all instances of `DTDLOCATION` in `catalog-dita.xml` with the full location where you extracted the DITA version 1.2 DTDs, for example `/home/MySpace/installLocal/dtd1.2/`.<br/>Note: Don't forget the ending '`/`' character!
6. Save the `catalog-dita.xml` file.
7. Note the full pathname for this file, for example: `/home/MySpace/MyData/security-guidance/buildUtils/catalog-dita.xml`.

## Install Visual Studio Code

1. Go to the Visual Studio Code website.
2. [Download](https://code.visualstudio.com/download) an installation package.
3. Run the normal installation process for Visual Studio Code on your platform.
4. Start Visual Studio Code.


## Enable DITA awareness in Visual Studio Code

1. In Visual Studio Code, click **View** from the top menu.
2. Click **Extensions**.
3. In the Extensions search bar, type `XML`. 
4. Select and install the XML extension, developed by Red Hat.
5. Restart Visual Studio Code.
6. In the top menu, select **Code** > **Settings** > **Settings**.
7. In the settings search bar, type `catalog`.
8. Click **Add Item** and paste the full pathname for the `catalog-dita.xml` you created earlier, for example: `/Users/edward.prosser/installLocal/dtd1.2/catalog-dita.xml`.
9. Click **Ok**.
10. Restart Visual Studio Code.


## Test the XML awareness in Visual Studio Code

1. Open Visual Studio Code, Open the security-guidance repository. Navigate to one of the DITA files in your repository.
2. If you make modifications to the file that are invalid XML, or that are invalid DITA, you will now get an error or warning within Atom.


---

<!--
Fairly sure this instruction is now redundant, but keeping it here in a comment just in case we need to refer to it later.

Under the `core:` settings, add an entry that reads:
```
customFileTypes:
      "text.xml": [
        "dita"
        "ditamap"
        "ditaval"
  ]
```

>