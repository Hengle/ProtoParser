# -*- coding: utf-8 -*-

TEMPLATE = """
-- this file is auto generate by ProtoParser tool.

$up_messages.sort(key = lambda x: x[0])
local send_messages = {
#for cmd, mode, method, protoName in $up_messages
	[$cmd] = "$method",
#end for
}

$dn_messages.sort(key = lambda x: x[0])
local recv_messages = {
#for cmd, mode, method, protoName in $dn_messages
	[$cmd] = "$method",
#end for
}

return {
	send_messages = send_messages,
	recv_messages = recv_messages,
}
"""
