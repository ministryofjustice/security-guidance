---
Review: 2021-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Secure Data Transfer Guide

## Introduction

This guide outlines the security procedures and advice for Ministry of Justice (MoJ) staff wanting to send or receive data securely from external sources.  

This is incredibly important to the MoJ as personal and sensitive data is regularly being transmitted between departments.  Laws like GDPR and industry standards, such as PCI DSS, dictate the MoJ’s responsibility to secure this data.  It is also important to recognise the damage that leaked sensitive data could cause to the vulnerable people the MoJ endeavours to protect.

## Who is this for?

This policy is aimed at three audiences:

1. **Technical users**: these are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. **Service Providers**: defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.
3. **General users**: all other staff working for the MoJ.

'All MoJ users' refers to General users, Technical users and Service Providers as defined above.

## Related guides

Need to insert link to Tee's file sharing document (MOJ Secure File Transfer Procedure v2.6.docx)<FIXME>
Need link to relevant policy document <FIXME>

## Transfer Considerations

Anyone handling personal or sensitive data must seek consent from their line manager to authorise data transfer.

Before any data transfers are requested, consider the following:

- Is it strictly necessary for the effective running of the MoJ and the care of the people it serves that the data (sensitive or not) is transferred  
- The nature of the information, its sensitivity, confidentiality or possible value
- The size of the data being transferred
- The damage or distress that may be caused to individuals as a result of any loss during transfer
- The implications any loss would have for the MoJ
- Precisely what information is necessary for the identified purpose? For example, do not just send a whole document or spreadsheet when only one section or specific columns are required
- For all transfers of information containing personal or sensitive data, it is essential that you appropriately establish the identity and authorisation of the recipient.

Any technique used must:

- encrypt the data over the network (in transit) using the appropriate encryption (TLS 1.2 or greater)
- require strong authentication to ensure both the sender and recipient are who they claim to be.

This especially applies when transmitting any data over a wireless communication network (eg Wi-Fi), or when the data will pass through an untrusted network.

If the MoJ is the controller of the data being transferred, the security storage requirements at the destination must be considered to ensure it adheres to the relevant regulation, such as PCI DSS or GDPR.

When dealing with third parties consider whether any data sharing agreements or contracts are in place that cover the transfer of that data. Check whether there are any stipulations in place regarding the method of transfer that should be used.

If personal data is being transferred to a third party then the privacy team must be informed to see if a Data Protection Impact Assessment is required.

## Data Transfer

Ideally, files should not be transferred by being sent by email but over secure links such as https, ssh or sftp.  For large files, those over 5MB, this becomes a practical necessity as many recipients will not accept emails with attachments greater than 5MB but this figure is variable.

### Data Transfer by Secure link

The MoJ's preferred method of data sharing is to use Microsoft Teams via Sharepoint.  Teams has been authorised to hold OFFICIAL-SENSITIVE information and will be developed to provide greater granular protection through the deployment of Azure Information Protection (AIP).  Where possible, data should be transferred using Teams.

Due to the diverse nature of the MoJ's architecture this may not always be possible and those in Digital and Technology who do not have access to Teams may use GSuite to transfer data.

The actual process to be used can be found (provide link to Tee Patel's document - FIXME)

### Data Transfer by Email

Where it is not possible to use Teams or GSuite and the data to be transferred is less than 20MB, email can be used but the following requirements must be followed:

- Email communication should not be used to transfer unencrypted sensitive or personal data. Employees should be mindful that emails are not designed to attach and transfer large amounts of data. The MoJ’s email system does not support file attachments that exceeds the total of 20MB.
- Staff should consider an alternative secure method of transferring sensitive data wherever possible and practicable. If no suitable alternative is available then apply an extra level of security. This can be achieved by the use of encryption, applying a password to the sensitive data you wish to send. All passwords must be transferred using an alternative method of communication to the recipient (this includes post, telephone call to an agreed number, or by SMS text message).
- Email messages must contain clear instructions of the recipient’s responsibilities and instructions on what to do if they are not the correct recipient.
- Information sent must, where practical, be enclosed in an encrypted attachment.
- Care must be taken as to what information is placed in the subject line of the email or in the accompanying message. Filename or subject line must not reveal the full contents of attachments or disclose any sensitive personal data.
- Emails must be sent from your work email address, as provided by the MoJ, to ensure the correct privacy and security information is displayed.

### CJSM Email

- CJSM (Criminal Justice Secure eMail Service) is provided for criminal justice agencies and practitioners to communicate with each other.
- As a general rule it must only be used for purposes relating to the criminal justice service.

### Microsoft 365 Encrypted email

- This facility has been applied to all standard individual and generic MoJ email accounts
- This method can be used to send/receive files classified as Official from external partners, agencies and individuals which cannot be contacted via CJSM email
- The attached files on a single email must not exceed 25MB.

## Removable storage devices (eg usb drives)

The MoJ strongly discourages the use of removable storage devices for data transfer.  However, if all other options are not possible then removable storage devices may be used with caution.

Any data being transferred by removable media (e.g. USB memory stick) must be encrypted.  Encrypted portable storage devices must be password protected with a strong password (see password-managment-guide <FIXME>). If the password itself is to be conveyed to a third party, it must be transferred using an alternative method of communication to the recipient (this includes post, telephone call to an agreed number, or by SMS text message).

For users who are required to copy or move data using removable media, it is recommended that assistance should be sought from the MoJ’s Operational Security Team.

Ownership of the removable media used must be established. The removable media must be returned to the owner on completion of the transfer and the transferred data must be securely erased from the storage device after use.

Clear instructions of the recipient’s responsibilities and instructions on what to do if they are not the intended recipient must accompany the removable media.

Any accompanying message or filename must not reveal the contents of the encrypted file.  The sender must check, at an appropriate time, that the transfer has been successful and obtain a receipt. An email confirming receipt is acceptable.

Report any issues to your line manager and in the case of missing or corrupt data to Operational Security Team immediately.

## Data transfers by post/courier

Data transfers which occur via physical media such as memory cards or USB drives must only be dispatched via secure post. The use of first or second class Royal Mail is not permitted; only Special Delivery or Recorded Delivery should be used. For non-Royal Mail services, a secure courier service must be used with a signature obtained upon delivery. The recipient should be clearly stated on the parcel and the physical media must be securely packaged so that it is not damaged in transit.

The recipient should be advised in advance that the data is being sent so that they are aware when to expect the data. The recipient must confirm safe receipt as soon as the data arrives. The sender responsible for sending the data is responsible for confirming the data has arrived safely.

## Hand Delivery and Collection

Hand delivery or collection of data may be used where removable media is required. When arranging for an individual to collect information, it should be established that they are who they say they are and seek an appropriate form of identification before handing over any documentation.

## Telephone/Mobile Phone

As phone calls may be monitored, overheard or intercepted either deliberately or accidentally, care must be taken as follows.  

- Transferred information must be kept to a minimum.
- Personal or Confidential information must not be transferred over the telephone unless the identity and authorisation of the receiver has been appropriately confirmed.

## Residual risks with encrypted data transfer

Data controllers should recognise that even if a system uses encrypted data transfer there are still occasions where data can be subject to unauthorised access. It is important to be aware of these residual risks and to include this in employee awareness training. Examples include:

- certain data relating to the communication may still be exposed (eg metadata) in an unencrypted form
- implementations relying on public-key infrastructure must implement strict certificate checking to maintain trust in end-points.

## Contact details

- Contact the Technology Service Desk to report a suspected IT incident: Telephone: 0800 917 5148.
- Contact the MoJ Security Team for further advice and to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
- Contact the Privacy Team for information on Data Protection Impact Assessments: [privacy@justice.gov.uk](mailto:privacy@justice.gov.uk)
