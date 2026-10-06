# Additional service patterns

These notes cover useful adjacent container projects without combining them into a real host inventory. Each service is an independent option, not evidence that it is installed anywhere.

## Management interface

A Portainer-style interface can manage a container engine, but access to the engine socket is highly privileged. A read-only filesystem mount of that socket is not a guarantee that API calls through it cannot change the host. Prefer a separately reviewed management boundary, strong authentication and private administration access. Do not add a public management port to a generic Compose stack merely for convenience.

## Container log viewer

A Dozzle-style viewer makes troubleshooting easier but logs may contain tokens, URLs, identities and application data. Limit collection scope, protect the viewer and consider what engine-level access its connector requires. A public screenshot of a viewer is not automatically safe even after the title is cropped.

## Service homepage

A Homepage-style dashboard should expose only intentional links and non-sensitive status. Configure allowed hosts explicitly, keep service credentials out of browser-delivered configuration, avoid user-specific page titles, and use a fictional set of services for public demonstrations. Do not publish the page as an actual network map.

## DNS filtering

An AdGuard Home-style DNS service has a different risk profile from a web app. Test fallback resolution, port conflicts, local name handling and recovery before changing clients or DHCP. Do not expose an open resolver or publish query logs. A loopback-only web template does not solve DNS network design.

## Firmware dashboard and discovery

A firmware dashboard may need device and discovery access that a restricted bridge network does not provide automatically. Add only the required access after reviewing the integration. Avoid privileged mode, host networking and broad device passthrough as blanket fixes. Firmware credentials and generated binaries are private operational artifacts.

## Acceptance criteria

For each chosen service, define upstream source, reviewed version/digest, storage, expected listener, authentication, health behavior, backup/restore, update and rollback. Start with one service in an isolated lab. Keep the actual inventory, volume names, device identifiers and access routes out of the public repository.

## Broker identity and persistent storage

The MQTT blueprint requires an explicitly reviewed unprivileged UID/GID for the chosen image. Prepare the named volume and credential/ACL files with compatible permissions before startup. An image entrypoint that requires root initialization is not automatically compatible with this restricted example. Validate the entrypoint, volume ownership and broker startup in the lab; do not remove the restrictions blindly to make an unknown image start.
