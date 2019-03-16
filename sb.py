# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, sys
import time

#client = LineClient()
client = LineClient(authToken='ECoNulMpPjTnxa2nmor3.Zirap+Cd4SD+XgEOzbAoeW.x6XIbjUXZaNdkOfZ9GfL4MH0gSec4wzDDko/kcqwlg4=')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

while True:
    try:
        ops=poll.singleTrace(count=50)
        for op in ops:
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                ti = 0
                if msg.text != None:
                    if msg.toType == 2:
                        may = client.getProfile().mid
                        if msg.text.lower() == "!help":
                            client.sendText(receiver, """
Available Commands:
1. !cs < to spot siders >
2. !speed < to check bot's speed >
3. !ls < to make list siders >
4. !help < to see available commands >

That's All (for now)
                            
~ If you want to request more commands, please contact me @Lgd_d
~ If you want to contribute on this bot, please contact me @Lgd_d


                            """)
                        elif msg.text.lower() == "!cs":
                            try:
                                del cctv['point'][msg.to]
                                del cctv['sidermem'][msg.to]
                                del cctv['cyduk'][msg.to]
                            except:
                                pass
                            cctv['point'][receiver] = msg.id
                            cctv['sidermem'][receiver] = ""
                            cctv['cyduk'][receiver]=True

                        elif msg.text.lower() == "!ls":
                            if msg.to in cctv['point']:
                                cctv['cyduk'][msg.to]=False
                                client.sendText(msg.to, cctv['sidermem'][msg.to])
                            else:
                                client.sendText(receiver, "Please type 'check sider' first!")
                            #ti = 1
                        #elif msg.text.lower() == "list sider":
                         #   if msg.to in cctv['point']:#ti == 1:
                            #seconds = 180;
                            #for t in range(seconds):
                               # seconds = seconds - t
                                #time.sleep(1);
                          #      cctv['cyduk'][msg.to]=False
                           #     client.sendText(msg.to, cctv['sidermem'][msg.to])
                                #ti = 0
                            #else:
                             #   client.sendText(receiver, "Please type 'check sider' first!")
                        elif msg.text.lower() == '!speed':
                                start = time.time()
                                client.sendText(receiver, "Bot Speed Test")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%s detik" % (elapsed_time))
                        #elif msg.text.lower() == 'tag all':
                                #group = client.getGroup(msg.to)
                                #nama = [contact.mid for contact in group.members]
                                #client.mention(msg.to, nama)           
                                #client.sendText(receiver, "Members: "+str(jml))
                    else:
                        pass
                else:
                    pass
            elif op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tag all':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                        client.mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                        client.mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                        client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                        client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                        client.mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                        client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                        client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                        client.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                        client.mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                        client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                        client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                        client.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                        client.mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                        client.mention(msg.to, nm5)             
                                        client.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'cek sider':
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'list sider':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    client.sendText(msg.to, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(msg.to, "Nyalain dulu sider checkernya")
                            elif text.lower() == 'shutdown':
                                client.sendText(msg.to, "Shutting Down...")
                                sys.exit()
                                
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))

            elif op.type == OpType.NOTIFIED_READ_MESSAGE:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                #pref=['Sider Spotted','Another Sider']
                                client.sendText(op.param1, 'Sider Spotted '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            elif op.type == OpType.NOTIFIED_INVITE_INTO_GROUP:
                try:
                    group_id=op.param1
                    # Accept group invitation
                    client.acceptGroupInvitation(group_id)
                except Exception as e:
                    client.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
            else:
                pass
                

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
            client.log("[SINGLE_TRACE] ERROR : " + str(e))
