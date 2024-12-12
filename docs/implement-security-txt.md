# Implementing security.txt

Domains where the Ministry of Justice \(MoJ\) is primarily responsible for cyber security **shall** redirect the `/.well-known/security.txt` location to the central `security.txt` file.

This redirection **should** be accessible from the public Internet whether or not the underlying applications or systems are. For example, `https://test.not-production.justice.gov.uk` may be a web-application requiring authentication, however `https://test.not-production.justice.gov.uk/.well-known/security.txt` **should** still be accessible without authentication.

## security.txt

`/.well-known/security.txt` **shall** `HTTP 301` \(permanent redirect\) to `https://security-guidance.service.justice.gov.uk/.well-known/security.txt`.

For example, `https://www.prisonvisits.service.gov.uk/.well-known/security.txt` **shall** `HTTP 301` to `https://security-guidance.service.justice.gov.uk/.well-known/security.txt`.

### `/.well-known/`

We use `/.well-known/` to house `security.txt` as [RFC5785](https://tools.ietf.org/html/rfc5785) defines it as a path prefix for "well-known locations" in selected Uniform Resource Identifier \(URI\) schemes.

## Internal-facing domains

Internal-facing domains resolvable from the public Internet \(for example, `intranet.justice.gov.uk` is based on `.gov.uk` with a publicly routeable IP address\) **should** also implement `security.txt` as described previously.

## Non-production domains

Non-production domains resolvable from the public Internet \(for example, a demonstration deployment of a MoJ digital service or prototype\) **should** also implement `security.txt` as described previously.

## Contact and Feedback

For any further questions or advice relating to security, or for any feedback or suggestions for improvement, contact: [security@justice.gov.uk](mailto:security@justice.gov.uk).

