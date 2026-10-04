# C0055: Quad7 Activity

**Type:** campaign  
**Reference:** https://attack.mitre.org/campaigns/C0055  
**Aliases:** Quad7 Activity  

## Description
Quad7 Activity, also known as CovertNetwork-1658 or the 7777 Botnet, is a network of compromised small office/home office (SOHO) routers. (Citation: Bitsight 7777 Botnet) (Citation: Microsoft Storm-0940) The botnet was initially composed primarily of TP-Link routers and was named Quad7 due to compromised devices exposing TCP port 7777 with the distinctive banner <code>xlogin</code>. Later activity showed a significant increase in compromised Asus routers and the addition of new ports and banners, including TCP port 63256 displaying <code>alogin</code>. Quad7 infrastructure functions as a collection of egress IPs that various China-affiliated threat actors have used to conduct password-spraying and brute-force operations. (Citation: Bitsight 7777 Botnet)(Citation: Medium 777-Botnet) Microsoft has reported that Storm-0940 leveraged credentials obtained through Quad7 Activity to target organizations in North America and Europe, including government agencies, non-governmental organizations, think tanks, law firms, energy firms, IT providers, and defense industrial base entities. (Citation: Microsoft Storm-0940)
