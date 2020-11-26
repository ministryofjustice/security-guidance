# Setting up a DITA development and build environment

## DITA editing

There are (currently) two options for editing DITA files:

-   [Eclipse](eclipse.md)
-   [Atom](atom.md)

## Installing DITA (pre-requisite)

1. Open a terminal.
2. Run the command: `java --version`.
3. Check that the response confirms that Java is installed on your system.
4. If Java is not installed, address this before proceeding.

## Installing DITA

1. Open a web browser, and go to [the DITA Open Toolkit website](https://www.dita-ot.org).
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
7. If you get an error message similar to: `java.lang.OutOfMemoryError: Java heap space` when you run the `dita` command, try increasing the size of the Java heap space. To do this, modify the line in the `startcmd.sh` script, changing from:<br/>`export ANT_OPTS="-Xmx512m $ANT_OPTS"`<br/>to:<br/>`export ANT_OPTS="-Xmx1024m $ANT_OPTS"`<br/>*Note:* You'll need to exit from the terminal and re-run the `startcmd.sh` script for the change to take effect.

## Enable EPUB format output from a build

1. Download and install the [Dita4Publisher](http://www.dita4publishers.org/) plugin. Install the plugin by:
    1. Unzipping the downloaded zip file into the DITA installation `plugins` directory.
    2. From the DITA installation root directory, run the `ant -f integrator.xml` command.
    3. Check that the integration has succeeded, by looking for an `epub` value in the results of running the command: `dita transtypes`.
2. (Optional) To build an EPUB format document from the DITA source, run the command:<br/>`ant -lib $DITA_DIR/config -f builder.ant compile_epub`<br/>The resulting file is put into the `dita/out` directory.

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
