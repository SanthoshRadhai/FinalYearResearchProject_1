# S0231: Invoke-PSImage

**Type:** tool  
**Reference:** https://attack.mitre.org/software/S0231  
**Aliases:** Invoke-PSImage  

## Description
[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this case will dump the passwords. (Citation: GitHub Invoke-PSImage)

## Techniques Used
- T1027.003: Steganography
- T1027.009: Embedded Payloads
