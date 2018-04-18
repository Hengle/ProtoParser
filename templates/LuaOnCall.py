# -*- coding: utf-8 -*-

HEADER = """--
-- this file is auto generate by ProtoParser tool.
-- from $fileName
local $moduleName = loadprotobuf "$fileName"
local EMPTY_TABLE = {}
"""

def genOnName(name):
	if name.startswith("on"):
		return name
	return "on" + name[0].upper() + name[1:]

EXPAND_METHOD = """
#if $comment
-- [$cmd] ${comment}
#else
-- [$cmd]
#end if
#set onName = $genOnName($method)
local function ${onName}(data)
	local proto = $moduleName.${className}()
	local ok, msg = proto:Parse(data)
	if not ok then return nil, msg end

	#set values = ["proto." + v for v in $fields]
	#set argText = ", ".join($values)
	return proto, {$argText}
end
"""

COLLAPSED_METHOD = """
#if $comment
-- [$cmd] ${comment}
#else
-- [$cmd]
#end if
#set onName = $genOnName($method)
local function ${onName}(data)
	local proto = $moduleName.${className}()
	local ok, msg = proto:Parse(data)
	if not ok then return nil, msg end

	return proto, EMPTY_TABLE
end
"""

RETURN = """
$functions.sort(key = lambda x: x[0])
return {
#for cmd, fun in $functions
	#set onName = $genOnName($fun)
	[$cmd] = {"$onName", $onName,},
#end for
}
"""
