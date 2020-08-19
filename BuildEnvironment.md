# Setting up a DITA development and build environment

## Install Eclipse

1. Download the installer for the Eclipse IDE environment from [eclipse.org/downloads](eclipse.org/downloads). At the time of writing, the current version of Eclipse is 2020-06.
2. Unpackage the installer in a convenient temporary folder.
3. Run the installer:<br/>`eclipse-inst`
4. You'll be asked what configuration of Eclipse you want. Any will do, but really you want Git and XML components, which come as standard in the Eclipse IDE for Java Developers, so choose that one.
5. The installer will check that you have a suitable Java environment (needed to run Eclipse and DITA tooling). It'll suggest directories to install these components. You can change them if you wish (take notes!), but accepting the defaults is a good idea.
6. Read and understand the User Agreement.
7. Click the Install button to start installation. The process will take a few minutes, depending on network speed and which configuration you chose to install.
8. During installation, you might be asked to accept unsigned content. This refers to Ecipse components, so accept this.
9. When Installation completes, you'll be invited to run the application. Do so by clicking the Launch button.
10. Accept the default workspace for now. Click Launch.
11. The Welcome page appears in the newly launch IDE.
12. Click the 'X' icon to close the Welcome page.
13. Click the Help Menu, and select the Check for Updates option. The IDE contacts the Eclipse software sites, and will check for any updates that need to be installed.
14. If any updates are required, install them. You will need to restart Eclipse to complete the installation of updates.
15. After the IDE has updated, exit from the IDE and proceed to the next task (installing an XML editor).

## Installing an XML editor

1. Start eclipse. Do this by going to the installation directory (for example, `~/eclipse/java-2020-06/eclipse`) then run the `./eclipse` command.
2. Wait for the IDE to start. Accept the default workspace for now.
3. Click the Help menu, and select the Install New Software option.
4. In the Available Software window, select the Work with drop-down. Choose `--All available sites`.
5. In the filter text box, type `XML <enter>` This will filter the available software and show you the packages that mention XML in some way.
6. Scroll down the list to find 'Programming Languages', and select the 'Eclipse XML Editors and Tools' package. Don't worry about the version number; it'll always be the latest version.
7. Click `Next>`.
8. The Install Details window lets you check which package(s) are about to be installed. Click `Next>`.
9. On the Review Licenses window, review and understand the licenses, then check the `I accept...` option. Click `Finish`.
10. Wait for a short time while the package(s) download and install. You are then asked to restart the IDE to apply the software update. Click `Restart Now`.
11. To exit the IDE, click the `File` menu then select the `Exit` option.

## Installing a markdown editor

1. Start the IDE.
2. Click the Help menu, and select the Eclipse Marketplace option.
3. In the Find box, type `markdown` and click the `<Enter>` key.
4. Find the `Markdown Text Editor` in the list of packages. Click `Install`.
5. Accept the License agreement, then click Finish.
6. This is a package from the marketplace, so a warning appears. Click Install anyway.
7. Restart the IDE when asked to do so.
8. Exit from the IDE.

## Installing DITA (pre-requisite)

1. Open a terminal.
2. Run the command: `java --version`.
3. Check that the response confirms that Java is installed on your system.
4. If Java is not installed, address this before proceeding.

## Installing DITA

1. Open a web browser, and go to [the DITA Open Toolkit website](www.dita-ot.org).
2. Click the Download button, to download the latest version.
3. In a terminal, create a directory to install the DITA Open Toolkit. For example: `~/installLocal`. Change to this directory.
4. Extract the toolkit contents from the archive you just downloaded. This will extract into a directory named according to the toolkit version, for example `~/installLocal/dita-ot-3.5.2`.

### Test the DITA installation

1. Change into the Toolkit installation directory.
2. Set up the build environment by running the `startcmd.sh` script. Don't worry about the deprecation notice.
3. Within the DITA directory, change into the `docsrc/samples` directory.
4. Run the command:</br>`dita --input=sequence.ditamap --format=pdf`
5. Look into the newly created `out` folder. You should see a file `sequence.pdf`. Open this with a PDF reader, and check that there is content in there, about 'Working in the garage'.
6. If you have the content, your DITA Toolkit installation is working correctly.

## Add DITA awareness to the XML editor

1. Open the Eclipse Preferences (Window -> Preferences or (Mac) Eclipse -> Preferences).
2. Expand the XML section, and select `XML Catalog`.
3. Click the Add button.
4. Click the `Next Catalog` button.
5. Find the catalog file by clicking the `File System...` button, and navigating to the directory where the DITA Toolkit is installed. Select the `catalog-dita.xml` file, and click Open.
6. Click OK.
7. Click `Apply and Close`.
8. Open the Preferences menu again.
9. In the `type filter text` search field, enter `file`.
10. Select the General -> Editors -> File Associations option.
11. Click the `Add` button _next to the File Types section_.
12. Enter `*.dita` in the File type field, then click OK.
13. With the `*.dita` file type highlighted, click the `Add` button _next to the Associated editors section_.
14. Scroll down the list of editors, select the XML Editor, and click OK.
15. At the top of the File Associations Preferences window, click the 'See Content Types' link.
16. Expand the Text twisty in the Content types block.
17. Select the XML option - don't bother to expand the twisty.
18. With the XML option selected, click the `Add` button _next to the File association section_.
19. Enter `*.dita` in the Content type field, then click OK.
20. Select the `*.dita*` File association type, then select the XML editor in the Associated editors section.
21. Click the Apply and Close button.
22. Repeat steps 8 to 21 inclusive, but this time using the `*.ditamap` value rather than `*.dita`.

## Create an Eclipse project to work with DITA

1. Click the File menu, and select the New option, then the Project option.
2. Expand the General twisty.
3. Select Project, then click `Next>`.
4. Enter a project name, for example `MySecurityGuidanceProject`, then click Finish.

## Add an existing Git repository (your local copy) into a project

1. Click the File menu, and select the Import option.
2. Expand the General twisty.
3. Select the File System option, and click `Next>`.
4. Click the Browse button next to the 'From directory:' field, and navigate to the directory on your system containing your local copy of the Git repository.
5. Click the Open button.
6. Select the checkbox next to the name of the directory containing your local copy of the Git repository, for example `security-guidance`.
7. Click Finish.
8. When asked if you want to overwrite the `.project` file, click Yes.
9. In the Project Explorer window, expand the `MySecurityGuidanceProject` twisty.
10. Expand the `dita` directory.
11. Check that all the dita files have little icons with 'X' characters. This shows that the files are recognised as holding XML (DITA) content.
12. Double click on any dita file, to open it.
13. By default, the XML editor opens an XML file in 'design' mode, which shows the logical structure. Click the Source tab to show the actual XML file.
14. If everything has worked correctly, the dita file is opened with colour highlighting showing that the XML is understood and valid (thanks to the XML Catalog information provided earlier).

## Running a local DITA build

1. Open a terminal.
2. Ensure you have enabled your DITA build environment by running the `startcmd.sh` script as described in [Test the DITA installation](#test-the-dita-installation) above.
3. To check the environment is correct, run the command:</br>`which dita`</br>If the command is not found, your environment is not set correctly.
4. Change to the directory containing the DITA repository (for example `security-guidance`).
5. Change to the `buildUtils` directory.
6. Run the command:</br>`ant -lib $DITA_DIR/config -f builder.ant clean`
7. You should see a `BUILD SUCCESSFUL` message. This confirms that the basic build environment is correct.
8. To run an actual build of the DITA content, run the command:</br>`ant -lib $DITA_DIR/config -f builder.ant dist`
9. A large number of messages should appear, reporting on the build progress.
10. After a short time (~35 seconds?), a `BUILD SUCCESSFUL` message should appear.
11. Check in the `security-guidance/docs` directory; you should see a full set of markdown files and also a `moj-guidance.pdf` file.

## (Optional) Enable Word format output from a build

1. Open a terminal.
2. Ensure you have enabled your DITA build environment by running the `startcmd.sh` script as described in [Test the DITA installation](#test-the-dita-installation) above.
3. To check the environment is correct, run the command:</br>`which dita`</br>If the command is not found, your environment is not set correctly.
4. To install the Word format capability, run the command:<br/>`dita install com.elovirta.ooxml`<br/>This enables building an additional output format: `docx`, providing a basic compatibility with the word processing tool.
5. An additional Ant build target is also included. To build a Word format document from the DITA source, run the command:<br/>`ant -lib $DITA_DIR/config -f builder.ant compile_word`<br/>The resulting file is put into the `dita/out` directory.