# D3-FC: File Carving

**Reference:** https://d3fend.mitre.org/technique/D3-FC/  

## Definition
Identifying and extracting files from network application protocols through the use of network stream reassembly software.

## Parent Class(es)
- Network Traffic Analysis

## Relationships
- **analyzes:** File Transfer Network Traffic
- **kb-reference:** Reference - Computer Worm Defense System and Method - FireEye Inc

## Knowledge Base Article
## How it works
Protocol stream reassembly software recreates a directional byte stream by analyzing captured network packets. Once the stream is reassembled pattern matching is applied to determine if it contains a file of interest. Files of interest range from executable, archive, or document file formats. Once the file is captured, it is then processed with standard File Analysis Techniques. Example network protocols include HTTP, SMTP, FTP, HTTP/2, and TLS/HTTP/Dropbox.

## Considerations
- This is an error prone process due to the intricacies of network protocols and network packet capture.  For example reassembly may be done in real-time or streaming fashion, or packets may be written to disk, then bulk processed.  The packets may arrive out of order, with fragmentation, duplicates, or re-transmissions.  The reassembly software must compensate for the imperfect packet stream in order to recreate the well formed file which was transmitted.
- File type identification can be a difficult process which can be exploited by adversaries.
