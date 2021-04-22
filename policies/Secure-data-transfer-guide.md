---
Review: 2021-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Secure Data Transfer Guide

## Introduction

This guide outlines the security procedures and advice for Ministry of Justice (MoJ) staff wanting to send or receive data securely from external sources.  

This is incredibly important to the MoJ as personal and sensitive data is regularly being transmitted between departments.  Laws like GDPR and industry standards, such as PCI DSS, dictate the MoJ’s responsibility to secure this data.  It is also important to recognise the damage leaked sensitive data could cause to the vulnerable people the MoJ endeavours to protect.

Any technique used must encrypt the data over the network (in transit) and in storage (at rest) and require strong authentication to ensure both the sender and recipient are who they claim to be.

## Who is this for?

This policy is aimed at three audiences:

1. **Technical users**: these are in-house MoJ Digital and Technology staff who are responsible for implementing controls throughout technical design, development, system integration and operation. This includes DevOps, Software Developers, Technical Architects and Service Owners. It also includes Incident Managers from the Event, Problem, Incident, CSI and Knowledge (EPICK) Team.
2. **Service Providers**: defined as any other MoJ business group, agency, contractor, IT supplier and partner who in any way designs, develops or supplies services (including processing, transmitting and storing data) for, or on behalf of the MoJ.
3. **General users**: all other staff working for the MoJ.

'All MoJ users' refers to General users, Technical users and Service Providers as defined above.

## Related guides



## Transfer Considerations

Anyone handling personal or sensitive data must seek consent from their line manager to authorise data transfer.

Data (sensitive or not) should only be transferred where it is strictly necessary for the effective running of the MoJ and the care of the people it serves. Accordingly, before any data transfers are requested, the necessity of the transfer should be considered in advance.

When dealing with third parties consider whether any data sharing agreements or contracts are in place that cover the transfer of that data. Check whether there are any stipulations in place regarding the method of transfer that should be used.

Check that you are not providing more information than is necessary for the identified purpose. For example, do not just send a whole document or spreadsheet when only one section or specific columns are required.

For all transfers of information containing personal or sensitive data, it is essential that you appropriately establish the identity and authorisation of the recipient.

## Data Transfer Methods

Before choosing the method of transfer you must consider the following:

- The nature of the information, its sensitivity, confidentiality or possible value
- The size of the data being transferred
- The damage or distress that may be caused to individuals as a result of any loss during
transfer
- The implications any loss would have for the MoJ
- You must only send information that is necessary for the stated purpose, and any data not required should be redacted or removed completely (as appropriate) before transfer.

##Data Transfer by Email

- Email communication should not be used to transfer unencrypted sensitive data which could contain personal information. Employees should be mindful that emails are not designed to
attach and transfer large amounts of data. The MoJ’s email system does not support file
attachments that exceeds the total of ??MB.
- Staff should consider an alternative secure method of transferring sensitive data wherever
possible and practicable. If no suitable alternative is available then apply an extra level of
security. This can be achieved by the use of encryption, applying a password to the sensitive
data you wish to send. All passwords must be transferred using an alternative method of
communication to the recipient (this includes post, telephone call to an agreed number, or
by SMS text message).
- Email messages must contain clear instructions of the recipient’s responsibilities and
instructions on what to do if they are not the correct recipient.
- Information sent must, where practical, be enclosed in an encrypted attachment.
- Care must be taken as to what information is placed in the subject line of the email or in the
accompanying message. Filename or subject line must not reveal the full contents of attachments or disclose any sensitive personal data.
- Emails must be sent from your work email address, as provided by the MoJ, to ensure the
correct privacy and security information is displayed.

## Data Transfer via ??


## Removable storage devices (eg memory sticks, usb drives)

The MoJ strongly discourages the use of removable storage devices for data transfer.

Any data being transferred by removable media (e.g. USB memory stick) must be encrypted.
Encrypted portable storage devices must be password protected with a strong password. If the
password itself must be conveyed to a third party, it must be transferred using an alternative
method of communication to the recipient (this includes post, telephone call to an agreed number,
or by SMS text message).

For users who are required to copy or move data to removable media and the quantity of data to be
transferred is too large then assistance should be sought from the MoJ’s Operational Security Team.
Ownership of the removable media used must be established. The removable media must be
returned to the owner on completion of the transfer and the transferred data must be securely
erased from the storage device after use.

Clear instructions of the recipient’s responsibilities and instructions on what to do if they are not the intended recipient must be given.

Any accompanying message or filename must not reveal the contents of the encrypted file.  The sender must check, at an appropriate time, that the transfer has been successful and obtain a receipt. An email confirming receipt is acceptable.

Report any issues to your line manager and in the case of missing or corrupt data to the Chief Privacy
Officer or Data Protection Officer immediately.


## Contact details

- Contact the Technology Service Desk to report a suspected IT incident: Telephone: 0800 917 5148.
- Contact the MoJ Security Team for further advice and to report other security incidents: [Security@justice.gov.uk](mailto:Security@justice.gov.uk)
