#!/bin/bash
tmpFolder="$(mktemp -d /tmp/preparePDF.XXXXXXXX)"
tmpPageBreak="$(mktemp /tmp/preparePDF.XXXXXXXX)"
printf "\\usepackage{sectsty}\\sectionfont{\\clearpage}" > $tmpPageBreak
fullset=""
while IFS= read -r line; do
	echo "Processing file: $line"
	cp --parents $line $tmpFolder
	awk 'BEGIN { lineCount=1 } { if (NR==1) { if (/^---/) next; else { print $0; lineCount=0; } } else if (lineCount==0) { print $0; } else { if (/---/) lineCount=0; next; } }' $line > "$tmpFolder/$line"

	fullset="$fullset $tmpFolder/$line "
done << LAST_LINE
index.md
policies/general-user-video-and-messaging-apps-guidance.md
policies/guidance-for-using-open-internet-tools.md
policies/personal-devices.md
policies/remote-working.md
standards/cryptography.md
standards/malware-protection-guide-introduction.md
standards/malware-protection-guidance-defensive-layer-1.md
standards/malware-protection-guidance-defensive-layer-2.md
standards/malware-protection-guidance-defensive-layer-3.md
security_decisions/principles/data-security-and-privacy.md
security_decisions/principles/identify-protect-detect-respond-recover.md
security_decisions/principles/maintained-by-default.md
security_decisions/principles/secure-by-default.md
security_decisions/principles/security-log-collection.md
security_decisions/principles/shared-responsibility-models.md
standards/accounting.md
standards/authentication.md
standards/authorisation.md
standards/baseline-aws-accounts.md
standards/data-destruction.md
standards/data-security-and-privacy.md
standards/management-access.md
standards/networks-bearers-not-trust.md
standards/password-managers.md
standards/secrets-management.md
standards/vulnerability-scanning.md
standards/cots-applications.md
standards/custom-applications.md
standards/enterprise-it-infrastructure.md
standards/enterprise-it-mobile-devices.md
standards/hosting-platforms.md
standards/log-entry-metadata.md
standards/security-log-collection-maturity-tiers.md
guides/automated-certificate-renewal.md
guides/data-security-and-privacy-lifecycle.md
guides/data-security-and-privacy-triage-standards.md
guides/defensive-domain-registration.md
guides/online-indentifiers.md
guides/personnel-security-clearances.md
guides/standards-assurance-tables.md
guides/user-guide.md
guides/mail-check.md
guides/public-sector-dns.md
guides/web-check.md
guides/using-lastpass.md
security_decisions/suppliers/assessing-suppliers.md
security_decisions/suppliers/contracts.md
security_decisions/suppliers/data-destruction-instruction-and-confirmation-letter.md
security_decisions/suppliers/data-destruction-contract-clauses-definitions.md
security_decisions/suppliers/data-destruction-contract-clauses-short-format.md
security_decisions/suppliers/data-destruction-contract-clauses-long-format.md
security_decisions/suppliers/data-destruction-contract-clauses-long-format-appendix.md
security_decisions/suppliers/security-aspect-letters.md
security_decisions/suppliers/supplier-corporate-it.md
security_decisions/mythbusting/cjsm.md
security_decisions/mythbusting/data-sovereignty.md
security_decisions/mythbusting/internet-v-psn.md
security_decisions/mythbusting/ip-dns-diagram-handling.md
security_decisions/mythbusting/multiple-consecutive-back-to-back-firewalls.md
security_decisions/mythbusting/official-official-sensitive.md
contact/email.md
contact/reporting-an-incident.md
contact/vulnerability-disclosure-policy.md
contact/implement-security-txt.md
LAST_LINE
# echo $fullset
pandoc -f gfm -V papersize:A4 -V geometry:margin=2cm -V linkcolor:blue --toc -H $tmpPageBreak $fullset -o doc.pdf
rm -r $tmpFolder
rm $tmpPageBreak
