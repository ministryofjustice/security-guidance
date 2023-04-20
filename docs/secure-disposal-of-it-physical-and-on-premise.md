# Secure disposal of IT - physical and on-premise

This document is the Ministry of Justice \(MoJ\) guidance covering disposal of physical and on-premise media and data. It is intended to ensure that the confidentiality and integrity of MoJ data is maintained when physical hardware is decommissioned.

**Parent topic:** [Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)

**Related information**  


[Secure disposal of IT equipment](secure-disposal-of-it-equipment.md)

[Secure disposal of IT - physical and on-premise](secure-disposal-of-it-physical-and-on-premise.md)

[Secure disposal of IT - public and private cloud](secure-disposal-of-it-public-and-private-cloud.md)

[Technical Controls Policy](technical-controls-policy.md)

## Physical Media and Associated Data

The MoJ and its Executive Agencies and Arms Length Bodies use a wide variety of equipment, including photocopiers and printers, data centre hard and tape drives, desktop computers, laptops, USB memory sticks, and generic mobile devices. Some equipment might be the responsibility of a supplier to decommission and dispose of it safely and securely. Check asset tags or similar identifiers to determine and validate responsibility.

However, other devices across the MoJ estate might have been procured and managed locally. They **shall** be disposed of securely, to prevent MoJ information from being “leaked”.

## Approved organisations

For help to arrange secure disposal by an approved organisation, contact IT Service Desk \(0800 917 5148\).

## NCSC and CPNI on Secure Disposal

The National Cyber Security Centre \(NCSC\) and Centre for the Protection of National Infrastructure \(CPNI\) give critical guidance on the secure sanitisation of storage media [here](https://www.ncsc.gov.uk/guidance/secure-sanitisation-storage-media) and [here](https://www.cpni.gov.uk/secure-destruction-0), respectively, specifically regarding disposal and destruction of media, and the data contained within it.

The situations when sanitising data is required are:

-   Re-use.
-   Repair.
-   Disposal; sanitising unwanted media and its associated data whilst it is controlled by the MoJ and before it is passed outside the MoJ.
-   Destruction; destroying the media, and hence data it contains, onsite or offsite.

## Determining data deletion and destruction methods

To determine the data disposal and the media's destruction method, based on the type of equipment and its security classification, use the following table.

The table contains two columns, called “Data deletion method” and “Destruction method”, which are defined as:

<a name="data-deletion-method"></a>

-   **Data deletion method**

    Covers assets if they remain within the MoJ, and have not reached end of life. For example, the device can be re-used or reallocated to a different user, or repurposed for a different function.

<a name="destruction-method"></a>

-   **Destruction method**

    Covers assets that have reached end of life, and need to be physically destroyed onsite or offsite.


**Note:** If the data is encrypted, then only the key needs to be deleted or erased, and the table does not need to be followed.

If the table does not cover your exact requirement, contact IT Service Desk \(0800 917 5148\).

**Note:** When disposing of **Secret** or **Top Secret** equipment or materials, always contact IT Service Desk \(0800 917 5148\).

|Equipment or asset type|Data deletion method|Destruction method|
|-----------------------|--------------------|------------------|
|Flash \(USB\)|Delete the data, or erase using manufacturer instructions.|Destroy using commercially available disintegration equipment, to produce particles of a maximum of 6 mm in any direction.|
|Hard disk drive. **Note:** This includes data centre disk drives.|Overwrite the entire storage space with random or garbage data, verifying that only the data used to perform the overwrite can be read back.|Break the platters into at least four pieces. This can be carried out either manually or by using a commercially available destruction product suitable for use with hard disks. Alternatively, apply a lower level degauss \(refer to the explanation after this table\), and then apply a destructive procedure that prevents the disk from turning. For example, punch holes into the platters, or twist or bend them.|
|Magnetic tapes and floppy disks **Note:** This includes data centre tape drives.|Overwrite the entire storage space with random or garbage data, verifying that only the data used to perform the overwrite can be read back.|Destroy using a commercially available shredder that meets a recognised international destruction standard. Particles of tape should be no larger than 6 x 15 mm. Alternatively, apply a lower level degauss and then cut the tape to no larger than 20 mm in any direction.|
|Optical media|Data deletion is not possible. Refer also to the note about RW-capable media after this table.|Shred or disintegrate using equipment that meets a recognised international destruction standard. Particles should be no larger than 6 mm in any direction.|
|Monitors|Overwrite on-board storage by displaying non-sensitive data on the screen for a few minutes before powering off. **Note:** If a monitor screen has legible “burn-in” of sensitive information it **shall not** be re-sold or donated.|Monitors can be disposed of by: \(1\) Returning the product to the manufacturer who **shall** align to [formal waste disposal responsibilities](https://www.gov.uk/electricalwaste-producer-supplier-responsibilities), or \(2\) taking the item to a professional waste disposal facility, or \(3\) reselling or donating to a non-profit organisation, once basic sanitation procedures have been performed. Ensure there is no “burn-in” of sensitive information, and that the device has not reached its end of life. **Note:** If the end of life monitor contains mercury, it is considered hazardous waste and its disposal **shall** align to [WEEE 2013 Regulations](https://www.hse.gov.uk/waste/waste-electrical.htm) using specialist methods such as disassembly to remove the mercury containing backlights for specialist treatment and the separation of the remaining material streams.|

**Note:** A lower level degauss is a process using specialised equipment to erase data totally, by eliminating the unwanted magnetic field \(information\) stored on tape and disk media.

**Note:** Theoretically, data deletion is possible on some RW-capable media. For simplicity, however, the safer assumption is that rewriting and therefore data deletion is not possible on optical media.

Owners of the data storage devices are responsible for procuring services that meet the necessary destruction outcomes as described previously.

Wherever possible and appropriate, managers should pool together equipment with that of local colleagues to share service costs.

## Data destruction verification

As part of the physical media or data destruction by the MoJ or its suppliers, validation of destruction **shall** be carried out. This is to ensure that data handling processes align with the MoJ Asset Management Lifecycle policies. This includes:

1.  The MoJ or supplier scans the hard drive or physical media asset tags or barcodes.
2.  The MoJ or supplier carries out data destruction \(as per the previous table\).
3.  The MoJ or supplier confirms hard drive or physical media data destruction by providing reasonable proof. This can include:
    1.  Providing an inventory of physical media in their possession.
    2.  Reconciliation carried out on the physical media scanned/received matching the physical media destroyed.
    3.  A witness in attendance to sign a destruction certificate that is be stored in a secure space or network share.

**Note:** An alternative to the previous steps is to use a leading enterprise erasure tool that provides a certificate aligned to [NIST 800-88 Guidelines for Media Sanitization](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf). Such a tool verifies:

1.  When the physical media was destroyed.
2.  That verification was performed.

If you are based in a London HQ site the Accommodation Team coordinates bulk secure disposal; please contact them in the first instance.

**Note:** All destruction certificates and destroyed assets **shall** be supplied to the MoJ hardware team to update CMDB. This can be done using the technical portal to “Bulk upload CIs - update”, or alternatively by emailing the details to: [MoJITAssetManagementTeam@justice.gov.uk](mailto:MoJITAssetManagementTeam@justice.gov.uk).

## Transporting data between sites securely

If you have any concerns about moving items between sites securely, contact IT Service Desk \(0800 917 5148\).

Guidance on the transportation of secure data is located in the CPNI guidance: “[10. Transport of sensitive items](https://www.cpni.gov.uk/system/files/documents/c5/e1/2017_01_20_CPNI_Secure_Destruction_Standard.pdf)”.

The previous guidance is also referenced in the CAS Sanitisation Service Requirement, under section “[MIT001 – Keep items secure during transportation](https://www.ncsc.gov.uk/files/CAS-Sanitisation_Service_Requirement_2-1.pdf)” on page 9.

## Contact details

For any further questions or advice, contact IT Service Desk \(0800 917 5148\).

## Feedback

> If you have any questions or comments about this guidance, such as suggestions for improvements, please contact: [itpolicycontent@digital.justice.gov.uk](mailto:itpolicycontent@digital.justice.gov.uk).

