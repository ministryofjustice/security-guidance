---
Review: 2020-12-31
Owner: CISO
Target audience:
---

[Home > Cyber and Technical Security](home-security-policies-guides.md)

# Managing User Access Guide

## Introduction

This guide provides information on the authentication methods which should be used to manage user access to systems and information in the MoJ. This is a sub-page to the [Access Control Guide](access-control-guide.md).

## Managing access to MoJ systems

The following methods can be used to manage access to the MoJ’s systems. They are in order of preference for their use, with 1 providing more secure management features than 4.

<table>
<tr>
<th></th>
<th>Method</th>
<th>Comment</th>
</tr>
<tr><td>1</td><td>Application Program Interface (API)</td><td>Where possible, APIs should be used instead of remote server configuration tools such as Secure Shell (SSH) and Remote Desktop  (RDP). This is because APIs offer greater technical control over security systems without the need for parsing commands required by remote server configuration tools.</td></tr>
<tr><td>2</td><td>Automated diagnostic data collection</td><td> It should be considered the exception for administrators to directly administer a server/node when there is automated diagnostic data collection. Diagnostic data collection allows the underlying technical data to be easily correlated and analysed.</td></tr>
<tr><td>3</td><td>Remote server configuration tools</td><td>If you cannot use APIs then remote server configuration tools can be used with the following controls.</td></tr>
<tr><td></td><td></td>
<td>Use of bastion or ‘jump’ boxes for access into systems is a useful technical security design that also helps ‘choke’ and control sessions.</td></tr>
<tr><td></td><td></td>
<td>The need to use remote server configuration tools to interact with a server/node can be reduced through improved infrastructure and server design. For instance, the use of stateless cluster expansion/contraction and the automated diagnostic data capture can reduce the need to use SSH.</td></tr>
<tr><td></td><td></td>
<td>System Admins should only login to a server/node via SSH and execute commands with elevated privileges (typically, root) under exceptional circumstances.</td></tr>
<ul><li>SSH must be strictly controlled and environments should be segregated so that no single bastion or ‘jump’ SSH server can access both production and non-production accounts.</li>
<li>Do not allow direct logging in as root through SSH, administrators must have a separate account that they regularly use and simply sudo to root when necessary.</li>
<li>SSHs must be limited to users who need shell (by comparison to users who will use SSH as a port forwarding tunnel).</li>
<li>Joiners/Movers/Leavers processes must be strictly enforced (optimally and preferably automated) on SSH servers as they are a critical and privileged access method.</li>
<li>SSH should not be password-based, and should use individually created and purposed SSH key pairs. Private keys must not be shared or re-used.</li></ul>
</table>

The Government Digital Service (GDS) recommends the use of the open authorisation standard ‘OAuth2’ as a means to authenticate users. See the GDS guide for more information.

Contact details

Contact the Cyber Assistance Team for advice – [CyberConsultancy@digital.justice.gov.uk](mailto:CyberConsultancy@digital.justice.gov.uk)
