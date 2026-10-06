# Network-storage and backup boundaries

A remote SMB/CIFS or other network share is a possible destination, not proof of a backup. This guide intentionally omits real share names, server addresses, credentials and mount configuration.

Keep share credentials in a protected local credential file outside the repository. Use the platform's supported secure protocol configuration and a narrowly scoped account. Verify that a mount is actually present before writing: an absent mount can cause a backup to fill an unintended local filesystem. Check available capacity, write/read permissions and stable ownership independently.

Create an application-consistent source snapshot before archiving. Encrypt using the intended public recipient before transferring data across a storage boundary. Keep the decryption identity offline or in an approved private store; a public encryption recipient is not a secret, but this archive contains neither recipient nor identity.

A restore test must check more than the checksum. Decrypt privately, inspect the archive paths, restore into a separate disposable destination, validate application consistency and confirm recovery without overwriting the live source. Treat external tar archives as untrusted and defend against path traversal, special files and unexpected ownership before extracting.

Track a successful restore as separate evidence from a successful copy. Avoid automatic deletion or retention scripts until failure handling and storage identification have been reviewed. Do not commit archives, share metadata, test recovery screenshots or actual source lists.
