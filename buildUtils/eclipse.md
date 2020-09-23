# Setting up an Eclipse development and build environment

## Install Eclipse

1. Download the installer for the Eclipse IDE environment from [https://eclipse.org/downloads](https://eclipse.org/downloads). At the time of writing, the current version of Eclipse is 2020-06.
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
2. Expand the Git twisty.
3. Select the Project from Git option, and click `Next>`.
4. Click `Existing local repository`, and click `Next>`.
5. Click the `Add` button.
6. Navigate to the directory on your system containing your local copy of the Git repository.
7. Click the checkbox under the search results, next to the dirctory containing your repository.
8. Click `Finish`.
9. In the `Select Git Repository` window, select your newly added respository, then click `Next>`.
10. Under `Wizard for project import`, select `Import as general project`, then click `Next>`.
11. Enter a project name, then click `Finish>`.
12. In the Project Explorer window, expand the `MySecurityGuidanceProject` twisty.
13. Expand the `dita` directory.
14. Check that all the dita files have little icons with 'X' characters. This shows that the files are recognised as holding XML (DITA) content.
15. Double click on any dita file, to open it.
16. By default, the XML editor opens an XML file in 'design' mode, which shows the logical structure. Click the Source tab to show the actual XML file.
17. If everything has worked correctly, the dita file is opened with colour highlighting showing that the XML is understood and valid (thanks to the XML Catalog information provided earlier).
