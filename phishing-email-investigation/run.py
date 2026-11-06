from email import policy
from email.parser import Parser
from urllib.parse import urlparse
import re
raw='From: Helpdesk <support@accounts.example>\nTo: user@example.org\nSubject: Urgent account verification\nAuthentication-Results: lab.example; spf=fail; dkim=fail; dmarc=fail\n\nVerify immediately at https://verify.example.net/login\n'
msg=Parser(policy=policy.default).parsestr(raw)
auth=str(msg['Authentication-Results'])
urls=re.findall(r'https?://[^\s]+',msg.get_payload())
sender=str(msg['From']).split('@')[1].rstrip('>')
flags=[x for x in ['spf=fail','dkim=fail','dmarc=fail'] if x in auth]
assert len(flags)==3 and urlparse(urls[0]).hostname!=sender
print('Synthetic message:',raw)
print('Indicators:',flags,'; sender domain:',sender,'; URL domain:',urlparse(urls[0]).hostname)
print('Disposition: suspicious; quarantine and validate through a trusted channel')
print('PASS: authentication-failure and domain-mismatch indicators identified')
