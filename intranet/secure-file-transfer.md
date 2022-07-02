#Secure file transfer

##Introduction

This procedure document assists users who need to share [**Official-Sensitive**](https://security-guidance.service.justice.gov.uk/data-handling-and-information-sharing-guide/#electronic-data-transfer-and-storage) information through a secure encrypted method to partners or external users outside the Ministry of Justice (MoJ).

There are several methods [available](https://security-guidance.service.justice.gov.uk/general-user-video-and-messaging-apps-guidance/#tools-for-sharing-information-internally-and-externally) for sending files if the preferred Criminal Justice Secure Exchange (CJSE) method is not possible.

**Note:** Regardless of whether the **Official-Sensitive** information is shared with or received from an external party, [out of band checks](https://security-guidance.service.justice.gov.uk/glossary/#out-of-band-checks) **should** be carried out to confirm the legitimacy of the communications and requests.

**Note:** You **shall** comply with MoJ [security policies](https://security-guidance.service.justice.gov.uk/cyber-and-technical-security-guidance/), and refer to guidance on MoJ approved [applications](https://security-guidance.service.justice.gov.uk/general-user-video-and-messaging-apps-guidance/).

##Methods of sharing documents

|Domain|Applications|File size|Internal or external|Examples|
|------|------------|---------|--------------------|--------|
|`*.*@justice.gov.uk`|SharePoint, MS Teams, or OneDrive|Over 25MB|External, including third-party suppliers, legal teams, or other government departments outside of the MoJ.|Multiple files more than 25MB each.|
|`*.*@justice.gov.uk`|Outlook encrypted email|Under 25MB|Internal and external.|Sending a few documents less than 25MB each.|
|`*.*@digital.justice.gov.uk`|Google Workspace|Under 25MB|Internal and external.|Sending a few documents less than 25MB each.|
|`*.*@digital.justice.gov.uk`|Google Drive (part of Google Workspace)|Over 25MB|External, including third-party suppliers, legal teams, or other government departments outside of the MoJ.|Multiple files more than 25MB each|

**Note:** The term Google Workspace rather than Google "GSuite" is used now, with Google Drive (Drive) included as part of the Google Workspace integrated tools.

**Note:** For further information on the controls in place when sharing sensitive information, refer to the [information sharing](https://security-guidance.service.justice.gov.uk/data-handling-and-information-sharing-guide/#information-sharing) section of the Data Handling and Information Sharing Guide.

##Objectives of this procedure

* To provide step-by-step instructions on how to transfer files externally.
* Follow policies and procedures to ensure MoJ information and services are protected.
* To share information with interested parties on a need-to-know basis only.

##Alternative methods and processes

* **Criminal Justice Secure Mail (CJSM)**

    CJSM is the approved secure email solution.

* **Data Movement Form (DMF)**

    A [DMF](https://security-guidance.service.justice.gov.uk/data-handling-and-information-sharing-guide/#data-movement-form-dmf) is required for all bulk file transfers. All requests **shall** be reviewed and approved by the MoJ [Justice Digital Security Operations Centre (SOC)](mailto:security@justice.gov.uk).


**Note:** You **shall not** use personal accounts for work purposes. This includes using personal systems such as Gmail, Hotmail, or Yahoo mail to send or receive emails for work purposes. You **shall** use your officially-issued `*.*@justice.gov.uk` or `*.*@digital.justice.gov.uk` email address for MoJ business.

##Receiving password protected files

It is acceptable to receive password protected files from external parties or from the public. However, you **shall** carry out the following checks:

* Confirm that the file was received from a known and reputable source or sender. Do this by performing an [out of band check](https://security-guidance.service.justice.gov.uk/glossary/#out-of-band-checks).
* The password needed to access the file **shall** be shared separately from the file, and **shall not** be provided using the same method as was used to send the file. In other words, if the password protected file is received by email, the password **shall** be received through another method, not by email.
* The contents of a password protected file cannot always be scanned during entry into MoJ systems. In such cases, the password protected file **shall** go through an isolated local folder or computer disconnected from the network, where it is decrypted and then scanned before progressing further or being uploaded into MoJ systems.

##Sharing files using Microsoft OneDrive or SharePoint

**Note:** A tutorial on Microsoft OneDrive is [available](https://support.microsoft.com/en-us/office/share-onedrive-files-and-folders-9fcc2f7d-de0c-4cec-93b0-a82024800c07). A tutorial on Microsoft SharePoint is also [available](https://support.microsoft.com/en-us/office/share-sharepoint-files-or-folders-1fe37332-0f9a-4719-970e-d2578da4941c).

1.  Go to [https://justiceuk-my.sharepoint.com/](https://justiceuk-my.sharepoint.com/).
2.  Log in with your MoJ `*.*@justice.gov.uk` email account.
3.  Click on the menu dots and select OneDrive.

    ![The image shows a list of Microsoft applications. The 3 by 3 menu grid is highighted. The OneDrive icon and application name is also highlighted.](images/sft001.png)

4.  Next, create a new folder. To do this, click on the **New** drop-down arrow, and select the option to create a new folder.

    ![The image shows the file and folder management view. The option to create a new object is highighted, and the new folder item is selected.](images/sft002.png)

5.  Give the new folder a unique name.

    ![The image shows the Document management view. The field to enter the new folder name is highlighted. The new folder is about to be given a unique name.](images/sft003.png)

6.  Upload the file to the newly named folder.

    ![The image shows the file and folder upload view. The new folder has been selected. The upload option has been chosen, and the new file is about to be uploaded.](images/sft004.png)

7.  Next, share the file. To do this, click on the **Share** option in the menu. Then in the **Send link** box, click on **People in Ministry of Justice with the link can edit**, which takes you to the **Link settings** box.

    ![The image shows the Share view. The Link Settings menu is presented. The choice is made to allow Specific People to work with the link. In the Other Settings options, Allow editing is selected. The option to Block downloads is enabled - this prevents anyone from downloading the information.](images/sft005.png)

8.  Select the option for **Specific people**, ensure **Allow editing** is unticked, and the **Block download** option is activated. Finally, click on **Apply**. This returns you to the **Send link** box.

    ![The image shows the send file view. The method used to send a link has been highlighted. The option to allow People in Ministry of Justice with the link to edit is selected.](images/sft006.png)

9.  Next, add all the email accounts that should be able to **view** the file. Click the **Send** button.

    ![The image shows the Send link view. The field to add email addresses is selected. Email addresses are being added. The Send button is highighted.](images/sft007.png)

10. When you click the **Send** button, an email is sent from your`*.*@justice.gov.uk` email account to the selected recipients. The email contains a link to the document.

##Recipient receives an email with a link to the file

1.  Each recipient receives a link to the file within the email. They initiate access by clicking on the **Open** button.

    ![The image shows the email received by the recipient. The email tells them that a file is being shared with them. In addition to the name of the file, there is an 'Open' button for the recipient to access the file.](images/sft008.png)

2.  The recipient also receives a separate email to the same registered email address. This secondary email enables access to the file by providing a PIN Code to open the file.

    ![The image shows the PIN email received by the recipient. The email includes an 'Account Verification Code', which is a multi-digit number.](images/sft009.png)

3.  When the recipient clicks the **Open** button in the 'file share' email, they are asked to provide the account verification code before they can access the file content.

##Sharing Files Using Microsoft Teams

**Note:** A tutorial on Microsoft Teams is [available](https://support.microsoft.com/en-us/office/microsoft-teams-video-training-4f108e54-240b-4351-8084-b1089f0d21d7).

1.  Open MS Teams. Click on the Teams icon within the Left Panel. Click on the icon at the bottom of the app called **Join or Create a Team**.

    ![The image shows the Teams membership panel. The option to join or create a team is selected.](images/sft010.png)

2.  Select the **Create a team** applet, and then click the **Create team** button.

    ![The image shows the 'Create a Team' panel. The panel has a button called 'Create team'.](images/sft011.png)

3.  Select the tab called **From scratch**.

    **Note:** From SharePoint, OneDrive or in a Teams **File** tab right-click, and share.

    ![The image shows the 'Create a Team' panel with several tab options. The tab called 'From scratch' is highlighted.](images/sft012.png)

4.  In the window called **What kind of team will this be?**, select the **Private** option.

    ![The image shows the 'What type of team will this be?' panel with several tab options. The tab called 'Private' is highlighted.](images/sft013.png)

5.  You are invited to provide some quick details about the private team. Enter a team name for the **Give your team a name** field. Since the team is not going to be used for a lot of activity, a simple option is to provide a name that includes the current date and time, to make the name unique. For example, you might use a temporary name such as `ProjectAmberFile2022June08`.

    ![The image shows the panel to provide quick details about the private team. The details include two fields: the team name, and its description.](images/sft014.png)

6.  You can either add members to your new team now, or skip the step and do it later.

    ![The image shows the panel to add members to the team. There is a single field, where you can enter a name, a distribution list, or an email enabled security group. When a value is entered into the field, an 'Add' button is enabled.](images/sft015.png)

    **Note:** The team is now available within the left panel. It has a **General** tab by default. Within the right panel, you can either start a conversation in the **General** tab, or click on the **Files** tab on the right to upload content for sharing by the team.

7.  You can add external recipients as members of the team by adding their email addresses using the 'triple dot' menu.

    ![The image shows part of the list of teams. Next to the team name is a 'triple dot' menu. The team name and the menu are highlighted.](images/sft016.png)

8.  A Welcome Message is displayed to confirm the team has been created.

    ![The image shows the 'Welcome to the team' message.](images/sft017.png)

9.  To add members to the team at any time, click the triple dot menu on the channel name and select **Add members**.

    **Note:** External team members - anyone who does not have an MoJ email account - is added to the team as a 'guest'.

    ![The image shows part of the list of teams with the 'triple dot' menu. The menu has been selected, and a sub-menu presented. The sub-menu options include 'Add member', which is highlighted.](images/sft018.png)

    ![The image shows the panel to add a member to the team or channel.](images/sft019.png)

10. You can add members to the team, including external users. Use the **Manage Team** option to review user access, modify permissions, and add files to the team 'file share'.

When a recipient is added to a shared folder, they receive an email inviting them to **Join a Teams Folder**. They should use their email address to log in and access the shared information. The email address is the same one used to receive the invitation.

##Sharing files using Microsoft Outlook

1.  If you are using a Mac client laptop, once you have completed the content of your Outlook email, from the email menu bar, select **Options** and then click on **Encrypt**.

    ![The image shows the Outlook client application on a Mac. The 'Encrypt' option is selected.](images/sft020.png)

    If you are using a Windows client laptop, once you have completed the content of your Outlook email, from the email menu bar, select **Options** and then click on **Encrypt**.

    ![The image shows the Outlook client application on Windows. The 'Encrypt' option is selected.](images/sft021.png)

2.  When an authorised recipient receives the message, to read it they select **Options** and then click on the **Read the message** tab.

    ![The image shows the email received by the recipient. The email tells them that a protected file has been sent to them. In addition to the name of the file, there is a 'Read the message' button for the recipient to access the file.](images/sft022.png)

3.  The recipient clicks on the **Sign in with a One-time passcode** button.

    ![The image shows that the recipient has clicked the 'Read the message' button. They are asked to sign into prove they are authorised to view the email. There are two options. One is to sign in using a Yahoo! ID. The other option is highlighted, and allows the recipient to sign in using a One-time passcode.](images/sft023.png)

4.  When the recipient clicks the **Sign in with a One-time passcode** button, a passcode email is automatically sent to the recipient's email address.

    ![The image shows that the recipient has clicked the 'Sign in with a One-time passcode' button. A message tells them that a one-time passcode has been sent to their email address.](images/sft024.png)

5.  The recipient notes the passcode.

    ![The image shows that an example email containing a one-time passcode, which is highlighted.](images/sft025.png)

6.  The recipient pastes the passcode into the original email they received.

    ![The image shows a form with a field containing the newly-received one-time passcode.](images/sft026.png)

7.  The result is that the email is unlocked, and can be read by the recipient.

    ![The image shows the normal email display page, containing the email that has now been successfully accessed by the authorised recipient.](images/sft027.png)


##Sharing files using Google Workspace

Pre-requisite: Ensure you have a current and correct mobile phone telephone number for each of your recipients. This contact number is used to send them a unique PIN code to unlock shared files.

1.  When your email is ready to send, select the encrypt icon at the bottom of the toolbar. In Google Workspace email, this button is called **Toggle confidential mode**.

    ![The image shows a Google Workspace email composition page. The email has been created as normal. At the bottom of the page, a 'padlock' icon is selected.](images/sft028.png)

2.  On the Confidential mode panel, select the Radio Button for **SMS Passcode**.

    ![The image shows the Confidential mode panel. A section of the panel allows you to choose between requiring a passcode or not. The choice is made using radio buttons. In the image, the 'No SMS passcode' option is currently selected. The option to use an SMS passcode is highlighted, ready to select that option in preference.](images/sft029.png)

3.  Click the **Save** button.

    ![The image shows the Confidential mode panel. In the image, the 'SMS passcode' option is currently selected. 'Save' button is highlighted, ready to be clicked.](images/sft030.png)

4.  Add the mobile telephone numbers for each of the recipients. Click the **Send** button.

    ![The image shows the Confirm phone numbers panel. In the image, the area for entering recipient phone numbers is highlighted. There is a 'Send' button.](images/sft031.png)

5.  The result is that an email is sent to each recipient.

    ![The image shows an example of an encrypted email sent to the recipient. At the bottom of the email, there is a warning panel advising that the content has an expiry date, after which recipients will not be able to forward, copy, print, or download the email.](images/sft032.png)


##Recipient receives the encrypted email

1.  The recipient receives a notification email from Google Workspace, advising that they have been sent an email which can only be accessed by the authorised recipient. Click the **View the email** button.

    ![The image shows an example of an encrypted email notification sent to the recipient. It confirms when the email was sent, and that it can only be opened by the authorised recipient. A 'View the email' button on the page is highlighted.](images/sft033.png)

2.  To view the email, the recipient requires a passcode. To get the passcode, click the **Send Passcode** button.

    ![The image shows a panel inviting the recipient to request an access passcode. The panel confirms that the passcode will be sent to a specific phone number as an SMS code. The button to request the passcode is highlighted.](images/sft034.png)

3.  The recipient receives the passcode by SMS text message on their mobile telephone.

    ![The image shows an example SMS message received on a phone. The message states what the verification code is. In the example image, the code number is highlighted.](images/sft035.png)

4.  After clicking the **Send Passcode** button, a form appears notifying the recipient that the Passcode has been sent to the indicated phone number. The recipient enters the Passcode from the SMS message into the form, and clicks the **Submit** button.

    ![The image shows a form where the recipient can enter the Passcode from an SMS message received on their phone. The example Passcode has been entered into the 'Enter passcode' field. A 'Submit' button appears on the form for the recipient to click.](images/sft036.png)

5.  The email is unlocked and viewable by the recipient.

    ![The image shows a newly-unlocked email after the recipient successfully entered the correct Passcode.](images/sft037.png)


##Very large file using Google Workspace

**Note:** This option is only for MoJ Google Workspace users, with `*.*@digital.justice.gov.uk` accounts.

1.  Using Google Drive, locate the large file you want to share. Right click on the file.

    ![The image shows a Google Drive window. A file has been selected, and right-click used to bring up a menu. Within the menu, the 'Share' option has been highighted.](images/sft038.png)

2.  Choose the **Share** option. A form appears, where you can add the user's email address you want to share to. You can also choose what sort of link will be provided. The default is **Restricted**, which means only the specific named recipients can access the file. Leave the default unchanged.

    ![The image shows a Google Share window. The name of the file to be shared provides the title for the window. There is a field for adding more people or groups to receive the file. Underneath the field is a list of people who will have access to the file. The permissions they have when accessing the file is listed alongside their name. Underneath the list of people with access is a General access section, which allows selection of the sort of access permitted. The setting is shown as Restricted, meaning that only people granted access can open the file using the link. At the bottom of the window are two buttons. One is to copy the link to the file with the current access permissions. The other is a 'Done' button, which is used when all the desired recipients have been added.](images/sft040.png)

3.  When you add the first recipient, the window changes to a notification window, confirming which file will be sent to the recipients. You can add more recipients to the list. You can also enter an information message that will be included in the email to the recipients.

    ![The image shows an updated Google Share window. The name of the file to be shared provides the title for the window. There is a field listing each of the people or groups to receive the file. The permissions they have when accessing the file is listed alongside their name. Underneath the list of people with access is a 'Notify people' checkbox. Underneath the checkbox is a field to enter a notification message that will be sent to the recipients. At the bottom of the window are three buttons. One is to copy the link to the file with the current access permissions. The middle button is a 'Cancel' button, used to abandon the file sharing task. The third button is the 'Send' button, positioned on the right hand side. It is highlighted, indicating that the user is about to send the file share link and message to the list of recipients.](images/sft041.png)

4.  Before the large file is shared, a dialogue box appears, asking you to confirm that you want to "Share outside organisation?" Read the message and then click on the **Share anyway** button.

    ![The image shows a 'Share outside organisation' confirmation dialogue box. The name of the file to be shared is included in a warning message, advising that you are about to share the file with one or more recipients who are outside the MoJ. At the bottom of the window are two buttons. One button is a 'Cancel' button, used to abandon the file sharing task. The other button is the 'Share anyway' button, positioned on the right hand side. It is highlighted, indicating that the user is satisfied that it is correct to send the file share link and message to the list of recipients.](images/sft042.png)


##Recipient receives the shared Google Workspace file email

1.  The recipient receives an email stating that a file on Google Workspace has been shared with them. They click on the **Open** button.

    ![The image shows an email received by a recipient, advising that a named user is inviting them to access a shared file or folder. The name of the file to be shared is included in the message. Underneath the name of the shared file is a notification area, displaying an information message from the user who is sharing the file. At the bottom of the window is a highlighted Open button.](images/sft043.png)

2.  Ater clicking the **Open** button, the shared file or folder now appears in the recipients file storage area. They have access permissions that correspond to what was specified by the user sharing the file.

    ![The image shows a portion of the recipients file storage area. It now includes an entry for the shared file. Next to the file name is a small icon of two people side by side, indicating that this is a shared file.](images/sft044.png)


##Contact details

For any further questions or advice relating to security, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

---

##Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

