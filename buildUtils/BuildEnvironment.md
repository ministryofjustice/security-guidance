# Setting up a DITA development and build environment

## DITA editing

The recommended option for editing DITA files is to use Visual Studio.

However, any XML-aware editor can be used.

## Installing pre-requisites for the build environment

1. Open a terminal.
2. Run the command: `java --version`.
3. Check that the response confirms that Java is installed on your system. Check also that the Java version is at least 17.
4. If Java is not installed, or is older than version 17, address this before proceeding.
5. Run the commandL `python3 --version`.
6. Check that the response confirms that Python3 is installed on your system. Check also that the Python 3 version reported is at least `3.10.6`.
7. If Python3 is not installed, or is older than 3.10.6, address this before proceeding.

## Installing the DITA Open Toolkit

1. Open a web browser, and go to [the DITA Open Toolkit website](https://www.dita-ot.org).
2. Click the Download button, to download the latest version.
3. In a terminal, create a directory to install the DITA Open Toolkit. For example: `~/installLocal`. Change to this directory.
4. Extract the toolkit contents from the archive you just downloaded. This will extract into a directory named according to the toolkit version, for example `~/installLocal/dita-ot-4.0.1`.

### Test the DITA installation

1. Change into the Toolkit installation directory.
2. Set up the build environment by running the `startcmd.sh` script. Don't worry about the deprecation notice.
3. Within the DITA directory, change into the `docsrc/samples` directory.
4. Run the command:</br>`dita --input=sequence.ditamap --format=pdf`
5. Look into the newly created `out` folder. You should see a file `sequence.pdf`. Open this with a PDF reader, and check that there is content in there, about 'Working in the garage'.
6. If you have the content, your DITA Toolkit installation is working correctly.

### Modify the Java heap space

During a DITA build, you might get an error message similar to: `java.lang.OutOfMemoryError: Java heap space`.
If you see this message when you run the `dita` command, try increasing the size of the Java heap space.

To do this, modify the line in the DITA Open Tookit `startcmd.sh` script, changing from:<br/>`export ANT_OPTS="-Xmx512m $ANT_OPTS"`<br/>to:<br/>`export ANT_OPTS="-Xmx1024m $ANT_OPTS"`<br/>*Note:* You'll need to exit from the terminal and re-run the `startcmd.sh` script for the change to take effect.

### Modify the PDF font usage during build

By default, the DITA build attempts to reference all available PDF fonts on your system. This is not necessary.
To use just the required fonts, modify the DITA Open Toolkit PDF build configuration.

To do this, modify the `fop.xconf` file in the DITA Open Tookit `plugins/org.dita.pdf2.fop/cfg` folder.
Search for the section that attempts to auto-detect fonts:

```
<!-- auto-detect fonts -->
<auto-detect/>
```

Comment out the `auto-detect` line, for example:
```
<!-- auto-detect fonts
<auto-detect/> -->
```

## Enable EPUB format output from a build

1. Download and install the [XMLMind DITA Converter](https://www.xmlmind.com/ditac/).<br/>The tool is free, open source, and software licensed under [Mozilla Public License version 2.0](https://www.xmlmind.com/ditac/MPL-2.0.html).
    1. Ensure that you install the full converter, which comes with the Apache FOP processor. The installation package has `...plus-fop...` as part of the filename.
    2. Ensure that the `ditac` tool provided by the Converter is available in the operating system application `PATH` variable.
3. After installing, ensure that you can run the converter. Do this by opening a terminal, and running the command:<br/>`ditac --help`<br/>You should get a lengthy list of help options for running the tool. Any error message indicates that the converter was not installed correctly.

Note: Converter version 3.11.2 is known to work well for this build environment.

<!--

## Enable Microsoft Word format output from a build

1. Download and install the [pandoc](https://pandoc.org/) 'Universal Document Converter' file conversion toolkit.
   1. Check that the installation has succeeded, and that the `pandoc` command can be found. Do this by running the following command in a terminal:</br>`which pandoc`.
   2. If the command is not found, your installation is not correct.
2. During a build, Microsoft Word versions of the content are created, and placed in the `dita/worddocs` directory.
3. (Optional) To build a Microsoft Word format document from the DITA source, run the command:<br/>`ant -lib $DITA_DIR/config -f builder.ant compile_word`.
-->

## Enable Python build tooling

1. Install the PyPDF2 component. Do this by running the following command in a terminal:</br>`pip3 install --user PyPDF2`
2. Install the RSS feedgen component. Do this by running the following command in a terminal:</br>`pip3 install --user feedgen`

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

