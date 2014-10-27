url = "http://hosted.app/api/packets"
token = "supersecretusertoken"
import os, sys
from scapy.all import sniff
# create parent function with passed in arguments
def customAction(url,token):
  # uploadPacket function has access to the url & token parameters because they are 'closed' in the nested function
  def uploadPacket(packet):
    # upload packet, using passed arguments
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(packet,token), headers=headers)
  return uploadPacket

if not os.geteuid()==0:
   sys.exit("\n Only root can run this script\n")
  
sniff(prn=customAction(url,token))
