# Browser and web-application connector matrix

| Stage | Expected evidence | Failure class to investigate |
|---|---|---|
| Target navigation | Intended lab origin reached | DNS, TLS, proxy, redirects or wrong base path |
| Login element discovery | Stable field identified by reviewed selector | Dynamic DOM, localization, stale driver or unsupported page |
| Credential entry | Authorized disposable account used | Secret injection path, encoding, timing or unsupported flow |
| Multi-factor step | Approved interaction and timeout | Unsupported MFA method, conditional policy or session expiry |
| Session establishment | Target application confirms authorized identity | Cookie boundary, redirect loop, application permission or browser isolation |
| Recording/audit | Initiating user and event stage attributed correctly | Session broker integration, retention or collection gap |
| Password lifecycle | Verification/change/reconcile individually tested if supported | Unsupported rotation interface or dependency order |
| Logout/recovery | Session closes and secrets are not left in page/logs | Persistent cookies, abandoned sessions or cleanup failure |

A CPM-style credential-lifecycle integration and a PSM-style browser/session connector solve different problems. Do not label a successful UI login as completed password-management integration. Use separate acceptance evidence for each function. Test browser and driver versions as a compatible pair in a lab, and keep actual page selectors and screenshots private when they reveal the application or environment.

Do not globally bypass certificate validation, disable MFA or weaken access policy to silence a connector error. Compare direct and mediated paths with the same approved account and controlled scope, then isolate the first differing stage.
