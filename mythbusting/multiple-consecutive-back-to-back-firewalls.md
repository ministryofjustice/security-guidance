---
expires: 2019-03-15
---
# Multiple consecutive (back-to-back) firewalls

At `OFFICIAL` the MOJ does **not** require or prefer the use of two or more firewalls in a 'back-to-back' fashion unless they are reasonably required due to segregated role or trust management (for example, interconnecting two networks which are managed independently).

### Same rules, same management, different vendor

There is a myth that the use of multiple back-to-back firewalls from different vendors (with the exact same rulesets) is better for security as vulnerabilities that exist in one firewall will not exist in the other however any value of this perceived security benefit (which is likely limited in meaningful benefit anyway) is dwarfed by additional cost, complexity, and maintenance overheads.

### Two networks, two managers

When interconnecting two networks that have different purposes or trust requirements (and when they are potentially managed by different parties) back-to-back firewalls can be used to enforce segregation and ensure managed integration and change control.
